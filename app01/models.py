from django.db import models

# 导入ContentType表
from django.contrib.contenttypes.models import ContentType

from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation

class Course(models.Model):
    title = models.CharField(max_length=32)
    # 数据库不生成,只用于连表查询(反向查询)
    policy_list = GenericRelation('Pricepolicy')

class DegreeCourse(models.Model):
    title = models.CharField(max_length=32)
    # 数据库不生成,只用于连表查询(反向查询)
    policy_list = GenericRelation('Pricepolicy')

class Pricepolicy(models.Model):
    # 关联django_content_type表, 注意: 不能用to=""关联, content_type不要用驼峰体命名
    content_type = models.ForeignKey(ContentType)
    # 数据id(不是外键,只是一个数字)
    object_id = models.PositiveIntegerField()

    # 数据库不生成,只用于帮助数据操作
    content_object = GenericForeignKey('content_type', 'object_id')
    period = models.CharField(max_length=16)
    price = models.FloatField()















