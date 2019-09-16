from django.shortcuts import render

# Create your views here.

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from django.contrib import messages
from django.http import Http404
from django.views import generic

from braces.views import SelectRelatedMixin

from . import models

from django.contrib.auth import get_user_model
User = get_user_model()

class ClientList(LoginRequiredMixin,generic.ListView):
    
    model = models.Client
