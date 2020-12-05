from django import forms
from django.forms import modelformset_factory

from supermarket.models import Supermarket
from express.models import Express

from .models import SupermarketToExpress


class CreateSupermarketToExpress(forms.Form):
    express = forms.ModelChoiceField(queryset=Express.objects.all())


EditSupermarketToExpress = modelformset_factory(SupermarketToExpress, fields=(), extra=0, can_delete=True)
