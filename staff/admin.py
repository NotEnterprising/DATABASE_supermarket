from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from staff.models import Staff

admin.site.register(Staff, UserAdmin)
