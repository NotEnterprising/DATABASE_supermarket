from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.forms import widgets, forms
from django.urls import reverse_lazy
from .models import Commodity


class CommodityListView(LoginRequiredMixin, ListView):
    model = Commodity
    context_object_name = 'commodity_list'
    template_name = "commodity/commodity_list.html"


class CommodityDetailView(LoginRequiredMixin, DetailView):
    model = Commodity
    template_name = "commodity/commodity_detail.html"
    context_object_name = 'commodity'


class CommodityCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Commodity
    fields = '__all__'
    success_message = '新商品添加成功'

    def get_form(self):
        '''add date picker in forms'''
        form = super(CommodityCreateView, self).get_form()
        form.fields['production_date'].widget = widgets.DateInput(
            attrs={'type': 'date'})
        return form


class CommodityUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Commodity
    fields = '__all__'
    success_message = "商品信息修改成功."

    def get_form(self):
        '''add date picker in forms'''
        form = super(CommodityUpdateView, self).get_form()
        form.fields['production_date'].widget = widgets.DateInput(
            attrs={'type': 'date'})
        return form


class CommodityDeleteView(LoginRequiredMixin, DeleteView):
    model = Commodity
    success_url = reverse_lazy('commodity-list')
