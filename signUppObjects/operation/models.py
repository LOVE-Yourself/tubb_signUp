from datetime import datetime

from django.db import models

from  course.models import Course
from  users.models import UserProfile


# from ..course.models import Course
# from Lyonline.users import UserProfile



# Create your models here.

class userAsk(models.Model):
    name = models.CharField(max_length=20,verbose_name=u'姓名')
    telphone = models.CharField(verbose_name=u'手机',max_length=11)
    coure_name = models.CharField(max_length=50,verbose_name=u'课程名')
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'用户咨询'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name

class CourseComments(models.Model):
    user = models.ForeignKey(UserProfile,verbose_name=u'用户')
    course = models.ForeignKey(Course,verbose_name=u'课程')
    comments = models.CharField(max_length=200,verbose_name=u'评论')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'课程评论'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name


class UserFavorrate(models.Model):
    user = models.ForeignKey(UserProfile,verbose_name=u'用户')
    fav_id = models.IntegerField(default=0,verbose_name=u'数据id')
    fac_type = models.IntegerField(choices=((1,u'课程'),(2,u'课程机构'),(3,u'讲师')),verbose_name=u'收藏类型')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'用户收藏'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name

class UserMessage(models.Model):
    user = models.IntegerField(default=0,verbose_name=u'接受用户')
    message = models.CharField(max_length=500,verbose_name=u'消息')
    has_read = models.BooleanField(default=False,verbose_name=u'是否已读')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'用户消息'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name

class UserCourse(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u'用户')
    course = models.ForeignKey(Course, verbose_name=u'课程')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'用户课程'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name