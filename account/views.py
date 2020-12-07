from django.shortcuts import render, HttpResponse, get_object_or_404, redirect

from admin.models import User
from customer.models import Customer
from .forms import RegistrationForm, LoginForm, CustomerRegisterForm
from django.http import HttpResponseRedirect
from django.contrib import auth, messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.forms import widgets, forms


def register(request):
    if request.method == 'POST':
        form = CustomerRegisterForm(request.POST)
        if form.is_valid():
            if User.objects.get(username=form.cleaned_data['用户名']) is not None:
                messages.warning(request, '用户名已存在')
                form.fields['address'].widget = widgets.Textarea(attrs={'rows': 1})
                return render(request, 'admin/admin_form.html', context={'form': form})
            user = User.objects.create_user(username=form.cleaned_data['用户名'], password=form.cleaned_data['password1'],
                                            is_customer=True)

            customer = Customer.objects.create(name=form.cleaned_data['name'], gender=form.cleaned_data['gender'],
                                               mobile_number=form.cleaned_data['mobile_number'], user_id=user.id)
            customer.save()
            return HttpResponseRedirect("/accounts/login/")
        form.fields['address'].widget = widgets.Textarea(attrs={'rows': 1})
    else:
        form = CustomerRegisterForm()
    return render(request, 'registration/registration.html', context={'form': form})


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                return redirect('home')
            else:
                return render(request, 'registration/login.html',
                              {'form': form, 'message': '输入密码不对请重新尝试'})
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})


@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/accounts/login/")
