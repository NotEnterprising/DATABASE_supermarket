from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from django.core.validators import RegexValidator
from django.utils import timezone


class Supermarket(models.Model):

    name = models.CharField(max_length=200, verbose_name='超市名称')

    start_time = models.TimeField(default=timezone.now, verbose_name='起始营业时间')
    end_time = models.TimeField(default=timezone.now, verbose_name='结束营业时间')

    mobile_num_regex = RegexValidator(regex="^[0-9]{8,11}$", message="输入的电话号码格式不对")
    mobile_number = models.CharField(validators=[mobile_num_regex], max_length=13, blank=True, verbose_name='电话号码')

    address = models.TextField(blank=True, verbose_name='超市地址')

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('supermarket-detail', kwargs={'pk': self.pk})

    def clean(self):
        super().clean()
        if not (self.start_time <= self.end_time):
            raise ValidationError('结束营业时间先于起始营业时间')
