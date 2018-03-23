# -*- coding: utf-8 -*-
__author__ = 'wangruiyy'
__date__ = '2018/3/21 上午9:20'

import xadmin
from .models import CityDict, TypeEnterprise, ProjectType, ProductType, Credits


class CityDictAdmin(object):
    list_display = ['name', 'desc', 'add_time']


class TypeEnterpriseAdmin(object):
    list_display = ['enterprise', 'desc', 'add_time']


class ProjectTypeAdmin(object):
    list_display = ['pt_type', 'pt_desc', 'add_time']

class ProductTypeAdmin(object):
    list_display = ['pr_type', 'pr_desc', 'add_time']

class CreditsAdmin(object):
    list_display = ['credit_type', 'credit_desc', 'add_time']


xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(TypeEnterprise, TypeEnterpriseAdmin)
xadmin.site.register(ProjectType, ProjectTypeAdmin)
xadmin.site.register(ProductType, ProductTypeAdmin)
xadmin.site.register(Credits, CreditsAdmin)