from django import forms
from django.forms import ModelForm, modelformset_factory

from .models import Category


class CategoryForm(ModelForm):
    prefix = 'Category'

    class Meta:
        model = Category
        fields = ['name', 'area']

