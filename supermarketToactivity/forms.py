from django import forms
from django.forms import modelformset_factory

from supermarket.models import Supermarket
from activity.models import Activity

from .models import SupermarketToActivity


class CreateSupermarketToActivity(forms.Form):
    activity = forms.ModelChoiceField(queryset=Activity.objects.all())


EditSupermarketToActivity = modelformset_factory(SupermarketToActivity, fields=(), extra=0, can_delete=True)
