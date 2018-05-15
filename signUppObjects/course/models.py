from django.db import models
from datetime import datetime

# from Lyonline.organization.models import CourseOrg
# Create your models here.

#训练场地
class Practiceplace(models.Model):
    title = models.CharField(default='训练场地1',max_length=20,verbose_name='场地名称')
    #后期经纬度
    #long_td = models.DecimalField(max_digits=10, decimal_places=7,verbose_name='经度')#精度
    #lati_td = models.DecimalField(max_digits=10,decimal_places=7,verbose_name='纬度')#纬度
    image = models.ImageField(upload_to='practicplace/%Y/%m',verbose_name=u'封面图')
    detail = models.TextField(verbose_name=u'Tuobaba承诺')
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')
    class Meta:
        verbose_name = u'训练场地'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.title

#课程
class Course(models.Model):
    name = models.CharField(max_length=50,verbose_name=u'课程名称')
    detail1 = models.TextField(default='',verbose_name=u'费用详情')
    detail2 = models.TextField(default='',verbose_name=u'赠送课时')
    cost_new = models.CharField(null=True,blank=True,default='4850',max_length=20,verbose_name=u'现价')
    cost_old = models.CharField(null=True,blank=True,default='5000',max_length=20,verbose_name=u'原价')
    image = models.ImageField(upload_to='course/%Y/%m',max_length=200,verbose_name=u'封面图')
    # click_nums = models.IntegerField(default=0,verbose_name=u'点击数')
    practiceplace = models.ForeignKey(Practiceplace,null=True,blank=True,verbose_name=u'练习场地')
    pay_mount = models.CharField(max_length=20,null=True,blank=True,verbose_name=u'支付金额')
    discount = models.CharField(max_length=20,null=True,blank=True,verbose_name=u'优惠金额')
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'课程'
        verbose_name_plural = verbose_name
    def get_advantages(self):
        return self.advantage_set.all()
    def get_costs(self):
        return self.cost_set.all()

    def __str__(self):
        return self.name

#优势
class Advantage(models.Model):
    course = models.ForeignKey(Course,verbose_name=u'课程')
    detail = models.CharField(max_length=100,verbose_name=u'描述')
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')
    class Meta:
        verbose_name = u'课程优势'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.detail

#费用
class Cost(models.Model):
    course = models.ForeignKey(Course,verbose_name=u'相关课程')
    name = models.CharField(max_length=20,verbose_name=u'费用名称')
    money = models.CharField(max_length=10,verbose_name=u'金额')
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')
    class Meta:
        verbose_name = u'费用明细'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name

#活动
class Active(models.Model):
    title = models.CharField(default='新春活动',max_length=20,verbose_name='活动名称')
    code = models.IntegerField(default=1,verbose_name='活动编号')
    detail = models.TextField(verbose_name='活动规则')
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'活动'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

    # def get_coupons(self):
    #     return self.coupon_set.all()

