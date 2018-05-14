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

























