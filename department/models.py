from django.core.validators import RegexValidator
from django.utils import timezone

from django.db import models
from django.urls import reverse

from supermarket.models import Supermarket


class Department(models.Model):
    name = models.CharField(max_length=200, verbose_name='部门名称')

    supermarket = models.ForeignKey(Supermarket, verbose_name='所属超市', on_delete=models.CASCADE)
    mobile_num_regex = RegexValidator(regex="^[0-9]{8,11}$", message="输入的电话号码格式不对")
    mobile_number = models.CharField(validators=[mobile_num_regex], max_length=13, blank=True, verbose_name='电话号码')

    comment = models.CharField(max_length=200, verbose_name='部门描述')

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('department-detail', kwargs={'pk': self.pk})
