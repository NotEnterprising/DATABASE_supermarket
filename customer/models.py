from django.db import models
from django.urls import reverse
from django.core.validators import RegexValidator
from school_app.settings import hash_code


class Customer(models.Model):
    GENDER = [
        ('male', '男'),
        ('female', '女')
    ]

    name = models.CharField(max_length=200, verbose_name='用户昵称')
    gender = models.CharField(max_length=10, choices=GENDER, default='男', verbose_name='性别')

    balance = models.IntegerField(verbose_name='余额', default=0)

    username = models.CharField(max_length=200, verbose_name='用户名')
    password = models.CharField(max_length=200, verbose_name='密码')

    mobile_num_regex = RegexValidator(regex="^[0-9]{8,11}$", message="输入的电话号码格式不对")
    mobile_number = models.CharField(validators=[mobile_num_regex], max_length=13, blank=True, verbose_name='电话号码')

    address = models.TextField(blank=True, verbose_name='住址')

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('staff-detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        self.password = hash_code(self.password)
        super().save(*args, **kwargs)
