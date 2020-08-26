from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django import forms
from django.db.models import Q
from django.template import Context, Template
from django.utils import timezone
from datetime import datetime

import demo.forms as df

from . import models

def generator(request):
    if request.method == 'POST':
        try:
            form = df.CustomerForm(request.POST)
            if form.is_valid():
                _input = request.POST
                equipement = models.Equipment.objects.get(id=_input['equipement'])

                customer = models.Customer.objects.filter(
                    Q(ip=_input['ip'])
                    | Q(hostname=_input['hostname'])
                )

                if customer.exists():
                    info = get_customer_info(_input)
                    customer.update(**info, updated_at=datetime.now(tz=timezone.utc))
                    template = get_rendered_template(customer.get(), equipement.layout)

                else:
                    customer = models.Customer(
                        ip=_input['ip'],
                        hostname=_input['hostname'],
                        name=_input['name'],
                        address=_input['address'],
                        equipement=equipement
                    )
                    customer.save()
                    template = get_rendered_template(customer, equipement.layout)
                return HttpResponse(template)
        except:
            raise
    return HttpResponse("Bad Request")

def get_rendered_template(customer, layout):
    #* Create a Template from layout and a Context dict using the input data
    template = Template(layout)
    context = Context({
        'IP': customer.ip,
        'HOSTNAME': customer.hostname,
        'CLIENT_NAME': customer.name,
        'MORADA': customer.address
    })

    return template.render(context)

#* Create a dict for client so can be used when updating
def get_customer_info(_customer):
    info = {}

    set_field('ip', info, _customer)
    set_field('hostname', info, _customer)
    set_field('name', info, _customer)
    set_field('address', info, _customer)
    set_field('router', info, _customer)

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
