from django import forms
from django.contrib import admin

from django.template.response import TemplateResponse
from django.urls import path

from . import models

class ClientAdmin(admin.ModelAdmin):
    change_form_template = 'admin/router/router_change_form.html'

# Register your models here.
admin.site.register(models.Router)
admin.site.register(models.Client, ClientAdmin)