from django.shortcuts import render
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

class CreateClient(LoginRequiredMixin,generic.CreateView):
    fields = ('name','email')
    model = models.Client

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class DeleteClient(LoginRequiredMixin,generic.DeleteView):
    model = models.Client
    success_url = reverse_lazy('clients:all')

    def delete(self,*args,**kwargs):
        messages.success(self.request,'Email Borrado')
        return super().delete(*args,**kwargs)

class ClientUpdate(LoginRequiredMixin, generic.UpdateView):
    model = models.Client
    fields = ['email']
    template_name_suffix = '_update_form'
