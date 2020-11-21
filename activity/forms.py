from django import forms
from django.forms import ModelForm, modelformset_factory
from .models import Activity


class ActivityForm(ModelForm):
    prefix = 'Activity'

    class Meta:
        model = Activity
        fields = ['name', 'comment']
