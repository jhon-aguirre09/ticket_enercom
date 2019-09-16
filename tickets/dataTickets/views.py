from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from django.contrib import messages
from django.http import Http404
from django.views import generic

from braces.views import SelectRelatedMixin

from . import models
# from . import forms

class CreateTicket(generic.CreateView):
    template_name = 'thanks.html'

# class TicketList(LoginRequiredMixin):
#     template_name = 'dashboard.html'
