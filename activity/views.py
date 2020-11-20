from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.forms import widgets
from django.urls import reverse_lazy

from .models import Activity


class ActivityListView(LoginRequiredMixin, ListView):
    model = Activity
    context_object_name = 'activity_list'
    template_name = "activity/activity_list.html"


class ActivityCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Activity
    fields = '__all__'
    success_message = '新员工添加成功'

    def get_form(self):
        '''add date picker in forms'''
        form = super(ActivityCreateView, self).get_form()
        form.fields['start_date'].widget = widgets.DateInput(
            attrs={'type': 'date'})
        form.fields['end_date'].widget = widgets.DateInput(
            attrs={'type': 'date'})
        form.fields['address'].widget = widgets.Textarea(attrs={'rows': 1})
        return form


class ActivityUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Activity
    fields = '__all__'
    success_message = "员工信息修改成功."

    def get_form(self):
        '''add date picker in forms'''
        form = super(ActivityUpdateView, self).get_form()
        form.fields['start_date'].widget = widgets.DateInput(
            attrs={'type': 'date'})
        form.fields['end_date'].widget = widgets.DateInput(
            attrs={'type': 'date'})
        form.fields['address'].widget = widgets.Textarea(attrs={'rows': 1})
        return form


class ActivityDeleteView(LoginRequiredMixin, DeleteView):
    model = Activity
    success_url = reverse_lazy('activity-list')
