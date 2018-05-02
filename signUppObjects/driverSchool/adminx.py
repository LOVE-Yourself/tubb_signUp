from .models import Coach,DriverSchool

import xadmin



class CoachAdmin(object):

    list_display = ['name','age','sex','address','telphone','catgory','students','years_old','long_td','code','add_time']
    search_fields = ['name','age','sex','address','telphone','catgory','students','years_old','long_td','code']
    list_filter = ['name','age','sex','address','telphone','catgory','students','years_old','long_td','code','add_time']


class DriverSchoolAdmin(object):
    list_display = ['name','add_time']
    search_fields = ['name']
    list_filter = ['name','add_time']

xadmin.site.register(Coach,CoachAdmin)
xadmin.site.register(DriverSchool,DriverSchoolAdmin)

