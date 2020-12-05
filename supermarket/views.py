from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.forms import widgets, forms
from django.urls import reverse_lazy

from supermarketToactivity.models import SupermarketToActivity
from .models import Supermarket


class SupermarketListView(LoginRequiredMixin, ListView):
    model = Supermarket
    context_object_name = 'supermarket_list'
    template_name = "supermarket/supermarket_list.html"


class SupermarketDetailView(LoginRequiredMixin, DetailView):
    model = Supermarket
    template_name = "supermarket/supermarket_detail.html"
    context_object_name = 'supermarket'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        results = SupermarketToActivity.objects.all()
        supermarket = Supermarket.objects.get(id=self.kwargs['pk'])
        departments = supermarket.department_set.all()

        bulk = {}
        for result in results:
            activitys = []
            for activity in results:
                if activity.supermarket == result.supermarket:
                    activitys.append(activity.activity)
            bulk[result.supermarket.id] = {
                "supermarket": result.supermarket,
                "activitys": activitys,
            }
        context['results'] = bulk
        context['departments'] = departments
        return context


class SupermarketCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Supermarket
    fields = '__all__'
    success_message = '新超市添加成功'

    def get_form(self):
        '''add date picker in forms'''
        form = super(SupermarketCreateView, self).get_form()
        form.fields['start_time'].widget = widgets.DateInput(
            attrs={'type': 'time'})
        form.fields['end_time'].widget = widgets.DateInput(
            attrs={'type': 'time'})
        form.fields['address'].widget = widgets.Textarea(attrs={'rows': 1})
        return form


class SupermarketUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Supermarket
    fields = '__all__'
    success_message = "超市信息修改成功."

    def get_form(self):
        '''add date picker in forms'''
        form = super(SupermarketUpdateView, self).get_form()
        form.fields['start_time'].widget = widgets.DateInput(
            attrs={'type': 'time'})
        form.fields['end_time'].widget = widgets.DateInput(
            attrs={'type': 'time'})
        form.fields['address'].widget = widgets.Textarea(attrs={'rows': 1})
        return form


class SupermarketDeleteView(LoginRequiredMixin, DeleteView):
    model = Supermarket
    success_url = reverse_lazy('supermarket-list')
