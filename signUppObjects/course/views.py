from django.shortcuts import render,HttpResponse
from django.views.generic import View
from operation.models import UserCourse
from django.db.models import Q
from .models import Course,Cost,Practiceplace
from tradApp.models import Coupon
from users.models import Banner
from operation.models import UserCoupon
from users.forms import LoginForm
# from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
class Courselistview(View):
    def get(self,request):
        try:
            course1 = Course.objects.get(id=1)
            course2 = Course.objects.get(id=2)
        except:
            print('【+课程列表页】：没有取到课程列表')
        try:
            banners = Banner.objects.all()
        except:
            print('【+课程列表页】：没有取到轮播图')
        return render(request,'enrol.html',{'course1':course1,'course2':course2,'banners':banners})

class CourseDetailView(View):
    def get(self,request,course_id):

        try:
            course = Course.objects.get(id=course_id)
        except:
            print('【+】：没有取到相应课程')


        return render(request,'curriculumDetail.html',{'course':course,})


class CourseInfoView(View):
    def get(self,request,course_id):
        user = request.user
        course = Course.objects.get(id=course_id)
        user_coupons = UserCoupon.objects.filter(user=user)
        if course.name == 'C1超越期望优质课':
            style = '限C1报名'
        else:
            style = '限C2报名'
        coupons = []
        for user_coupon in user_coupons:
            if user_coupon.coupon.belong_course == style:
                if user_coupon.coupon.status == 'onused':
                    coupons.append(user_coupon.coupon)
        mount = 0
        for coupon in coupons:
            mount = mount + int(coupon.coupon_mount)

        course.discount = str(mount)
        course.pay_mount = int(course.cost_new) - mount
        course.save()

        return render(request,'writeOrderForm.html',{'course':course,'coupons':coupons})

from .models import Active
import json
class ActiveDetail(View):
    def get(self,request,active_id):
        if not request.user.is_authenticated:

            print('----判断登录-->')
            #每登录正常显示
            active = Active.objects.get(code=active_id)
            coupons = Coupon.objects.filter(active=active)
            banners = Banner.objects.all()
            return render(request,'getCoupon.html',{'coupons':coupons,'active':active,'banners':banners})
        else:
            #判断 是否领取了  （coupon  是否在 UserCoupon）
            try:
                user = request.user
                print('--username-->',user.username)
                usercoupons = UserCoupon.objects.filter(user=user)
                l = []
                for usercoupon in usercoupons:
                    l.append(usercoupon.coupon)
                active = Active.objects.get(code=active_id)
                coupons = Coupon.objects.filter(active=active)
                banners = Banner.objects.all()
                return render(request,'getCoupon.html',{'coupons':coupons,'active':active,'banners':banners,'usercoupons':l})
            except:
                print('---未登录-->')
                login_form = LoginForm()
                # 每登录正常显示
                active = Active.objects.get(code=active_id)
                coupons = Coupon.objects.filter(active=active)
                banners = Banner.objects.all()
                return render(request, 'getCoupon.html', {'coupons': coupons, 'active': active, 'banners': banners,'login_form':login_form})

    def post(self,request):
        print('---登录失败-->')
        login_form = LoginForm(request.POST)
        active_code = request.POST.get('active_code','')
        
        # 每登录正常显示
        active = Active.objects.get(code=active_code)
        coupons = Coupon.objects.filter(active=active)
        banners = Banner.objects.all()
        return render(request, 'getCoupon.html',
                      {'coupons': coupons, 'active': active, 'banners': banners, 'login_form': login_form})


                      
class GetCoupon(View):
    def get(self,request):
        pass
    def post(self,request):
        #判断登录状态
        if request.user.is_authenticated():
            coupon_id = request.POST.get('coupon_id','')
            active_id = request.POST.get('active_id','')
            print('-cp-->',coupon_id)
            print('--ac--->', active_id)
            usercoupon = UserCoupon()
            coupon = Coupon.objects.get(code=coupon_id)
            usercoupon.user = request.user
            usercoupon.coupon = coupon
            usercoupon.save()

            resp = {'status': 200,'msg':'领取成功'}   #前段拿到200 window reload
            return HttpResponse(json.dumps(resp), content_type='application/json')
        else:
            print('----->未登录')
            resp = {'status':202,'msg':'未登录'}
            return HttpResponse(json.dumps(resp), content_type='application/json')

























