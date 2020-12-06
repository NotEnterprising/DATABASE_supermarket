from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, modelformset_factory

from .models import User, Customer


class CustomerRegisterForm(UserCreationForm):
    用户名 = forms.CharField(max_length=200,

                          error_messages={

                              'max_length': '长度不超过20',

                              'required': '用户名不能为空'

                          })

    class Meta(UserCreationForm.Meta):
        model = Customer
        fields = ['name', 'gender', 'vip_level', 'balance', 'mobile_number', 'address', '用户名']
