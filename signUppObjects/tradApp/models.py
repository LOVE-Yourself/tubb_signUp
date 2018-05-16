from django.db import models
from datetime import datetime
from users.models import UserProfile
from course.models import Course,Active
# Create your models here.

#模拟器订单
class Simulator_Orders(models.Model):
    Order_Status = (
        ('success', '成功'),
        ('cancel', '取消'),
        ('wait', '待支付'),
    )
    Pay_Type = (
        ('wechat', '微信'),
        ('aplipay', '支付宝'),
    )
    simulatorName = models.CharField(max_length=20,verbose_name=u'模拟器名称')
    simulatorCode = models.CharField(max_length=50,verbose_name=u'模拟器唯一码')
    user = models.ForeignKey(UserProfile, verbose_name=u'用户')
    user_code = models.CharField(max_length=100, verbose_name=u'用户编号')
    order_sn = models.CharField(max_length=30, verbose_name=u'订单号')
    trade_no = models.CharField(max_length=100, unique=True, null=True, blank=True, verbose_name=u'支付生成的订单号')
    address = models.CharField(max_length=100, verbose_name=u'地址')
    appointment_datetime = models.DateField(verbose_name='预约日期')
    appointment_times =  models.CharField(max_length=100,verbose_name='预约时间段')
    order_status = models.CharField(choices=Order_Status, max_length=10, verbose_name='订单状态')
    pay_mount = models.FloatField(default=0.0, verbose_name='支付全额')
    order_mount = models.FloatField(default=0.0, verbose_name='订单金额')
    pay_type = models.CharField(choices=Pay_Type, max_length=10, verbose_name='支付方式')
    pay_time = models.DateTimeField(null=True, blank=True, verbose_name='支付时间')
    pay_intage = models.IntegerField(default=0, verbose_name=u'支付积分')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = u'模拟器订单'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.order_sn)

class Coupon(models.Model):
    Coupon_Status = (('used','已使用'),
                     ('onused','未使用'),
                     )
    Coupon_isOver = (('true','可叠加'),
                     ('false','不可叠加'),
                     )
    Coupon_categry = (('voucher','抵用劵'),
                     ('active','活动券'),
                     )
    # Pay_Type = (
    #     ('wechat','微信'),
    #     ('aplipay','支付宝'),
    # )

    course = models.ForeignKey(Course,verbose_name='课程')
    active = models.ForeignKey(Active,blank=True,null=True,verbose_name='活动')
    belong_course = models.CharField(max_length=20,default='限C1报名',verbose_name='所属课程')
    code = models.CharField(blank=True,null=True,max_length=20,default='1805071231',verbose_name=u'优惠券码')
    coupon_sn = models.CharField(blank=True,null=True,max_length=20,verbose_name=u'优惠劵号')
    # pay_type = models.CharField(choices=Pay_Type, max_length=10, verbose_name='支付方式')
    status = models.CharField(choices=Coupon_Status,max_length=10,verbose_name='使用状态')
    coupon_mount = models.CharField(max_length=10,default='200', verbose_name='面额')
    end_detail = models.TextField(default='自领取之日起30天有效',verbose_name='截止时间')
    isover = models.CharField(max_length=20,choices=Coupon_isOver, null=True, blank=True, verbose_name='是否叠加')
    categry = models.CharField(max_length=20,choices=Coupon_categry,null=True,blank=True,verbose_name='优惠券类别')
    use_time = models.DateTimeField(default=datetime.now,null=True, blank=True, verbose_name='支付时间')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    # belong_activ = models.CharField(default='新春活动',max_length=20,verbose_name='所属活动')
    class Meta:
        verbose_name = u'优惠劵'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.code)

class Coach_Orders(models.Model):
    Order_Status = (
        ('TRADE_SUCCESS','已支付'),
        ('TRADE_CLOSED','已取消'),
        ('WAIT_BUYER_PAY','待支付'),
    )

    Pay_Type = (
        ('wechat','微信'),
        ('aplipay','支付宝'),
    )
    user = models.ForeignKey(UserProfile,null=True,blank=True,verbose_name=u'用户')
    username = models.CharField(null=True,blank=True,max_length=20,verbose_name=u'用户名')
    order_sn = models.CharField(max_length=30,verbose_name=u'订单号')
    coupon_cn = models.CharField(max_length=20,null=True,blank=True,verbose_name=u'优惠劵号')
    trade_no = models.CharField(max_length=100,unique=True,null=True,blank=True,verbose_name=u'支付生成的订单号')
    coach_name = models.CharField(null=True,blank=True,max_length=50,verbose_name='教练名称')
    order_status = models.CharField(choices=Order_Status,default='WAIT_BUYER_PAY',max_length=20,verbose_name=u'订单状态')
    pay_mount = models.FloatField(default=0.0, verbose_name='支付金额')
    order_mount = models.FloatField(null=True,blank=True,default=0.0,verbose_name='订单金额')
    pay_type = models.CharField(choices=Pay_Type,max_length=10,verbose_name='支付方式')
    course_name = models.CharField(max_length=20,verbose_name=u'课程名称')
    pay_time = models.DateTimeField(default=datetime.now,null=True,blank=True,verbose_name='支付时间')
    pay_intage = models.IntegerField(default=0,verbose_name=u'支付积分')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = u'教练订单'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.order_sn)
