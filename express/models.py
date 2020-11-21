from django.db import models
from django.urls import reverse
from django.core.validators import RegexValidator


class Express(models.Model):
    name = models.CharField(max_length=200, verbose_name='物流名称')

    mobile_num_regex = RegexValidator(regex="^[0-9]{8,11}$", message="输入的电话号码格式不对")
    mobile_number = models.CharField(validators=[mobile_num_regex], max_length=13, blank=True, verbose_name='电话号码')

    address = models.CharField(max_length=200, blank=True, verbose_name='物流地址')

    comment = models.CharField(max_length=200, blank=True, verbose_name='物流描述')

    def __str__(self):
        return f'{self.name}'
