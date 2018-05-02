from django.db import models
from datetime import datetime

# Create your models here.
class DriverSchool(models.Model):
    name = models.CharField(max_length=50,verbose_name=u'驾校名称')
    # desc = models.TextField(verbose_name=u'机构描述')
    # catgory = models.CharField(verbose_name=u'机构分类',default='pxjg',max_length=20,choices=(('pxjg','培训机构'),('gx','高校'),('gr','个人')))
    # address = models.CharField(max_length=150,verbose_name=u'机构地址')
    # fav_nums = models.IntegerField(default=0,verbose_name=u'收藏人数')
    # image = models.ImageField(upload_to='org/%Y/%m',max_length=200,verbose_name=u'封面图')
    # click_nums = models.IntegerField(default=0,verbose_name=u'点击数')
    # students = models.IntegerField(default=0,verbose_name=u'学习人数')
    # courses_nums = models.IntegerField(default=0,verbose_name=u'课程数')
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')
    # city = models.ForeignKey(CityDict,verbose_name=u'所在区域')

    class Meta:
        verbose_name = u'驾校机构'
        verbose_name_plural = verbose_name

    # def org_teachers(self):
    #     org_teacher_list = self.teacher_set.all()
    #     return org_teacher_list
    #
    # def org_courses(self):
    #     org_course_list = self.course_set.all()
    #     return org_course_list

    def __str__(self):
        return self.name


#教练
class Coach(models.Model):
    org = models.ForeignKey(DriverSchool,verbose_name=u'所属驾校')
    name = models.CharField(null=True,blank=True,verbose_name='昵称',max_length=10)
    age = models.IntegerField(verbose_name=u'年龄',null=True,blank=True)
    sex = models.CharField(max_length=5,choices=(('male',u'男'),('female',u'女')))
    address = models.CharField(max_length=100,verbose_name=u'区域')
    telphone = models.CharField(max_length=11,null=True,blank=True)
    # image = models.ImageField(upload_to='image/%Y/%m',default=u'image/default.png',max_length=100)
    catgory = models.CharField(verbose_name=u'驾驶证类型', default='c1', max_length=10,choices=(('c1', '高级'), ('c2', '中级'), ('c3', '低级')))
    students = models.IntegerField(default=0, verbose_name=u'学生人数')
    years_old = models.IntegerField(default=0,verbose_name=u'驾龄')
    long_td = models.DecimalField(null=True,blank=True,max_digits=10, decimal_places=7,verbose_name='经度')#精度
    lati_td = models.DecimalField(null=True,blank=True,max_digits=10,decimal_places=7,verbose_name='纬度')#纬度
    code = models.CharField(null=True,blank=True,max_length=20,verbose_name='城市编码')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = u'教练信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name



#教练练习场地
class CoachActiveAdress(models.Model):
    name = models.CharField(null=True,blank=True,verbose_name='名称',max_length=10)
    address = models.CharField(max_length=100,verbose_name=u'区域')
    # image = models.ImageField(upload_to='image/%Y/%m',default=u'image/default.png',max_length=100)
    long_td = models.DecimalField(max_digits=10, decimal_places=7,verbose_name='经度')#精度
    lati_td = models.DecimalField(max_digits=10,decimal_places=7,verbose_name='纬度')#纬度
    code = models.CharField(max_length=20,verbose_name='城市编码')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = u'教练练习场地'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name