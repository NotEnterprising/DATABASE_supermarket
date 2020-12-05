from django.db import models

from supermarket.models import Supermarket
from express.models import Express


class SupermarketToExpress(models.Model):
    supermarket = models.ForeignKey(Supermarket, on_delete=models.CASCADE)
    express = models.ForeignKey(Express, on_delete=models.CASCADE)

    class Meta:
        ordering = ['supermarket']

    def __str__(self):
        return f'{self.supermarket} {self.express}'
