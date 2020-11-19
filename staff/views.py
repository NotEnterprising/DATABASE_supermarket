from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.forms import widgets, forms
from django.urls import reverse_lazy

from .models import Staff


class StaffListView(LoginRequiredMixin, ListView):
    model = Staff
    context_object_name = 'staff_list'
    template_name = "staff/staff_list.html"


class StaffDetailView(LoginRequiredMixin, DetailView):
    model = Staff
    template_name = "staff/staff_detail.html"
    context_object_name = 'staff'


class StaffCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Staff
    fields = '__all__'
    success_message = '新员工添加成功'

    def get_form(self):
        '''add date picker in forms'''
        form = super(StaffCreateView, self).get_form()
        form.fields['entry_date'].widget = widgets.DateInput(
            attrs={'type': 'date'})
        form.fields['address'].widget = widgets.Textarea(attrs={'rows': 1})
        return form


class StaffUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Staff
    fields = '__all__'
    success_message = "员工信息修改成功."

    def get_form(self):
        '''add date picker in forms'''
        form = super(StaffUpdateView, self).get_form()
        form.fields['entry_date'].widget = widgets.DateInput(
            attrs={'type': 'date'})
        form.fields['address'].widget = widgets.Textarea(attrs={'rows': 1})
        return form


class StaffDeleteView(LoginRequiredMixin, DeleteView):
    model = Staff
    success_url = reverse_lazy('staff-list')
