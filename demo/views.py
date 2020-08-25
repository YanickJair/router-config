from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django import forms
from django.template import Context, Template

from . import models

def index(request):
    if request.method == 'POST':
        client = request.POST
        router = models.Router.objects.get(id=client['router'])
        template = Template(router.layout)
        context = Context({
            'IP': client['ip'],
            'HOSTNAME': client['hostname'],
            'CLIENT_NAME': client['client_name'],
            'MORADA': client['address']
        })

    return HttpResponse(template.render(context))