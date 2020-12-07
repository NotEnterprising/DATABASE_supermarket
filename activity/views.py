from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.forms import widgets
from django.urls import reverse_lazy

from .forms import ActivityForm
from .models import Activity


class ActivityListView(LoginRequiredMixin, ListView, PermissionRequiredMixin):
    model = Activity
    context_object_name = 'activity_list'
    template_name = "activity/activity_list.html"
    permission_required = ('activity.view_activity', 'activity.add_activity')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ActivityForm()
        return context


class ActivityCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = ActivityForm
    template_name = 'activity/mgt_form.html'
    success_url = reverse_lazy('activity-list')
    success_message = '新品类添加成功'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ActivityForm()
        return context


class ActivityUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Activity
    fields = '__all__'
    template_name = 'activity/mgt_form.html'
    success_message = "品类信息修改成功"
    success_url = reverse_lazy('activity-list')

    def get_form(self):
        '''add date picker in forms'''
        form = super(ActivityUpdateView, self).get_form()
        return form


class ActivityDeleteView(LoginRequiredMixin, DeleteView):
    model = Activity
    success_url = reverse_lazy('activity-list')
    template_name = 'activity/core_confirm_delete.html'
    success_message = "品类信息删除成功"
