from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.forms import widgets, forms
from django.urls import reverse_lazy

from .models import Supermarket


class SupermarketListView(LoginRequiredMixin, ListView):
    model = Supermarket
    context_object_name = 'supermarket_list'
    template_name = "supermarket/supermarket_list.html"


class SupermarketDetailView(LoginRequiredMixin, DetailView):
    model = Supermarket
    template_name = "supermarket/supermarket_detail.html"
    context_object_name = 'supermarket'


class SupermarketCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Supermarket
    fields = '__all__'
    success_message = '新员工添加成功'

    def get_form(self):
        '''add date picker in forms'''
        form = super(SupermarketCreateView, self).get_form()
        form.fields['start_time'].widget = widgets.DateInput(
            attrs={'type': 'time'})
        form.fields['end_time'].widget = widgets.DateInput(
            attrs={'type': 'time'})
        form.fields['address'].widget = widgets.Textarea(attrs={'rows': 1})
        return form


class SupermarketUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Supermarket
    fields = '__all__'
    success_message = "员工信息修改成功."

    def get_form(self):
        '''add date picker in forms'''
        form = super(SupermarketUpdateView, self).get_form()
        form.fields['start_time'].widget = widgets.DateInput(
            attrs={'type': 'time'})
        form.fields['end_time'].widget = widgets.DateInput(
            attrs={'type': 'time'})
        form.fields['address'].widget = widgets.Textarea(attrs={'rows': 1})
        return form


class SupermarketDeleteView(LoginRequiredMixin, DeleteView):
    model = Supermarket
    success_url = reverse_lazy('supermarket-list')
