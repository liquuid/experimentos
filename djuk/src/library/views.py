# -*- coding: utf-8 -*-
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render_to_response
from library.models import Track
from library.forms import TrackForm

def index(request):
    form = TrackForm()
    
    if request.method == "POST":
        form = TrackForm(request.POST);
        t = Track()
        t.url = form.data['url'] 
        t.save()

    return render_to_response('index.html',locals())

def get_tracks(request):
    tracks = Track.objects.all().order_by('id')
    retorno = serializers.serialize("json",  tracks)
    return HttpResponse(retorno, mimetype="text/javascript")
