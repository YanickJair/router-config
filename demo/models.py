from django.db import models

class Router(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, unique=True)
    layout = models.TextField()

    def __str__(self):
        return self.name

class Client(models.Model):
    ip = models.CharField(max_length=50, null=False, blank=False, unique=True, verbose_name="IP")
    hostname = models.CharField(max_length=50, null=False, blank=False, unique=True, verbose_name="Hostname")
    client_name = models.CharField(max_length=50, null=False, blank=False, verbose_name="Cliente")
    address = models.CharField(max_length=50, null=False, blank=False, verbose_name="Morada")
    technician_contact = models.CharField(max_length=50, null=False, blank=False, verbose_name="Contacto Técnico")
    router = models.ForeignKey(Router, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.hostname