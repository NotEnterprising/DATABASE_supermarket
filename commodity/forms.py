from django import forms
from django.forms import ModelForm, modelformset_factory

from .models import Commodity


class CommodityForm(ModelForm):
    class Meta:
        model = Commodity
        fields = '__all__'
