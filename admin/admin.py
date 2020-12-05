from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from admin.models import Admin

admin.site.register(Admin, UserAdmin)
