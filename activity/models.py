from django.utils import timezone

from django.db import models
from django.urls import reverse


class Activity(models.Model):
    name = models.CharField(max_length=200, verbose_name='活动名称')

    start_time = models.DateField(default=timezone.now, verbose_name='活动起始时间')
    end_time = models.DateField(default=timezone.now, verbose_name='活动结束时间')

    comment = models.CharField(max_length=200, verbose_name='活动描述')

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('activity-detail', kwargs={'pk': self.pk})