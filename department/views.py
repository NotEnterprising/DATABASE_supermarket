from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.forms import widgets, forms
from django.urls import reverse_lazy

from staff.models import Staff
from supermarket.models import Supermarket
from .models import Department


class DepartmentListView(LoginRequiredMixin, ListView):
    model = Department
    context_object_name = 'department_list'
    template_name = "department/department_list.html"

    def get_context_data(self, **kwargs):
        departments = Department.objects.all()
        supermarkets = Supermarket.objects.all()

        bulk = {}
        for department in departments:
            bulk[department.id] = {
                "department": department,
                "staffCount": department.staff_set.all().count()
            }
        bulk1 = []
        for supermarket in supermarkets:
            temp = []
            total = 0
            for department in supermarket.department_set:
                total = total + department.staff_set.all().count()
            for department in supermarket.department_set:
                proportion = float(department.staff_set.all().count() / total)
                temp.append({"department": department, "proportion": proportion})
            bulk1.append({
                "supermarket": supermarket,
                "departments": temp,
            })
        context = {
            "departments": bulk,
            "supermarkets": bulk1,
        }
        return context

    def get(self, request, *args, **kwargs):
        if request.user.is_customer:
            return redirect('home')
        return super(DepartmentListView, self).get(self, request, *args, **kwargs)


class DepartmentDetailView(LoginRequiredMixin, DetailView):
    model = Department
    template_name = "department/department_detail.html"
    context_object_name = 'department'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        department = Department.objects.get(id=self.kwargs['pk'])
        staffs = department.staff_set.all()
        num = department.staff_set.all().count()
        context['staffs'] = staffs
        context['num'] = num
        return context

    def get(self, request, *args, **kwargs):
        if request.user.is_customer:
            return redirect('home')
        return super(DepartmentDetailView, self).get(self, request, *args, **kwargs)


class DepartmentCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Department
    fields = '__all__'
    success_message = '新部门添加成功'

    def get_form(self):
        '''add date picker in forms'''
        form = super(DepartmentCreateView, self).get_form()
        return form

    def get(self, request, *args, **kwargs):
        if request.user.is_customer:
            return redirect('home')
        elif request.user.is_staff:
            return redirect('department-list')
        return super(DepartmentCreateView, self).get(self, request, *args, **kwargs)


class DepartmentUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Department
    fields = '__all__'
    success_message = "部门信息修改成功."

    def get_form(self):
        '''add date picker in forms'''
        form = super(DepartmentUpdateView, self).get_form()
        return form

    def get(self, request, *args, **kwargs):
        if request.user.is_customer:
            return redirect('home')
        elif request.user.is_staff:
            return redirect('department-list')
        return super(DepartmentUpdateView, self).get(self, request, *args, **kwargs)


class DepartmentDeleteView(LoginRequiredMixin, DeleteView):
    model = Department
    success_url = reverse_lazy('department-list')

    def get(self, request, *args, **kwargs):
        if request.user.is_customer:
            return redirect('home')
        elif request.user.is_staff:
            return redirect('department-list')
        return super(DepartmentDeleteView, self).get(self, request, *args, **kwargs)
