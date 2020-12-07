from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.forms import widgets
from django.urls import reverse_lazy

from .forms import ExpressForm
from .models import Express


class ExpressListView(LoginRequiredMixin, ListView):
    model = Express
    context_object_name = 'express_list'
    template_name = "express/express_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ExpressForm()
        return context


class ExpressCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = ExpressForm
    template_name = 'express/mgt_form.html'
    success_message = '新物流添加成功'
    success_url = reverse_lazy('express-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ExpressForm()
        return context

    def get(self, request, *args, **kwargs):
        if request.user.is_customer or request.user.is_staff:
            return redirect('express-list')
        return super(ExpressCreateView, self).get(self, request, *args, **kwargs)


class ExpressUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Express
    fields = '__all__'
    template_name = 'express/mgt_form.html'
    success_message = "物流信息修改成功."
    success_url = reverse_lazy('express-list')

    def get_form(self):
        '''add date picker in forms'''
        form = super(ExpressUpdateView, self).get_form()
        form.fields['address'].widget = widgets.Textarea(attrs={'rows': 1})
        return form

    def get(self, request, *args, **kwargs):
        if request.user.is_customer or request.user.is_staff:
            return redirect('express-list')
        return super(ExpressUpdateView, self).get(self, request, *args, **kwargs)


class ExpressDeleteView(LoginRequiredMixin, DeleteView):
    model = Express
    success_url = reverse_lazy('express-list')
    template_name = 'express/core_confirm_delete.html'
    success_message = "物流信息删除成功"

    def get(self, request, *args, **kwargs):
        if request.user.is_customer or request.user.is_staff:
            return redirect('express-list')
        return super(ExpressDeleteView, self).get(self, request, *args, **kwargs)
