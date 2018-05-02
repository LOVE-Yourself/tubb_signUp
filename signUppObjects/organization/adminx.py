import xadmin
from .models import CourseOrg,CityDict,Teacher



class CourseOrgAdmin(object):

    list_display = ['name','desc','address','fav_nums','image','click_nums','add_time','city']
    search_fields = ['name','desc','address','fav_nums','image','click_nums','city']
    list_filter = ['name','desc','address','fav_nums','image','click_nums','add_time','city']

class CityDictAdmin(object):

    list_display = ['name','desc','add_time']
    search_fields = ['name','desc']
    list_filter = ['name','desc','add_time']

class TeacherAdmin(object):

    list_display = ['org', 'name','work_years','work_company','work_position','points','fav_nums','click_nums','add_time']
    search_fields = ['org', 'name','work_years','work_company','work_position','points','fav_nums','click_nums']
    list_filter = ['org', 'name','work_years','work_company','work_position','points','fav_nums','click_nums','add_time']


# xadmin.site.register(CourseOrg, CourseOrgAdmin)
# xadmin.site.register(CityDict, CityDictAdmin)
# xadmin.site.register(Teacher, TeacherAdmin)



