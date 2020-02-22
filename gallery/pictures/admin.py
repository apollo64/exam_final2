from django.contrib import admin

# Register your models here.
from .models import Picture, Comment

admin.register(Picture)
admin.register(Comment)
