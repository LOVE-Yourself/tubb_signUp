from datetime import datetime

from django.db import models

from  course.models import Course
from  users.models import UserProfile
from tradApp.models import Coupon

# from ..course.models import Course
# from Lyonline.users import UserProfile
# Create your models here.

#用户报名课程
class UserCourse(models.Model):
    name = models.CharField(default='报名C1',max_length=10,verbose_name='报名课程')
    user = models.ForeignKey(UserProfile, verbose_name=u'用户')
    course = models.ForeignKey(Course, verbose_name=u'课程')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'用户课程'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name

#用户领券
class UserCoupon(models.Model):

    user = models.ForeignKey(UserProfile, verbose_name=u'用户')
    coupon = models.ForeignKey(Coupon,null=True,blank=True,verbose_name=u'优惠劵 ')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'用户优惠劵'
        verbose_name_plural = verbose_name

