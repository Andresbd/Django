# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader
from .models import Actor


def index(request):
    latest_actor_list = Actor.objects.order_by('-first_name')[:5]
    template = loader.get_template('andan/index.html')
    context = {
        'latest_actor_list': latest_actor_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, actor_id):
    return HttpResponse("Estas viendo al actor %s." % actor_id)

def detail(request, actor_id):
    try:
        actor = Actor.objects.get(pk=actor_id)
    except Actor.DoesNotExist:
        raise Http404("El actor no existe")
    return render(request, 'andan/detail.html', {'actor': actor})
