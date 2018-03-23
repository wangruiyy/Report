# _*_ coding:utf-8 _*_
from django.db import models
from datetime import datetime

# Create your models here.

class CityDict(models.Model):
    name = models.CharField(max_length=20, verbose_name=u"城市")
    desc = models.CharField(max_length=200, verbose_name=u"描述")
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = u"城市"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class TypeEnterprise(models.Model):
    enterprise = models.CharField(max_length=20, verbose_name=u"企业类型")
    desc = models.CharField(max_length=100, verbose_name=u"描述")
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = u"企业类型"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.enterprise


class ProjectType(models.Model):
    pt_type = models.CharField(max_length=20, verbose_name=u"项目类型")
    pt_desc = models.CharField(max_length=100, verbose_name=u"项目类型描述")
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = u"项目类型"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.pt_type


class ProductType(models.Model):
    pr_type = models.CharField(max_length=20, verbose_name=u"产品类型")
    pr_desc = models.CharField(max_length=100, verbose_name=u"产品类型描述")
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = u"产品类型"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.pr_type


class Credits(models.Model):
    credit_type = models.CharField(max_length=20, verbose_name=u"信用类型")
    credit_desc = models.CharField(max_length=100, verbose_name=u"信用类型描述")
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = u"信用类型"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.credit_type