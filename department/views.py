from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.forms import widgets, forms
from django.urls import reverse_lazy

from staff.models import Staff
from .models import Department


class DepartmentListView(LoginRequiredMixin, ListView):
    model = Department
    context_object_name = 'department_list'
    template_name = "department/department_list.html"


class DepartmentDetailView(LoginRequiredMixin, DetailView):
    model = Department
    template_name = "department/department_detail.html"
    context_object_name = 'department'

    def get_context_data(self, **kwargs):
        departments = Department.objects.all()

        bulk = {}
        for department in departments:
            bulk[department.id] = {
                "department": department,
                "staffCount": department.staff_set.all().count()
            }

        context = {
            "departments": bulk
        }
        return context


class DepartmentCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Department
    fields = '__all__'
    success_message = '新部门添加成功'

    def get_form(self):
        '''add date picker in forms'''
        form = super(DepartmentCreateView, self).get_form()
        return form


class DepartmentUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Department
    fields = '__all__'
    success_message = "部门信息修改成功."

    def get_form(self):
        '''add date picker in forms'''
        form = super(DepartmentUpdateView, self).get_form()
        return form


class DepartmentDeleteView(LoginRequiredMixin, DeleteView):
    model = Department
    success_url = reverse_lazy('department-list')
