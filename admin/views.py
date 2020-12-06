from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.forms import widgets, forms
from django.urls import reverse_lazy

from .forms import AdminRegisterForm
from .models import Admin, User


class AdminListView(LoginRequiredMixin, ListView):
    model = Admin
    context_object_name = 'admin_list'
    template_name = "admin/admin_list.html"


class AdminDetailView(LoginRequiredMixin, DetailView):
    model = Admin
    template_name = "admin/admin_detail.html"
    context_object_name = 'admin'


@login_required()
def register(request):
    if request.method == 'POST':
        form = AdminRegisterForm(request.POST)
        if form.is_valid():
            if User.objects.get(username=form.cleaned_data['用户名']) is not None:
                messages.warning(request, '用户名已存在')
                form.fields['address'].widget = widgets.Textarea(attrs={'rows': 1})
                return render(request, 'admin/admin_form.html', context={'form': form})
            user = User.objects.create_user(username=form.cleaned_data['用户名'], password=form.cleaned_data['password1'],
                                            is_admin=True)

            admin = Admin.objects.create(name=form.cleaned_data['name'], gender=form.cleaned_data['gender'],
                                         mobile_number=form.cleaned_data['mobile_number'],
                                         address=form.cleaned_data['address'], user_id=user.id)
            admin.save()
            messages.success(request, '新管理员添加成功')
            return redirect('admin-list')
        form.fields['address'].widget = widgets.Textarea(attrs={'rows': 1})
    else:
        form = AdminRegisterForm()
        form.fields['address'].widget = widgets.Textarea(attrs={'rows': 1})
    return render(request, 'admin/admin_form.html', context={'form': form})


class AdminUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Admin
    success_message = "管理员信息修改成功."
    form_class = AdminRegisterForm

    def get_form(self):
        '''add date picker in forms'''
        form = super(AdminUpdateView, self).get_form()
        form.fields['address'].widget = widgets.Textarea(attrs={'rows': 1})
        return form

    def post(self, request, *args, **kwargs):
        form = AdminRegisterForm(request.POST)
        if form.is_valid():
            admin = Admin.objects.get(user_id=self.kwargs['pk'])
            user = User.objects.get(id=self.kwargs['pk'])
            admin.name = request.POST.get('name')
            admin.gender = request.POST.get('gender')
            admin.mobile_number = request.POST.get('mobile_number')
            admin.address = request.POST.get('address')
            admin.save()
            user.username = request.POST.get('用户名')
            user.set_password(request.POST.get('password1'))
            user.save()
            return redirect('admin-list')
        form.fields['address'].widget = widgets.Textarea(attrs={'rows': 1})
        return render(request, 'admin/admin_form.html', context={'form': form})

    def get(self, request, *args, **kwargs):
        admin = Admin.objects.get(user_id=self.kwargs['pk'])
        user = User.objects.get(id=self.kwargs['pk'])
        form = self.form_class(instance=admin)
        form.fields['address'].widget = widgets.Textarea(attrs={'rows': 1})
        return render(request, 'admin/admin_form.html', {'form': form})


class AdminDeleteView(LoginRequiredMixin, DeleteView):
    model = Admin
    success_url = reverse_lazy('admin-list')

    def post(self, request, *args, **kwargs):
        admin = Admin.objects.get(user_id=self.kwargs['pk'])
        temp = admin.user
        admin.delete()
        temp.delete()
        return redirect('admin-list')
