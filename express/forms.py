from django import forms
from django.forms import ModelForm, modelformset_factory
from .models import Express


class ExpressForm(ModelForm):
    prefix = 'Express'

    class Meta:
        model = Express
        fields = ['name', 'mobile_number', 'address', 'comment']
