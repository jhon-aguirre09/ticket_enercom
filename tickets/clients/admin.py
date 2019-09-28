from django.contrib import admin
from . import models
# Register your models here.

class ClientAdmin(admin.ModelAdmin):

    list_display = ['name','email']

admin.site.register(models.Client, ClientAdmin)
admin.site.register(models.Groups)
admin.site.register(models.GroupMember)
