from django.conf.urls import url

from .views import Orglistview,AskUserView,OrgHomeView,OrgCourseView,OrgDescView,OrgTeacherView,AddFavView

urlpatterns = [

    url(r'org_list/$',Orglistview.as_view() ,name='orgList'),
    url(r'user_ask/$',AskUserView.as_view() ,name='user_Ask'),
    url(r'detail_home/(?P<org_id>\d+)$',OrgHomeView.as_view() ,name='org_home'),
    url(r'detail_cousre/(?P<org_id>\d+)$', OrgCourseView.as_view(), name='org_course'),
    url(r'detail_desc/(?P<org_id>\d+)$', OrgDescView.as_view(), name='org_desc'),
    url(r'detail_teacher/(?P<org_id>\d+)$', OrgTeacherView.as_view(), name='org_teacher'),
    url(r'org_fav/$', AddFavView.as_view(), name='org_fav'),
]