# _*_ coding:utf-8 _*_
from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser
from company.models import CompanyName
from basics.models import CityDict, TypeEnterprise, ProjectType, ProductType
from company.models import KehuUsers, CompanyName


# Create your models here.

class Record(models.Model):
    kehu_name = models.ForeignKey(KehuUsers, on_delete=models.DO_NOTHING, verbose_name=u"客户名称")
    # kehu_name = models.CharField(max_length=20, verbose_name=u"客户名称")
    project_name = models.CharField(max_length=50, verbose_name=u"项目名称")
    pt_type = models.ForeignKey(ProjectType, on_delete=models.DO_NOTHING, verbose_name=u"项目类型")
    pt_department = models.CharField(max_length=50, verbose_name=u"项目归属部门")
    bs_situation = models.TextField(verbose_name=u"基本情况")
    Decision_maker = models.CharField(max_length=20, verbose_name=u"项目决策人")
    cj_time = models.DateField(default=datetime.now, verbose_name=u"预计成交时间")
    xy_support = models.TextField(verbose_name=u"需要的支持")
    companyname = models.ForeignKey(CompanyName, on_delete=models.DO_NOTHING, verbose_name=u"公司名称")
    address = models.CharField(max_length=100, null=True, blank=True, verbose_name=u'公司地址')
    bb_people = models.CharField(max_length=20, verbose_name=u"报备人")
    mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name=u"报备人电话")
    bb_time = models.DateTimeField(default=datetime.now, verbose_name=u"报备时间")
    bb_state = models.CharField(default='xzxm', max_length=20, choices=(('xzxm',u'新增项目'), ('xmjxz',u'项目进行中'),
                                                                        ('xmyzz',u'项目已终止'),('zcbbz',u'再次报备中')),
                                verbose_name=u'报备状态')


    class Meta:
        verbose_name = u"项目报备系统"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.project_name


class ProjectProgress(models.Model):
    record = models.ForeignKey(Record, on_delete=models.DO_NOTHING, verbose_name=u"项目名称")
    pp_spead = models.TextField(verbose_name=u"项目进度描述")
    new_time = models.DateTimeField(default=datetime.now, verbose_name=u"最新更新时间")

    class Meta:
        verbose_name = u"项目进度"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.pp_spead