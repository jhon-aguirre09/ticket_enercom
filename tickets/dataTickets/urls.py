from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'dataTickets'

urlpatterns = [
    # path('',views.TicketList.as_view(), name='all'),
    path('new/',views.CreateTicket.as_view(), name='create'),
    # re_path(r'by/(?P<username>[-\w]+)/(?P<pk>\d+)/$',views.TicketDetail.as_view(),name='single'),
]
