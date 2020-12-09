from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.forms import widgets, forms
from django.urls import reverse_lazy

from admin.models import User
from department.models import Department
from .forms import StaffRegisterForm
from .models import Staff


class StaffListView(LoginRequiredMixin, ListView):
    model = Staff
    context_object_name = 'staff_list'
    template_name = "staff/staff_list.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_customer:
            return redirect('home')
        return super(StaffListView, self).get(self, request, *args, **kwargs)


class StaffDetailView(LoginRequiredMixin, DetailView):
    model = Staff
    template_name = "staff/staff_detail.html"
    context_object_name = 'staff'

    def get(self, request, *args, **kwargs):
        if request.user.is_customer:
            return redirect('home')
        return super(StaffDetailView, self).get(self, request, *args, **kwargs)


class StaffDeleteView(LoginRequiredMixin, DeleteView):
    model = Staff
    success_url = reverse_lazy('staff-list')

    def post(self, request, *args, **kwargs):
        staff = Staff.objects.get(user_id=self.kwargs['pk'])
        temp = staff.user
        staff.delete()
        temp.delete()
        return redirect('staff-list')

    def get(self, request, *args, **kwargs):
        if request.user.is_customer or request.user.is_staff:
            return redirect('home')
        return super(StaffDeleteView, self).get(self, request, *args, **kwargs)


@login_required()
def register(request):
    if request.user.is_customer:
        return redirect('home')
    elif request.user.is_staff:
        return redirect('staff-list')
    if request.method == 'POST':
        form = StaffRegisterForm(request.POST)
        if form.is_valid():
            a = None
            try:
                a = User.objects.get(username=form.cleaned_data['用户名'])
            except:
                pass
            if a is not None:
                messages.warning(request, '用户名已存在')
                form.fields['address'].widget = widgets.Textarea(attrs={'rows': 1})
                return render(request, 'admin/admin_form.html', context={'form': form})
            user = User.objects.create_user(username=form.cleaned_data['用户名'], password=form.cleaned_data['password1'],
                                            is_staff=True)
            staff = Staff.objects.create(name=form.cleaned_data['name'], gender=form.cleaned_data['gender'],
                                         mobile_number=form.cleaned_data['mobile_number'],
                                         address=form.cleaned_data['address'],
                                         entry_date=form.cleaned_data['entry_date'], user_id=user.id,
                                         department_id=request.POST.getlist("department")[0])
            staff.save()
            messages.success(request, '新员工添加成功')
            return redirect('staff-list')
        form.fields['entry_date'].widget = widgets.DateInput(
            attrs={'type': 'date'})
        form.fields['address'].widget = widgets.Textarea(attrs={'rows': 1})
    else:
        form = StaffRegisterForm()
        form.fields['entry_date'].widget = widgets.DateInput(
            attrs={'type': 'date'})
        form.fields['address'].widget = widgets.Textarea(attrs={'rows': 1})
    return render(request, 'staff/staff_form_new.html', context={'form': form})


class StaffUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Staff
    success_message = "员工信息修改成功."
    form_class = StaffRegisterForm

    def get_form(self):
        '''add date picker in forms'''
        form = super(StaffUpdateView, self).get_form()
        form.fields['address'].widget = widgets.Textarea(attrs={'rows': 1})
        form.fields['entry_date'].widget = widgets.DateInput(
            attrs={'type': 'date'})
        return form

    def post(self, request, *args, **kwargs):
        form = StaffRegisterForm(request.POST)
        if form.is_valid():
            staff = Staff.objects.get(user_id=self.kwargs['pk'])
            user = User.objects.get(id=self.kwargs['pk'])
            staff.name = request.POST.get('name')
            staff.gender = request.POST.get('gender')
            staff.mobile_number = request.POST.get('mobile_number')
            staff.address = request.POST.get('address')
            staff.entry_date = request.POST.get('entry_date')
            staff.department_id = request.POST.getlist("department")[0]
            staff.save()
            user.username = request.POST.get('用户名')
            user.set_password(request.POST.get('password1'))
            user.save()
            return redirect('staff-list')
        form.fields['address'].widget = widgets.Textarea(attrs={'rows': 1})
        form.fields['entry_date'].widget = widgets.DateInput(
            attrs={'type': 'date'})
        return render(request, 'staff/staff_form.html', context={'form': form})

    def get(self, request, *args, **kwargs):
        if request.user.is_customer:
            return redirect('home')
        elif request.user.is_staff and (request.user.id != self.kwargs['pk']):
            return redirect('staff-list')
        staff = Staff.objects.get(user_id=self.kwargs['pk'])
        form = self.form_class(instance=staff)
        form.fields['address'].widget = widgets.Textarea(attrs={'rows': 1})
        form.fields['entry_date'].widget = widgets.DateInput(
            attrs={'type': 'date'})
        return render(request, 'staff/staff_form.html', {'form': form})
