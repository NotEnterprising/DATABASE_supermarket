from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.forms import widgets, forms
from django.urls import reverse_lazy

from .models import Warehouse


class WarehouseListView(LoginRequiredMixin, ListView):
    model = Warehouse
    context_object_name = 'warehouse_list'
    template_name = "warehouse/warehouse_list.html"


class WarehouseDetailView(LoginRequiredMixin, DetailView):
    model = Warehouse
    template_name = "warehouse/warehouse_detail.html"
    context_object_name = 'warehouse'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        warehouse = Warehouse.objects.get(id=self.kwargs['pk'])
        commoditys = warehouse.commodity_set.all()
        context['commoditys'] = commoditys
        return context


class WarehouseCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Warehouse
    fields = '__all__'
    success_message = '新仓库添加成功'

    def get_form(self):
        '''add date picker in forms'''
        form = super(WarehouseCreateView, self).get_form()
        form.fields['address'].widget = widgets.Textarea(attrs={'rows': 1})
        return form

    def get(self, request, *args, **kwargs):
        if request.user.is_customer or request.user.is_staff:
            return redirect('warehouse-list')
        return super(WarehouseCreateView, self).get(self, request, *args, **kwargs)


class WarehouseUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Warehouse
    fields = '__all__'
    success_message = "仓库信息修改成功."

    def get_form(self):
        '''add date picker in forms'''
        form = super(WarehouseUpdateView, self).get_form()
        form.fields['address'].widget = widgets.Textarea(attrs={'rows': 1})
        return form

    def get(self, request, *args, **kwargs):
        if request.user.is_customer or request.user.is_staff:
            return redirect('warehouse-list')
        return super(WarehouseUpdateView, self).get(self, request, *args, **kwargs)


class WarehouseDeleteView(LoginRequiredMixin, DeleteView):
    model = Warehouse
    success_url = reverse_lazy('warehouse-list')

    def get(self, request, *args, **kwargs):
        if request.user.is_customer or request.user.is_staff:
            return redirect('warehouse-list')
        return super(WarehouseDeleteView, self).get(self, request, *args, **kwargs)
