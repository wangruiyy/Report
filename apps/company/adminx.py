# -*- coding: utf-8 -*-
__author__ = 'wangruiyy'
__date__ = '2018/3/21 上午9:20'

import xadmin

from .models import CompanyName, KehuUsers


class CompanyNameAdmin(object):
    list_display = ['name', 'address', 'post_code', 'shengfen', 'city', 'general_manager',
                    'tel']
    search_fidlds = ['name', 'shengfen', 'city', 'general_manager', 'tel']
    list_filter = ['name', 'shengfen', 'city', 'general_manager', 'tel']


class KehuUsersAdmin(object):
    list_display = ['kehu_name', 'Decision_maker', 'tel', 'add_time']






xadmin.site.register(CompanyName, CompanyNameAdmin)
xadmin.site.register(KehuUsers, KehuUsersAdmin)