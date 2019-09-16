from django.db import models
from django.urls import reverse

from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.

class Client(models.Model):

    user=models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=254, unique=False)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('clients:all',kwargs={'username':self.user.username,'pk':self.pk})

    class Meta:
        ordering = ['name']
