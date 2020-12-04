from django.core.validators import MinValueValidator
from django.utils import timezone

from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='品类名称')

    commodityCount = models.IntegerField(default=0, verbose_name='商品数量', validators=[MinValueValidator(1)])

    area = models.CharField(max_length=200, verbose_name='区域')

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('category-detail', kwargs={'pk': self.pk})
