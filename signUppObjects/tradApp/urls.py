from django.conf.urls import url

from .views import AlipayReturnView,NotyfileReturnView,Notify_ReturnView,wxpay_View,Payfor

urlpatterns = [

    # url(r'course_list/(?P<sort>\d+)$',Courselistview.as_view() ,name='courseList'),
    url(r'payfor/$',Payfor.as_view(),name='payfor'),
    url(r'alipay_return/$',AlipayReturnView.as_view(),name='alipay_return'),
    url(r'notyfile_return/$',NotyfileReturnView.as_view(),name='notyfile_return'),
    url(r'wxnotify/$',Notify_ReturnView.as_view(),name='wx_notify'),
    url(r'wxpay/$',wxpay_View.as_view(),name='wxpay'),

]

