from django import forms
from django.forms import modelformset_factory

from commodity.models import Commodity

from .models import Purchase


class CreatePurchase(forms.Form):
    commoditys = forms.ModelMultipleChoiceField(
        queryset=Commodity.objects.all(), widget=forms.CheckboxSelectMultiple)


EditPurchase = modelformset_factory(Purchase, fields=['num'], extra=0, can_delete=True)
