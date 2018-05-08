from django.shortcuts import render,HttpResponse
from django.views.generic import View
from operation.models import UserCourse
from django.db.models import Q
from .models import Course,Cost
from tradApp.models import Coupon

# from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
class Courselistview(View):
    def get(self,request):

        course1 = Course.objects.get(id=1)
        course2 = Course.objects.get(id=2)
        return render(request,'enrol.html',{'course1':course1,'course2':course2})

class CourseDetailView(View):
    def get(self,request,course_id):
        print('------suanl ba ---->',course_id)
        try:
            course = Course.objects.get(id=course_id)
        except:
            print('【+】：没有取到相应课程')
        try:
            lesson_count = course.lesson_set.all()#章节数
        except:
            print('[+]:相应课程下的章节出错')

        #相关推荐
        try:
            tag = course.tag
            if tag:
                course_relate = Course.objects.filter(tag=tag)
            else:
                course_relate = []
        except:
            print('[+]:相关推荐出错')
        #判断用户状态
        org_has_fav = False
        course_has_fav= False

        # if request.user.is_authenticated():
        #     if UserFavorrate.objects.filter(user=request.user,fav_id=course.id,fac_type=1):
        #         course_has_fav = True
        #     if UserFavorrate.objects.filter(user=request.user,fav_id=course.org.id,fac_type=2):
        #         org_has_fav = True

        return render(request,'curriculumDetail.html',{'course':course})
        # return render(request,'course-detail.html',{'course':course,
        #                                             'lesson_count':lesson_count,
        #                                             'course_relate':course_relate,
        #                                             'course_has_fav':course_has_fav,
        #                                             'org_has_fav':org_has_fav})

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
        else:
            payUrl = get_alipayUrl(coachOrder.order_sn, coachOrder.pay_mount)
        return render(request,'course-video.html',{'course':course,'coach_order':coachOrder,'alipay_url':payUrl,'style':pay_type})


class GetCoupon(View):
    def get(self,request):
        coupons = Coupon.objects.all()

        return render(request,'getCoupon.html')

class AddCommentView(View):
    def post(self,request):
        print('---->添加评论')
        if not request.user.is_authenticated:

            return HttpResponse("{'status':'fail','msg':'用户未登录'}",content_type='application/json')

        course_id = request.POST.get('course_id',0)
        comments = request.POST.get('comments','')
        print('真的是你吗----》',comments)
        if int(course_id) >0 and comments:
            course = Course.objects.get(id=int(course_id))
            course_comment = CourseComments()
            course_comment.course = course
            course_comment.comments = comments
            course_comment.user = request.user
            course_comment.save()
            return HttpResponse("{'status':'success','msg':'添加成功'}",content_type='application/json')
        else:
            return HttpResponse("{'status':'fail','msg':'添加失败'}",content_type='application/json')


