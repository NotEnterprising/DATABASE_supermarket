from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.forms import widgets, forms
from django.urls import reverse_lazy

from .forms import CategoryForm
from .models import Category


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    context_object_name = 'category_list'
    template_name = "category/category_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
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
        context['commoditys'] = commoditys
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


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    success_url = reverse_lazy('category-list')
