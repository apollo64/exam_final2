from django.contrib import admin
from django.urls import path

from .views.pictures import PicturesIndexView

app_name = 'pictures'

urlpatterns = [

    path('', PicturesIndexView.as_view(), name='index'),
]
