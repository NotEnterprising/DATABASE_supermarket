from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.core.validators import RegexValidator


class Staff(models.Model):
    GENDER = [
        ('male', '男'),
        ('female', '女')
    ]

    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=10, choices=GENDER, default='男')
    entry_date = models.DateField(default=timezone.now)

    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    mobile_num_regex = RegexValidator(regex="^[0-9]{11,8}$", message="输入的电话号码格式不对")
    mobile_number = models.CharField(validators=[mobile_num_regex], max_length=13, blank=True)

    address = models.TextField(blank=True)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('staff-detail', kwargs={'pk': self.pk})
