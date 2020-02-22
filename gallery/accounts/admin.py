from django.contrib import admin
from django.contrib.auth.models import User
from .models import Account

admin.site.unregister(User)
admin.site.register(Account)

