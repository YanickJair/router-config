from django.db import models
from django.utils import timezone
from mptt.models import MPTTModel
from treewidget.fields import TreeForeignKey

class Equipment(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, unique=True)
    layout = models.TextField()

    def __str__(self):
        return self.name

class Customer(models.Model):
    ip = models.CharField(max_length=50, null=False, blank=False, unique=True, verbose_name="IP")
    hostname = models.CharField(max_length=50, null=False, blank=False, unique=True, verbose_name="Hostname")
    name = models.CharField(max_length=50, null=False, blank=False, verbose_name="Cliente")
    address = models.CharField(max_length=50, null=False, blank=False, verbose_name="Morada")
    # technician_contact = models.CharField(max_length=50, null=False, blank=False, verbose_name="Contacto Técnico")
    equipement = models.ForeignKey(Equipment, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=False, blank=True, null=True)

    def __str__(self):
        return self.hostname