from django.db import models

from supermarket.models import Supermarket
from activity.models import Activity


class SupermarketToActivity(models.Model):
    supermarket = models.ForeignKey(Supermarket, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)

    class Meta:
        ordering = ['supermarket']

    def __str__(self):
        return f'{self.supermarket} {self.activity}'
