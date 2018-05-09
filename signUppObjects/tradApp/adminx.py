from .models import Coach_Orders,Simulator_Orders,Coupon

import xadmin

class Coach_OrdersAdmin(object):

    list_display = ['username','order_sn','trade_no','coach_name','order_status','pay_mount','order_mount','pay_type','course_name','pay_time','coupon_cn','pay_intage','add_time']
    search_fields = ['username','order_sn','trade_no','coach_name','order_status','pay_mount','order_mount','pay_type','course_name','coupon_cn','pay_intage']
    list_filter = ['username','order_sn','trade_no','coach_name','order_status','pay_mount','order_mount','pay_type','course_name','pay_time','coupon_cn','pay_intage','add_time']



class Simulator_OrdersAdmin(object):

    list_display = ['simulatorName','simulatorCode','user','user_code','order_sn','trade_no','address','appointment_datetime','appointment_times','order_status','pay_mount','order_mount','pay_type','pay_time','pay_intage','add_time']
    search_fields = ['simulatorName','simulatorCode','user','user_code','order_sn','trade_no','address','appointment_datetime','appointment_times','order_status','pay_mount','order_mount','pay_type','pay_intage']
    list_filter = ['simulatorName','simulatorCode','user','user_code','order_sn','trade_no','address','appointment_datetime','appointment_times','order_status','pay_mount','order_mount','pay_type','pay_time','pay_intage','add_time']


class CouponAdmin(object):
    list_display = ['course','active','belong_course','code','coupon_sn','status','coupon_mount','end_detail','use_time','add_time']
    search_fields = ['course','active','belong_course','code','coupon_sn','status','coupon_mount','end_detail']
    list_filter = ['course','active','belong_course','code','coupon_sn','status','coupon_mount','end_detail','use_time','add_time']



xadmin.site.register(Coach_Orders,Coach_OrdersAdmin)
xadmin.site.register(Simulator_Orders,Simulator_OrdersAdmin)
xadmin.site.register(Coupon,CouponAdmin)

