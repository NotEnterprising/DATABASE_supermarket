
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.forms import widgets, forms
from django.urls import reverse_lazy

from .models import Supplier


class SupplierListView(LoginRequiredMixin, ListView):
    model = Supplier
    context_object_name = 'supplier_list'
    template_name = "supplier/supplier_list.html"


class SupplierDetailView(LoginRequiredMixin, DetailView):
    model = Supplier
    template_name = "supplier/supplier_detail.html"
    context_object_name = 'supplier'


class SupplierCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Supplier
    fields = '__all__'
    success_message = '新供货商添加成功'

    def get_form(self):
        '''add date picker in forms'''
        form = super(SupplierCreateView, self).get_form()
        form.fields['address'].widget = widgets.Textarea(attrs={'rows': 1})
        return form


class SupplierUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Supplier
    fields = '__all__'
    success_message = "供货商信息修改成功."

    def get_form(self):
        '''add date picker in forms'''
        form = super(SupplierUpdateView, self).get_form()
        form.fields['address'].widget = widgets.Textarea(attrs={'rows': 1})
        return form


class SupplierDeleteView(LoginRequiredMixin, DeleteView):
    model = Supplier
    success_url = reverse_lazy('supplier-list')
