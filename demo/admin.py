from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin

from . import models

@admin.register(models.Customer)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'ip', 'hostname', 'address', 'created_at', 'updated_at')
    list_display_links = ('id', 'name', 'ip', 'hostname', 'address', 'created_at', 'updated_at')
    exclude = ('created_at', 'updated_at')
    change_form_template = 'admin/router/router_change_form.html'


@admin.register(models.Equipment)
class EquipmentAdmin(DjangoMpttAdmin):
    pass

