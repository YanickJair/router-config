from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django import forms
from django.db.models import Q
from django.template import Context, Template

from . import models

def generator(request):
    if request.method == 'POST':
        _input = request.POST
        router = models.Router.objects.get(id=_input['router'])

        client = models.Client.objects.filter(
            Q(ip=_input['ip'])
            | Q(hostname=_input['hostname'])
        )

        if client.exists():
            info = get_client_info(_input)
            client.update(**info)
            template = get_rendered_template(client.get(), router.layout)
        else:
            client = models.Client(
                ip=_input['ip'],
                hostname=_input['hostname'],
                client_name=_input['client_name'],
                address=_input['address'],
                router=router
            )
            client.save()
            template = get_rendered_template(client, router.layout)
        print(template)
        return HttpResponse(template)
    return HttpResponse("Bad Request")



def get_rendered_template(client, layout):
    #* Create a Template from layout and a Context dict using the input data
    template = Template(layout)
    context = Context({
        'IP': client.ip,
        'HOSTNAME': client.hostname,
        'CLIENT_NAME': client.client_name,
        'MORADA': client.address
    })

    return template.render(context)

#* Create a dict for client so can be used when updating
def get_client_info(_client):
    info = {}

    set_field('ip', info, _client)
    set_field('hostname', info, _client)
    set_field('client_name', info, _client)
    set_field('address', info, _client)
    set_field('router', info, _client)

    return info if len(info.keys()) else None

#* set field, make a field blank if no data or if desired (i.e. fill_blank)
def set_field(field, bucket, _input, fill_blank=False):
    data = _input.get(field)
    if data is None and not fill_blank: 
        return None
    
    if isinstance(data, bool):
        bucket[field] = data
        return None
    
    data = None if data is None else data.strip()
    if data or fill_blank:
        bucket[field] = data
