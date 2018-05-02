from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
# Create your views here.
from .models import CourseOrg,CityDict
from .forms import UserAskForm
from operation.models import UserFavorrate

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

class Orglistview(View):
    def get(self,request):

        all_orgs = CourseOrg.objects.all()
        city_list = CityDict.objects.all()

        city_id = request.GET.get('city','')
        if city_id:
            all_orgs = all_orgs.filter(city_id = int(city_id))

        category = request.GET.get('ct', '')
        if category:
            all_orgs = all_orgs.filter(catgory=category)

        sort = request.GET.get('sort','')
        if sort:
            if sort == 'students':
                all_orgs = all_orgs.order_by('-students')
            elif sort == 'courses':
                all_orgs = all_orgs.order_by('-courses_nums')
        current_nav = 'org_nav'
        #排名
        hot_orgs= all_orgs.order_by('-click_nums')[:3]
        org_count = all_orgs.count()
        try:
            page = request.GET.get('page', 1)

        except PageNotAnInteger:
            page = 1

        # Provide Paginator with the request object for complete querystring generation

        p = Paginator(all_orgs, 2,request=request)

        orgs = p.page(page)
        return render(request,'org-list.html',{'all_orgs':orgs,
                                               'city_list':city_list,
                                               'city_id':city_id,
                                               'category':category,
                                               'count':org_count,
                                               'hot_orgs':hot_orgs,
                                               'sort':sort,
                                               'current_nav':current_nav})

class AskUserView(View):
    def post(self,request):
        userAsk_form = UserAskForm(request.POST)
        print('----来了吗--》')
        if userAsk_form.is_valid():
            userAsk = userAsk_form.save(commit=True)#保存到数据库
            print('-------->')
            return HttpResponse("{'status':'success'}",content_type='application/json')
        else:
            return HttpResponse("{'status':'fail','msg':{0}}".format(userAsk_form.errors),content_type='application/json')


class OrgHomeView(View):
    def get(self,request,org_id):
        print('-->',org_id)
        course_org = CourseOrg.objects.get(id=int(org_id))
        courses = course_org.course_set.all()#获取机构下课程
        teachers = course_org.teacher_set.all()
        desc = course_org.desc
        print('--?--->',courses)
        print('------??????',desc)
        current = 'home'
        return render(request,'org-detail-homepage.html',{'courses':courses,
                                                          'teachers':teachers,
                                                          'desc':desc,
                                                          'course_org':course_org,
                                                          'current':current})
class OrgCourseView(View):
    def get(self,request,org_id):
        print('-->',org_id)
        course_org = CourseOrg.objects.get(id=int(org_id))
        courses_all = course_org.course_set.all()#获取机构下课程
        current = 'course'
        try:
            page = request.GET.get('page', 1)

        except PageNotAnInteger:
            page = 1
        p = Paginator(courses_all, 4,request=request)
        courses = p.page(page)
        return render(request,'org-detail-course.html',{'courses':courses,
                                                          'course_org':course_org,
                                                        'current':current})

class OrgDescView(View):

    def get(self,request,org_id):
        print('-------->sidie',org_id)
        current = 'desc'
        course_org = CourseOrg.objects.get(id=int(org_id))
        desc = course_org.desc

        return render(request,'org-detail-desc.html',{'desc':desc,'current':current,'course_org':course_org})


class OrgTeacherView(View):
    def get(self,request,org_id):
         course_org = CourseOrg.objects.get(id=int(org_id))
         teachers = course_org.teacher_set.all()
         current = 'teacher'
         return render(request,'org-detail-teachers.html',{'teachers':teachers,'course_org':course_org,'current':current})

class AddFavView(View):
    def post(self,request):
        print('jia jia huilaiba ----???>>>>')
        fav_id = request.POST.get('fav_id',0)#0防止int出错
        fac_type = request.POST.get('fav_type',0)
        if not request.user.is_authenticated():
            return render(request,'login.html')

        exist_recordes = UserFavorrate.objects.filter(request.user,fav_id=int(fav_id),fac_type=int(fac_type))
        if exist_recordes:
            print('已收藏,改为取消')
            exist_recordes.delete()
        user_fav = UserFavorrate()
        if int(fav_id)>0 and int(fac_type)>0:
            user_fav.fav_id = fav_id
            user_fav.fac_type = fac_type
            user_fav.save()
        print('收藏出错')

        print('------>id',fav_id)

    def get(self,request):
        print('??????/为什么')


