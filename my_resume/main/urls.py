# main/urls.py

from django.urls import path
from . import views
from .views import resume

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('', resume, name='resume'),
    # add more URL patterns here
]
