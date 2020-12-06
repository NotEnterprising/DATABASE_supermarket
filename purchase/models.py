from django.core.validators import MinValueValidator
from django.db import models

from commodity.models import Commodity
from customer.models import Customer


class Purchase(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    commodity = models.ForeignKey(Commodity, on_delete=models.CASCADE)
    num = models.IntegerField(validators=[MinValueValidator(0)], default=0)

    class Meta:
        ordering = ['customer']

    def __str__(self):
        return f'{self.customer} {self.commodity}'
