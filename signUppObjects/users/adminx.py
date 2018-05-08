import xadmin
from .models import TelNumVerifyRecord,Banner

from xadmin import views


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True

class GlobalSettings(object):
    site_title = 'tuobaba学车平台'
    site_footer = '拓叭吧VR学车'
    menu_style = 'accordion'#下拉菜单

class TelNumVerifyRecordAdmin(object):
    list_display = ['code','telnum','send_type','status','send_time']
    search_fields = ['code','telnum','status','send_type']
    list_filter = ['code','telnum','send_type','status','send_time']

class BannerAdmin(object):

    list_display = ['title','image','url','detail','add_time']
    search_fields = ['title','image','url','detail']
    list_filter = ['title','image','url','detail','add_time']

xadmin.site.register(TelNumVerifyRecord,TelNumVerifyRecordAdmin)
xadmin.site.register(Banner,BannerAdmin)
xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSettings)