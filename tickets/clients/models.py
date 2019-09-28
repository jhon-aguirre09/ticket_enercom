from django.db import models
from django.urls import reverse

from django.contrib.auth import get_user_model
User = get_user_model()

class Client(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=254, unique=False)
    email = models.EmailField(max_length=254, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('clients:all')

    class Meta:
        ordering = ['name']

class Groups(models.Model):
    name = models.TextField()
    client = models.ManyToManyField(Client, through='GroupMember')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('clients:groups')

class GroupMember(models.Model):
    group = models.ForeignKey(Groups, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return self.group.name

    class Meta:
        unique_together = ['group','client']
