from .models import Course,Advantage,Practiceplace,Cost
import xadmin



class CourseAdmin(object):

    list_display = ['name','detail1','detail2','cost_new','cost_old','image','add_time']
    search_fields = ['name','detail1','detail2','cost_new','cost_old','image']
    list_filter = ['name','detail1','detail2','cost_new','cost_old','image','add_time']


class AdvantageAdmin(object):

    list_display = ['course', 'detail','add_time',]
    search_fields = ['course', 'detail',]
    list_filter = ['course', 'detail', 'add_time',]

class PracticeplaceAdmin(object):

    list_display = ['image', 'detail','add_time',]
    search_fields = ['image', 'detail',]
    list_filter = ['image', 'detail','add_time',]

class CostAdmin(object):

    list_display = ['course', 'name','money','add_time',]
    search_fields = ['course', 'name','money']
    list_filter = ['course', 'name','money','add_time']

xadmin.site.register(Course,CourseAdmin)
xadmin.site.register(Advantage,AdvantageAdmin)
xadmin.site.register(Practiceplace,PracticeplaceAdmin)
xadmin.site.register(Cost,CostAdmin)


