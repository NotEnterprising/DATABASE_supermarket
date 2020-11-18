from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.forms import widgets, forms
from django.urls import reverse_lazy

from .models import Customer


class CustomerListView(ListView):
    model = Customer
    context_object_name = 'Customer_list'
    template_name = "Customer/Customer_list.html"


class CustomerDetailView(DetailView):
    model = Customer
    template_name = "Customer/Customer_detail.html"
    context_object_name = 'Customer'


class CustomerCreateView(SuccessMessageMixin, CreateView):
    model = Customer
    fields = '__all__'
    success_message = '新员工添加成功'

    def get_form(self):
        '''add date picker in forms'''
        form = super(CustomerCreateView, self).get_form()
        form.fields['address'].widget = widgets.Textarea(attrs={'rows': 1})
        return form


class CustomerUpdateView(SuccessMessageMixin, UpdateView):
    model = Customer
    fields = '__all__'
    success_message = "员工信息修改成功."

    def get_form(self):
        '''add date picker in forms'''
        form = super(CustomerUpdateView, self).get_form()
        form.fields['address'].widget = widgets.Textarea(attrs={'rows': 1})
        return form


class CustomerDeleteView(DeleteView):
    model = Customer
    success_url = reverse_lazy('Customer-list')
