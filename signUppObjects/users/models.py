from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class UserProfile(AbstractUser):
    #默认有username 字段
    nick_name = models.CharField(null=True, blank=True, max_length=50, verbose_name=u'昵称',default=u'拓吧叭学员')
    sex = models.CharField(max_length=5,choices=(('male',u'男'),('female',u'女')))
    telphone = models.CharField(max_length=11,null=True,blank=True)
    image = models.ImageField(upload_to='image/%Y/%m',default=u'image/default.png',max_length=100)

    class Meta:
        verbose_name = u'用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class TelNumVerifyRecord(models.Model):
    code = models.CharField(max_length=20,verbose_name=u'验证码')
    telnum = models.CharField(max_length=50,verbose_name=u'电话号码')
    send_type = models.CharField(max_length=20,choices=(('register',u'注册'),('forget',u'忘记密码')))
    status = models.CharField(max_length=20,choices=(('true',u'可用'),('fail',u'已过期')))
    send_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = u'短信验证'
        verbose_name_plural = verbose_name

    def  __str__(self):
        return '{0}({1})'.format(self.code,self.telnum)

class Banner(models.Model):
    title = models.CharField(max_length=100,verbose_name=u'标题')
    image = models.ImageField(max_length=200,upload_to='banner/%y/%m',verbose_name=u'轮播')
    url = models.URLField(max_length=200,verbose_name=u'访问地址')
    index = models.IntegerField(default=100,verbose_name=u'顺序')
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u'添加日期')

    class Meta:
        verbose_name = u'轮播图'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
