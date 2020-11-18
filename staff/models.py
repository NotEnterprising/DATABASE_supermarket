from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.core.validators import RegexValidator


class Staff(models.Model):
    GENDER = [
        ('male', '男'),
        ('female', '女')
    ]

    name = models.CharField(max_length=200, verbose_name='姓名')
    gender = models.CharField(max_length=10, choices=GENDER, default='男', verbose_name='性别')
    entry_date = models.DateField(default=timezone.now,verbose_name='入职日期')

    username = models.CharField(max_length=200,verbose_name='用户名')
    password = models.CharField(max_length=200,verbose_name='密码')

    mobile_num_regex = RegexValidator(regex="^[0-9]{11,8}$", message="输入的电话号码格式不对")
    mobile_number = models.CharField(validators=[mobile_num_regex], max_length=13, blank=True,verbose_name='电话号码')

    address = models.TextField(blank=True,verbose_name='地址')

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('staff-detail', kwargs={'pk': self.pk})
