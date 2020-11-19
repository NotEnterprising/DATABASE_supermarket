from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.forms import widgets
from django.urls import reverse_lazy

from .models import Express


class ExpressListView(LoginRequiredMixin, ListView):
    model = Express
    context_object_name = 'express_list'
    template_name = "express/express_list.html"


class ExpressDetailView(LoginRequiredMixin, DetailView):
    model = Express
    template_name = "express/express_detail.html"
    context_object_name = 'express'


class ExpressCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Express
    fields = '__all__'
    success_message = '新员工添加成功'

    def get_form(self):
        '''add date picker in forms'''
        form = super(ExpressCreateView, self).get_form()
        form.fields['address'].widget = widgets.Textarea(attrs={'rows': 1})
        return form


class ExpressUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Express
    fields = '__all__'
    success_message = "员工信息修改成功."

    def get_form(self):
        '''add date picker in forms'''
        form = super(ExpressUpdateView, self).get_form()
        form.fields['address'].widget = widgets.Textarea(attrs={'rows': 1})
        return form


class ExpressDeleteView(LoginRequiredMixin, DeleteView):
    model = Express
    success_url = reverse_lazy('express-list')
