from django.db import models
from datetime import datetime
from organization.models import CourseOrg
# from Lyonline.organization.models import CourseOrg
# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=50,verbose_name=u'课程名称')
    # org = models.ForeignKey(CourseOrg, verbose_name=u'所属机构',null=True,blank=True)
    # desc = models.CharField(max_length=300,verbose_name=u'课程描述')
    detail1 = models.TextField(default='',verbose_name=u'费用详情')
    detail2 = models.TextField(default='',verbose_name=u'赠送课时')
    cost_new = models.CharField(null=True,blank=True,default='4850',max_length=20,verbose_name=u'现价')
    cost_old = models.CharField(null=True,blank=True,default='5000',max_length=20,verbose_name=u'原价')
    # degree = models.CharField(max_length=20,choices=(('cj','初级'),('zj','中级'),('gj','高级')))
    # category = models.CharField(default=u'后端开发',max_length=20,verbose_name=u'课程类别')
    # learn_times = models.IntegerField(default=0,verbose_name=u'学习时长(分)')
    # students = models.IntegerField(default=0,verbose_name='学习人数')
    # fav_nums = models.IntegerField(default=0,verbose_name=u'收藏人数')
    image = models.ImageField(upload_to='course/%Y/%m',max_length=200,verbose_name=u'封面图')
    # click_nums = models.IntegerField(default=0,verbose_name=u'点击数')
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')
    # tag = models.CharField(verbose_name=u'课程标签',default='',max_length=50)

    class Meta:
        verbose_name = u'课程'
        verbose_name_plural = verbose_name
    def get_advantages(self):
        return self.advantage_set.all()

    # def get_learn_users(self):
    #     return self.usercourse_set.all()
    # def get_lesson(self):
    #     return self.lesson_set.all()
    # def get_comment(self):
    #     return self.coursecomments_set.all()
    # def get_resource(self):
    #     return self.courseresource_set.all()
    def __str__(self):
        return self.name

class Advantage(models.Model):
    course = models.ForeignKey(Course,verbose_name=u'课程')
    detail = models.CharField(max_length=100,verbose_name=u'描述')
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')

class Practiceplace(models.Model):
    image = models.ImageField(upload_to='practicplace /%Y/%m', max_length=200, verbose_name=u'封面图')
    detail = models.TextField(verbose_name=u'Tuobaba承诺')
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')


class Cost(models.Model):
    course = models.ForeignKey(Course,verbose_name=u'相关课程')
    name = models.CharField(max_length=50,verbose_name=u'费用名称')
    models.CharField(max_length=30,verbose_name=u'金额')
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')


