from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Category
from .forms import CategoryForm


class CategoryListView(LoginRequiredMixin, SuccessMessageMixin, ListView):
    model = Category
    #template_name = 'corecode/category_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CategoryForm()
        return context


class CategoryCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = CategoryForm
    #template_name = 'corecode/mgt_form.html'
    success_url = reverse_lazy('category-list')
    success_message = '品类信息创建成功'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CategoryForm()
        return context


class CategoryUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Category
    fields = ['name', 'current']
    success_url = reverse_lazy('category-list')
    success_message = '品类信息更新成功'
    #template_name = 'corecode/mgt_form.html'


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    success_url = reverse_lazy('category-list')
    #template_name = 'corecode/core_confirm_delete.html'
    success_message = "品类信息删除成功"

