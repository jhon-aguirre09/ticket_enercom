from django.urls import path,re_path, include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'clients'

urlpatterns = [
    path('', views.ClientList.as_view(),name='all'),
    re_path('new/', views.CreateClient.as_view(),name='create'),
    re_path(r'delete/(?P<pk>\d+)/$',views.DeleteClient.as_view(),name='delete'),
    re_path(r'edit/(?P<pk>\d+)/$',views.ClientUpdate.as_view(),name='client_edit'),
]
