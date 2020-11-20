from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.forms import widgets, forms
from django.urls import reverse_lazy

from .models import Category


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    context_object_name = 'category_list'
    template_name = "category/category_list.html"


class CategoryDetailView(LoginRequiredMixin, DetailView):
    model = Category
    template_name = "category/category_detail.html"
    context_object_name = 'category'


class CategoryCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Category
    fields = '__all__'
    success_message = '新品类添加成功'

    def get_form(self):
        '''add date picker in forms'''
        form = super(CategoryCreateView, self).get_form()
        return form


class CategoryUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Category
    fields = '__all__'
    success_message = "品类信息修改成功."

    def get_form(self):
        '''add date picker in forms'''
        form = super(CategoryUpdateView, self).get_form()
        return form


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    success_url = reverse_lazy('category-list')
