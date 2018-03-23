# -*- coding: utf-8 -*-
__author__ = 'wangruiyy'
__date__ = '2018/3/20 上午10:16'

import xadmin
from xadmin import views
from .models import Record, ProjectProgress


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True

class GlobalSettings(object):
    site_title = "在线报备管理系统"
    site_footer = '公司内部系统'
    menu_style = 'accordion'

class RecordAdmin(object):
    list_display = ['kehu_name', 'project_name', 'pt_department', 'Decision_maker', 'cj_time', 'companyname',
                    'bb_people', 'bb_state', 'bb_time']
    search_fidlds = ['kehu_name', 'project_name', 'companyname', 'bb_people', 'mobile']
    list_filter = ['kehu_name', 'project_name', 'companyname', 'bb_people']

class ProjectProgressAdmin(object):
    list_display = ['record', 'pp_spead', 'new_time']
    search_fidlds = ['record']
    list_filter = ['record', 'new_time']

xadmin.site.register(Record, RecordAdmin)
xadmin.site.register(ProjectProgress, ProjectProgressAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)