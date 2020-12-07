from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        supplier = Supplier.objects.get(id=self.kwargs['pk'])
        commoditys = supplier.commodity_set.all()
        context['commoditys'] = commoditys
        return context


class SupplierCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Supplier
    fields = '__all__'
    success_message = '新供货商添加成功'

    def get_form(self):
        '''add date picker in forms'''
        form = super(SupplierCreateView, self).get_form()
        form.fields['address'].widget = widgets.Textarea(attrs={'rows': 1})
        return form

    def get(self, request, *args, **kwargs):
        if request.user.is_customer or request.user.is_staff:
            return redirect('supplier-list')
        return super(SupplierCreateView, self).get(self, request, *args, **kwargs)


class SupplierUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Supplier
    fields = '__all__'
    success_message = "供货商信息修改成功."

    def get_form(self):
        '''add date picker in forms'''
        form = super(SupplierUpdateView, self).get_form()
        form.fields['address'].widget = widgets.Textarea(attrs={'rows': 1})
        return form

    def get(self, request, *args, **kwargs):
        if request.user.is_customer or request.user.is_staff:
            return redirect('supplier-list')
        return super(SupplierUpdateView, self).get(self, request, *args, **kwargs)


class SupplierDeleteView(LoginRequiredMixin, DeleteView):
    model = Supplier
    success_url = reverse_lazy('supplier-list')

    def get(self, request, *args, **kwargs):
        if request.user.is_customer or request.user.is_staff:
            return redirect('supplier-list')
        return super(SupplierDeleteView, self).get(self, request, *args, **kwargs)
