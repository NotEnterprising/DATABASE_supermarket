from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.forms import widgets, forms
from django.urls import reverse_lazy

from admin.models import User
from .forms import CustomerRegisterForm
from .models import Customer


class CustomerListView(LoginRequiredMixin, ListView):
    model = Customer
    context_object_name = 'customer_list'
    template_name = "customer/customer_list.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_customer:
            return redirect('home')
        return super(CustomerListView, self).get(self, request, *args, **kwargs)


class CustomerDetailView(LoginRequiredMixin, DetailView):
    model = Customer
    template_name = "customer/customer_detail.html"
    context_object_name = 'customer'

    def get(self, request, *args, **kwargs):
        if request.user.is_customer:
            return redirect('home')
        return super(CustomerDetailView, self).get(self, request, *args, **kwargs)


@login_required()
def register(request):
    if request.user.is_customer:
        return redirect('home')
    elif request.user.is_staff:
        return redirect('customer-list')
    if request.method == 'POST':
        form = CustomerRegisterForm(request.POST)
        if form.is_valid():
            a = None
            try:
                a = User.objects.get(username=form.cleaned_data['用户名'])
            except:
                pass
            if a is not None:
                messages.warning(request, '用户名已存在')
                form.fields['address'].widget = widgets.Textarea(attrs={'rows': 1})
                return render(request, 'admin/admin_form.html', context={'form': form})
            user = User.objects.create_user(username=form.cleaned_data['用户名'], password=form.cleaned_data['password1'],
                                            is_customer=True)

            customer = Customer.objects.create(name=form.cleaned_data['name'], gender=form.cleaned_data['gender'],
                                               mobile_number=form.cleaned_data['mobile_number'],
                                               address=form.cleaned_data['address'],
                                               vip_level=form.cleaned_data['vip_level'],
                                               balance=form.cleaned_data['balance'], user_id=user.id)
            customer.save()
            messages.success(request, '新顾客添加成功')
            return redirect('customer-list')
        form.fields['address'].widget = widgets.Textarea(attrs={'rows': 1})
    else:
        form = CustomerRegisterForm()
        form.fields['address'].widget = widgets.Textarea(attrs={'rows': 1})
    flag = True
    return render(request, 'customer/customer_form.html', context={'form': form, "flag": flag})


class CustomerUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Customer
    fields = '__all__'
    success_message = "顾客信息修改成功."
    form_class = CustomerRegisterForm

    def get_form(self):
        '''add date picker in forms'''
        form = super(CustomerUpdateView, self).get_form()
        form.fields['address'].widget = widgets.Textarea(attrs={'rows': 1})
        return form

    def post(self, request, *args, **kwargs):
        form = CustomerRegisterForm(request.POST)
        if form.is_valid():
            customer = Customer.objects.get(user_id=self.kwargs['pk'])
            user = User.objects.get(id=self.kwargs['pk'])
            customer.name = request.POST.get('name')
            customer.gender = request.POST.get('gender')
            customer.mobile_number = request.POST.get('mobile_number')
            customer.address = request.POST.get('address')
            customer.vip_level = request.POST.get('vip_level')
            customer.balance = request.POST.get('balance')
            customer.save()
            user.username = request.POST.get('用户名')
            user.set_password(request.POST.get('password1'))
            user.save()
            return redirect('customer-list')
        form.fields['address'].widget = widgets.Textarea(attrs={'rows': 1})
        return render(request, 'customer/customer_form.html', context={'form': form})

    def get(self, request, *args, **kwargs):
        if request.user.is_customer:
            return redirect('home')
        elif request.user.is_staff:
            return redirect('customer-list')
        customer = Customer.objects.get(user_id=self.kwargs['pk'])
        user = User.objects.get(id=self.kwargs['pk'])
        form = self.form_class(instance=customer)
        form.fields['address'].widget = widgets.Textarea(attrs={'rows': 1})
        flag = False
        return render(request, 'customer/customer_form.html', {'form': form, "flag": flag})


class CustomerDeleteView(LoginRequiredMixin, DeleteView):
    model = Customer
    success_url = reverse_lazy('customer-list')

    def post(self, request, *args, **kwargs):
        customer = Customer.objects.get(user_id=self.kwargs['pk'])
        temp = customer.user
        customer.delete()
        temp.delete()
        return redirect('customer-list')

    def get(self, request, *args, **kwargs):
        if request.user.is_customer:
            return redirect('home')
        elif request.user.is_staff:
            return redirect('customer-list')
        return super(CustomerDeleteView, self).get(self, request, *args, **kwargs)
