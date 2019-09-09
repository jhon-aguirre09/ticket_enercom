from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def Home(request):
     return HttpResponseRedirect(reverse('login'))
