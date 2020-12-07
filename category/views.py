from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.forms import widgets, forms
from django.urls import reverse_lazy

from .forms import CategoryForm
from .models import Category


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    template_name = "category/category_list.html"

    def get_context_data(self, **kwargs):
        categorys = Category.objects.all()

        bulk = {}
        for category in categorys:
            bulk[category.id] = {
                "category": category,
                "commodityCount": category.commodity_set.all().count()
            }

        context = {
            "categorys": bulk
        }
        return context


class CategoryDetailView(LoginRequiredMixin, DetailView):
    model = Category
    template_name = "category/category_detail.html"
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = Category.objects.get(id=self.kwargs['pk'])
        commoditys = category.commodity_set.all()
        num = category.commodity_set.all().count()
        context['commoditys'] = commoditys
        context['num'] = num
        return context


class CategoryCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = CategoryForm
    template_name = "category/category_form.html"
    success_message = '新品类添加成功'
    success_url = reverse_lazy('category-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CategoryForm()
        return context

    def get(self, request, *args, **kwargs):
        if request.user.is_customer:
            return redirect('home')
        return super(CategoryCreateView, self).get(self, request, *args, **kwargs)

class CategoryUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Category
    fields = '__all__'
    template_name = "category/category_form.html"
    success_message = "品类信息修改成功."
    success_url = reverse_lazy('category-list')

    def get_form(self):
        '''add date picker in forms'''
        form = super(CategoryUpdateView, self).get_form()
        return form

    def get(self, request, *args, **kwargs):
        if request.user.is_customer:
            return redirect('home')
        return super(CategoryUpdateView, self).get(self, request, *args, **kwargs)


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    success_url = reverse_lazy('category-list')

    def get(self, request, *args, **kwargs):
        if request.user.is_customer:
            return redirect('home')
        return super(CategoryDeleteView, self).get(self, request, *args, **kwargs)