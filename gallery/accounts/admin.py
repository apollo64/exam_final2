from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Account


class ProfileInline(admin.StackedInline):
    model = Account
    fields = ['name', 'surname', 'email']


class ProfileAdmin(UserAdmin):
    inlines = [ProfileInline]


admin.site.unregister(User)
admin.site.register(Account)
admin.site.register(User, ProfileAdmin)
