from django.utils import timezone

from django.db import models
from django.urls import reverse


class Department(models.Model):
    name = models.CharField(max_length=200, verbose_name='部门名称')

    staff_num = models.IntegerField(default=0, verbose_name='部门人数')

    comment = models.CharField(max_length=200, verbose_name='部门描述')

    def __str__(self):
        return f'{self.name}'
