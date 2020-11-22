
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
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


class WarehouseCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Warehouse
    fields = '__all__'
    success_message = '新仓库添加成功'

    def get_form(self):
        '''add date picker in forms'''
        form = super(WarehouseCreateView, self).get_form()
        form.fields['address'].widget = widgets.Textarea(attrs={'rows': 1})
        return form


class WarehouseUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Warehouse
    fields = '__all__'
    success_message = "仓库信息修改成功."

    def get_form(self):
        '''add date picker in forms'''
        form = super(WarehouseUpdateView, self).get_form()
        form.fields['address'].widget = widgets.Textarea(attrs={'rows': 1})
        return form


class WarehouseDeleteView(LoginRequiredMixin, DeleteView):
    model = Warehouse
    success_url = reverse_lazy('warehouse-list')
