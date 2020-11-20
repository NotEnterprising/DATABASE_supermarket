from django import forms
from django.forms import ModelForm, modelformset_factory

from .models import Department


class DepartmentForm(ModelForm):
    prefix = 'Department'

    class Meta:
        model = Department
        fields = ['name', 'comment']



