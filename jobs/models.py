from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

JobTypes = [
    (0, "运营类"),
    (1, "技术类"),
    (2, "设计类")
]

Cities = [
    (0, '北京'),
    (1, '上海'),
    (2, '广州')
]
class Job(models.Model):
    job_type = models.SmallIntegerField(blank=False, choices=JobTypes, verbose_name='职位类型')
    job_name = models.CharField(max_length=200)
    job_city = models.SmallIntegerField(blank=False, choices=Cities, verbose_name='地点')
    job_responsibility = models.TextField(max_length=1024, verbose_name='职位描述')
    job_requirements = models.TextField(max_length=1024, verbose_name='职位要求')
    creator = models.ForeignKey(User, verbose_name='创建人', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(verbose_name='创建时间',default=datetime.datetime.now)
    modified_at = models.DateTimeField(verbose_name='修改时间', default=datetime.datetime.now)
