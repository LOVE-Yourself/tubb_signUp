import xadmin
from .models import UserCourse,UserCoupon


class UserCourseAdmin(object):

    list_display = ['name','user', 'course','add_time']
    search_fields = ['name','user', 'course']
    list_filter = ['name','user', 'course','add_time']

class UserCouponAdmin(object):
    list_display = ['user','coupon','add_time']
    search_fields = ['user','coupon']
    list_filter = ['user','coupon','add_time']

xadmin.site.register(UserCourse,UserCourseAdmin)
xadmin.site.register(UserCoupon,UserCouponAdmin)