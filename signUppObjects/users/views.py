from django.contrib.auth import authenticate, login, hashers
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.http import HttpResponseRedirect
from django.views.generic import View
from django.contrib.auth.hashers import make_password,check_password
import json,random
# from  utils.util import send_email
from .forms import LoginForm,RegisterForm,ForgetForm,ChangeForm,UploadImageForm
from .models import UserProfile,TelNumVerifyRecord
from utils.util import isauth
# Create your views here.

class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username)|Q(email=username)|Q(nick_name=username))
            if user.check_password(password):
                return user
            return None

        except Exception as e :
            print(e)

            return None

#忘记密码
class ForgetView(View):
    def get(self,request):
        forget_form = ForgetForm()
        return render(request, 'forgetpwd.html', {'forget_form':forget_form})
    def post(self,request):
        forget_form = ForgetForm(request.POST)
        if forget_form.is_valid():
            passw1 = request.POST.get('password1', '')
            passw2 = request.POST.get('password2', '')
            if passw1 != passw2:
                return render(request, 'forgetpwd.html', {'forget_form': forget_form, 'msg': '两次输入密码不一致'})
            telphone = request.POST.get('username', '')
            code = request.POST.get('verifyNum', '')
            send_type = request.POST.get('send_type','')
            try:
                user = UserProfile.objects.get(telphone=telphone)
            except:
                return render(request, 'forgetpwd.html', {'forget_form': forget_form, 'msg': '该手机号未注册'})
            try:
                VerifyRecord = TelNumVerifyRecord.objects.filter(telnum=telphone, code=code,send_type=send_type).order_by('-send_time')[0]
                five_munite_ago = datetime.now() - timedelta(hours=0,minutes=5,seconds=0)
                if VerifyRecord:
                    if VerifyRecord.send_time  < five_munite_ago:
                        return render(request, 'forgetpwd.html', {'forget_form': forget_form, 'msg': '验证码已过期'})
                    elif VerifyRecord.code != code:
                        return render(request, 'forgetpwd.html', {'forget_form': forget_form, 'msg': '验证码不符请重试'})
                    try:
                        pwd = hashers.make_password(passw1)
                        user.password = pwd
                        user.save()
                    except:
                        print('【+】：将数据保存后台出错')
                        return render(request, 'forgetpwd.html', {'forget_form': forget_form, 'msg': '网络延迟'})
                    return HttpResponseRedirect('/users/login/')
            except:
                return render(request, 'forgetpwd.html', {'forget_form': forget_form, 'msg': '内部服务器错误，请重试'})
        else:
            return render(request, 'forgetpwd.html', {'forget_form': forget_form})


class LoginView(View):
    def get(self,request):
        login_form = LoginForm()
        j = request.GET.get('j', '')
        print('?-<>',j)
        course_id = request.GET.get('course_id', '')
        return render(request, 'login.html', {'login_form': login_form, 'j': j, 'course_id': course_id})

    def post(self,request):
        login_form = LoginForm(request.POST)
        j = request.POST.get('j', '')
        course_id = request.POST.get('course_id', '')

        if login_form.is_valid():
            username = request.POST.get('username','')
            password1 = request.POST.get('password','')

            try:
                user = UserProfile.objects.get(username=username)
            except:
                return render(request, 'login.html', {'login_form':login_form, 'msg': '该手机号未注册', 'j':j, 'course_id':course_id})
            user = authenticate(username = username,password = password1)
            if user is  None:
                return render(request, 'login.html', {'login_form':login_form, 'msg': '用户名或密码错误', 'j':j, 'course_id':course_id})
            else:
                login(request, user)

                print('--->oldme-->',j)
                if j == '2':
                    return HttpResponseRedirect('/course/course_info/{0}'.format(course_id))
                elif j == '1':
                    return HttpResponseRedirect('/users/user_info')
                elif j == '3':
                    return HttpResponseRedirect('/course/active_detail/1')
                return HttpResponseRedirect('/')
        return render(request, 'login.html', {'login_form':login_form, 'j':j, 'course_id':course_id})


from utils.send_code import YunPian
from datetime import datetime,timedelta
from django.views.decorators.csrf import csrf_exempt,csrf_protect

