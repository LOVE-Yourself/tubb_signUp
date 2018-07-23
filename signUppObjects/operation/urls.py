from django.conf.urls import url

from .views import KitecarView,JoinUsVIew,AboutView,LoadAppView

urlpatterns = [

    # url(r'course_list/(?P<sort>\d+)$',Courselistview.as_view() ,name='courseList'),
    url(r'kitcar/$',KitecarView.as_view(),name='kitcar'),
    url(r'loadapp/$',LoadAppView.as_view(),name='loadapp'),
    url(r'about/$',AboutView.as_view(),name='about'),
    url(r'joinus/$',JoinUsVIew.as_view(),name='joinus'),

]
