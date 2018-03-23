# _*_ coding:utf-8 _*_
from django.db import models
from datetime import datetime
from basics.models import CityDict, TypeEnterprise, ProjectType, ProductType

# Create your models here.

class KehuUsers(models.Model):
    kehu_name = models.CharField(max_length=50, verbose_name=u"客户名称")
    Decision_maker = models.CharField(max_length=20, verbose_name=u"项目决策人")
    tel = models.CharField(max_length=11, blank=True, null=True, verbose_name=u"电话号码")
    desc = models.TextField(verbose_name=u"客户项目记录")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"客户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.kehu_name




class CompanyName(models.Model):
    name = models.CharField(max_length=50, verbose_name=u"公司名称")
    typeenterprise = models.ForeignKey(TypeEnterprise, on_delete=models.DO_NOTHING, verbose_name=u"企业类型")
    address = models.CharField(max_length=100, verbose_name=u'公司地址')
    post_code = models.CharField(null=True, blank=True, max_length=10, verbose_name=u"邮政编码")
    net_add = models.CharField(null=True, blank=True, max_length=100, verbose_name=u"公司网址")
    shengfen = models.CharField(max_length=10, verbose_name=u"省份")
    # city = models.CharField(max_length=20, verbose_name=u"城市")
    city = models.ForeignKey(CityDict, on_delete=models.DO_NOTHING, verbose_name=u"所在城市")
    cl_data = models.DateField(verbose_name=u"公司注册时间")
    yyzz_zch = models.CharField(max_length=20, verbose_name=u"营业执照注册号")
    general_manager = models.CharField(max_length=10, verbose_name=u"总经理")
    tel = models.CharField(max_length=11, verbose_name=u"总经理联系方式")
    email = models.EmailField(null=True, blank=True,verbose_name=u"邮件地址")
    tech_manager = models.CharField(null=True, blank=True, max_length=10, verbose_name=u"技术经理")
    tech_tel = models.CharField(null=True, blank=True, max_length=11, verbose_name=u"技术经理联系方式")
    tech_email = models.EmailField(null=True, blank=True, verbose_name=u"技术经理邮件地址")
    mt_manager = models.CharField(null=True, blank=True, max_length=10,verbose_name=u"市场经理")
    mt_tel = models.CharField(null=True, blank=True, max_length=11, verbose_name=u"市场经理联系方式")
    mt_email = models.EmailField(null=True, blank=True, verbose_name=u"市场经理邮件地址")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"合作企业信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name



