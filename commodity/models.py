from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator

from category.models import Category


class Commodity(models.Model):
    name = models.CharField(max_length=200, verbose_name='商品名称')

    price = models.FloatField(default=0, verbose_name='商品价格', validators=[MinValueValidator(0)])

    production_date = models.DateField(default=timezone.now, verbose_name='生产日期')

    count = models.IntegerField(default=1, verbose_name='商品数量', validators=[MinValueValidator(1)])

    category = models.ForeignKey(Category, verbose_name='所属品类', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('commodity-detail', kwargs={'pk': self.pk})