class GetveryCode(View):
    def get(self,request):
        pass
    @csrf_exempt
    def post(self,request):
        telnum = request.POST.get('phone', '')
        VerifyRecord = TelNumVerifyRecord.objects.filter().order_by('-send_time')[0]
        four_munite_ago = datetime.now() - timedelta(hours=0,minutes=4,seconds=0)
        if VerifyRecord:
            if VerifyRecord.send_time > four_munite_ago:
                resp = {'status': 404, 'code': VerifyRecord.code, 'msg': '请求频繁'}
                return HttpResponse(json.dumps(resp), content_type='application/json')

        print('---号码发送验证码---->',telnum)
        send_type = request.POST.get('send_type','')
        if telnum == '':
            print('【获取验证码】电话号码为空')
        yun_pain = YunPian('05e6858c497059ebea9bc5b81b08f37d')
        code = yun_pain.get_code()
        status = yun_pain.send_code(code,telnum,send_type)
    #2分钟让它失效
        if status == '发送成功':
            resp = {'status': 200, 'code':code,'msg':'发送成功' }
            #将验证码保存到表中
            VerifyRecord = TelNumVerifyRecord()
            VerifyRecord.code = code
            VerifyRecord.telnum = telnum
            VerifyRecord.send_type = send_type
            VerifyRecord.save()
        else:
            resp = {'status':404,'code':code,'msg':'请求频繁'}
        return HttpResponse(json.dumps(resp), content_type='application/json')

class RegistView(View):
    def get(self,request):
        register_form = RegisterForm()
        return render(request, 'register.html', {'register_form':register_form})
    def post(self,request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            passw1 = request.POST.get('password1','')
            passw2 = request.POST.get('password2','')
            if passw1 != passw2:
                return render(request, 'register.html', {'register_form':register_form, 'msg': '两次输入密码不一致'})
            telphone = request.POST.get('username','')
            code = request.POST.get('verifyNum','')
            try:
                user = UserProfile.objects.get(telphone=telphone)
                if user:
                    return render(request, 'register.html', {'register_form':register_form, 'msg': '该手机号已注册过'})
            except:
                print('【+】该手机可以注册')
            try:
                VerifyRecord = TelNumVerifyRecord.objects.filter(telnum=telphone,code=code,send_type='register').order_by('-send_time')[0]
                if VerifyRecord:
                    five_minute_ago = datetime.now() - timedelta(hours=0,minutes=5,seconds=0)
                    if VerifyRecord.send_time < five_minute_ago:
                        return render(request, 'register.html', {'register_form': register_form, 'msg': '验证码已经过期'})
                    else:
                        password = request.POST.get('password1', '')
                        username = request.POST.get('username', '')
                        try:
                            user = UserProfile()
                            user.username = username
                            user.telphone = telphone
                            user.set_password(password)
                            user.save()
                        except:
                            print('【+】：将数据保存后台出错')
                            return render(request, 'register.html', {'register_form': register_form, 'msg': '网络延迟'})
                        return HttpResponseRedirect('/users/login/')  # http://www.baidu.com/‘
            except:
                return render(request, 'register.html', {'register_form':register_form, 'msg': '服务器内部出错,请重试'})
        else:
            return render(request, 'register.html', {'register_form':register_form})
#------------个人详情页------------------------------------------------------------------------>>>>>>>>>>>>>>
from tradApp.models import Coupon
from operation.models import UserCoupon


class UserInfoView(View):
    @isauth
    def get(self,request):
        return render(request, 'personalInfo.html')

class UserCouponView(View):
    @isauth
    def get(self,request):
        status = request.GET.get('ct', '')
        if status == '':
            status = 'onused'
        user = request.user
        coupons = []
        usercoupons = UserCoupon.objects.filter(user=user,status=status)
        return render(request, 'personalCoupon.html', {'usercoupons': usercoupons, 'status': status})
        # try:
        # except:
        #     return HttpResponseRedirect('/users/login/?j=3')


class UserOrderView(View):
    def get(self,request):
        try:
            user = request.user
            return  render(request,'personalOrder.html')
        except:
            return HttpResponseRedirect('/users/login/?j=3')




class UserUploadImageView(View):
    def post(self,request):

        uploadForm = UploadImageForm(request.POST,request.FILES)

        if uploadForm.is_valid():
            request.user.image = uploadForm.cleaned_data['image']
            request.user.save()
            print('成功了  我想你 ')
            return HttpResponse("{'status':'success'}",content_type='application/json')


        return HttpResponse("{'status':'fail'}",content_type='application/json')

class UserUploadPwd(View):
    def post(self,request):

        # if not request.user.is_authenticated():
        #     return render(request,'login.html')
        user = request.user
        change_form = ChangeForm(request.POST)
        if change_form.is_valid():
            print('-->user', request.user)
            new_pwd = request.POST.get('password','')
            reset_pwd= request.POST.get('password2','')
            if new_pwd == reset_pwd:

                print('------>pwd',user.password)
                user.password = make_password(new_pwd)
                print('------------------->yuntoy ')
                user.save()
                print('充公了吗？？？？//复杂化了把')

                return HttpResponse("{'status':'success'}", content_type='application/json')
            else:
                return HttpResponse("{'status':'fail','msg':'前后密码不一致'}",content_type='application/json')

        return HttpResponse(json.dumps(change_form.errors), content_type='application/json')

from django.shortcuts import render_to_response
def page_not_found(request):
    response = render_to_response('404.html',{})
    response.status_code =404
    return response
# class page_not_found(View):
#     print('lail---------------->')
#     def get(self,request):
#          return render(request,'404.html')


