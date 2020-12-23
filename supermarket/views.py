from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.forms import widgets, forms
from django.urls import reverse_lazy

from purchase.models import Purchase
from supermarketToactivity.models import SupermarketToActivity
from supermarketToexpress.models import SupermarketToExpress
from .models import Supermarket


class SupermarketListView(LoginRequiredMixin, ListView):
    model = Supermarket
    context_object_name = 'supermarket_list'
    template_name = "supermarket/supermarket_list.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        supermarket_list = Supermarket.objects.all()
        time = []
        for supermarket in supermarket_list:
            temp1 = float(supermarket.start_time.hour) + float(supermarket.start_time.minute) / 60
            temp2 = float(supermarket.end_time.hour) + float(supermarket.end_time.minute) / 60
            temp = {'start_time': temp1, 'end_time': temp2}
            time.append(temp)
        context = {
            "supermarket_list": supermarket_list,
            "time": time,
        }
        return context


class SupermarketDetailView(LoginRequiredMixin, DetailView):
    model = Supermarket
    template_name = "supermarket/supermarket_detail.html"
    context_object_name = 'supermarket'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        results = SupermarketToActivity.objects.all()
        supermarket = Supermarket.objects.get(id=self.kwargs['pk'])
        departments = supermarket.department_set.all()
        commoditys = supermarket.commodity_set.all()

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

        resultsOfExpress = SupermarketToExpress.objects.all()
        bulk1 = {}
        for result in resultsOfExpress:
            expresses = []
            for express in resultsOfExpress:
                if express.supermarket == result.supermarket:
                    expresses.append(express.express)
            bulk1[result.supermarket.id] = {
                "supermarket": result.supermarket,
                "expresses": expresses,
            }
        context['results'] = bulk
        context['resultsOfExpress'] = bulk1
        context['departments'] = departments
        context['commoditys'] = commoditys

        purchases = Purchase.objects.all()

        value = [0] * 12
        for p in purchases:
            if supermarket.id == p.commodity.supermarket.id:
                date = p.purchase_date.month
                value[date - 1] = value[date - 1] + p.commodity.price * p.num
        context['income'] = value
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

    def get(self, request, *args, **kwargs):
        if request.user.is_customer or request.user.is_staff:
            return redirect('supermarket-list')
        return super(SupermarketCreateView, self).get(self, request, *args, **kwargs)


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

    def get(self, request, *args, **kwargs):
        if request.user.is_customer or request.user.is_staff:
            return redirect('supermarket-list')
        return super(SupermarketUpdateView, self).get(self, request, *args, **kwargs)


class SupermarketDeleteView(LoginRequiredMixin, DeleteView):
    model = Supermarket
    success_url = reverse_lazy('supermarket-list')

    def get(self, request, *args, **kwargs):
        if request.user.is_customer or request.user.is_staff:
            return redirect('supermarket-list')
        return super(SupermarketDeleteView, self).get(self, request, *args, **kwargs)


class SupermarketDetailView1(LoginRequiredMixin, DetailView):
    model = Supermarket
    template_name = "supermarket/supermarket_detail_commodity.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        supermarket = Supermarket.objects.get(id=self.kwargs['pk'])
        commoditys = supermarket.commodity_set.all()
        context['commoditys'] = commoditys
        context['supermarket'] = supermarket
        return context
