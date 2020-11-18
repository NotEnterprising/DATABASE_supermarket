from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.forms import widgets, forms
from django.urls import reverse_lazy

from .models import Admin


class AdminListView(ListView):
    model = Admin
    context_object_name = 'admin_list'
    template_name = "admin/admin_list.html"


class AdminDetailView(DetailView):
    model = Admin
    template_name = "admin/admin_detail.html"
    context_object_name = 'admin'


class AdminCreateView(SuccessMessageMixin, CreateView):
    model = Admin
    fields = '__all__'
    success_message = '新管理员添加成功'

    def get_form(self):
        '''add date picker in forms'''
        form = super(AdminCreateView, self).get_form()
        form.fields['address'].widget = widgets.Textarea(attrs={'rows': 1})
        return form


class AdminUpdateView(SuccessMessageMixin, UpdateView):
    model = Admin
    fields = '__all__'
    success_message = "管理员信息修改成功."

    def get_form(self):
        '''add date picker in forms'''
        form = super(AdminUpdateView, self).get_form()
        form.fields['address'].widget = widgets.Textarea(attrs={'rows': 1})
        return form


class AdminDeleteView(DeleteView):
    model = Admin
    success_url = reverse_lazy('admin-list')
