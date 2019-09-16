from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'clients'

urlpatterns = [
    path('', views.ClientList.as_view(),name='all'),
]
