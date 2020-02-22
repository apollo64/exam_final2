from django.contrib import admin
from django.contrib.auth.models import User
from gallery.accounts.models.Account import Account

admin.site.unregister(User)
admin.site.register(Account)
