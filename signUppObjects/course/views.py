from django.shortcuts import render,HttpResponse
from django.views.generic import View
from operation.models import UserCourse
from django.db.models import Q
from .models import Course,Cost,Practiceplace
from tradApp.models import Coupon
from users.models import Banner
from operation.models import UserCoupon

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
        try:
            p_id = course.practiceplace_id
            prac = Practiceplace.objects.get(id = p_id)
            print('训练场地--》',p.title)
        except:
            print('出错')

        return render(request,'curriculumDetail.html',{'course':course,'practice':prac})


from tradApp.models import Coach_Orders
from utils.about_pay import get_wxpayUrl,get_alipayUrl

class CourseInfoView(View):
    def get(self,request,course_id):

        course = Course.objects.get(id=course_id)
        # user = request.user
        # other_course_list = []
        # usercourse_list = UserCourse.objects.filter(course=course)[:3]
        # for usercourse in usercourse_list:
        #     u = usercourse.user
        #     user_course = UserCourse.objects.filter(user=u)[:1][0]
        #     other_course_list.append(user_course.course)
        #系统生成订单 和支付的url  随机订单号
        # request.post('username','') 正常获取
        # 现在是get  后来要改成  post
        #判断支付方式
        style_pay = request.GET.get('style','')
        if style_pay == '':
            pay_type = 'aplipay'
        else:
            pay_type = style_pay
        order_sn = request.GET.get('order_sn','')
        if order_sn == '':
            coachOrder = Coach_Orders()
            coachOrder.order_sn = '20150320010101135'
            coachOrder.course_name = 'c1过弯基础课程'
            coachOrder.username = '徐璟灏'
            coachOrder.order_mount = '4650'
            coachOrder.coach_name = '汪鹏'
            coachOrder.pay_type = pay_type
            coachOrder.pay_mount = '1'
            coachOrder.order_status = 'WAIT_BUYER_PAY'
            coachOrder.save()
        else:
            coachOrder = Coach_Orders.objects.filter(order_sn=order_sn)[0]
            coachOrder.pay_type = pay_type
            coachOrder.save()
        if pay_type == 'wechat':
            #微信支付
            payUrl = get_wxpayUrl(coachOrder.order_sn,coachOrder.pay_mount)
            #重定向那个url
        else:
            payUrl = get_alipayUrl(coachOrder.order_sn, coachOrder.pay_mount)
        return render(request,'course-video.html',{'course':course,'coach_order':coachOrder,'alipay_url':payUrl,'style':pay_type})

from .models import Active
import json
class ActiveDetail(View):
    def get(self,request,active_id):
        if not request.user.is_authenticated:
            #每登录正常显示
            active = Active.objects.get(code=active_id)
            coupons = Coupon.objects.filter(active=active)
            banners = Banner.objects.all()
            return render(request,'getCoupon.html',{'coupons':coupons,'active':active,'banners':banners})
        else:
            #判断 是否领取了  （coupon  是否在 UserCoupon）
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

























