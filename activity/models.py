from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.utils import timezone

from django.db import models
from django.urls import reverse


class Activity(models.Model):
    name = models.CharField(max_length=200, verbose_name='活动名称')

    start_date = models.DateField(default=timezone.now, verbose_name='活动起始时间')
    end_date = models.DateField(default=timezone.now, verbose_name='活动结束时间')

    comment = models.CharField(max_length=200, verbose_name='活动描述')

    def __str__(self):
        return self.name

    def clean(self):
        super().clean()
        if not (self.start_date <= self.end_date):
            raise ValidationError('活动结束时间先于活动起始时间')
