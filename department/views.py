from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Department
from .forms import DepartmentForm


class DepartmentListView(LoginRequiredMixin, SuccessMessageMixin, ListView):
    model = Department
    #template_name = 'corecode/department_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = DepartmentForm()
        return context


class DepartmentCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = DepartmentForm
    #template_name = 'corecode/mgt_form.html'
    success_url = reverse_lazy('department-list')
    success_message = '部门信息创建成功'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = DepartmentForm()
        return context


class DepartmentUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Department
    fields = ['name', 'current']
    success_url = reverse_lazy('department-list')
    success_message = '部门信息更新成功'
    #template_name = 'corecode/mgt_form.html'


class DepartmentDeleteView(LoginRequiredMixin, DeleteView):
    model = Department
    success_url = reverse_lazy('department-list')
    #template_name = 'corecode/core_confirm_delete.html'
    success_message = "部门信息删除成功"

