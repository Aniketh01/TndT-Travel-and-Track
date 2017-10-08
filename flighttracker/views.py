# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def mapinteg(request):
    f = open("flighttracker/latitude.json", "r")
    latitude = []
    for i in range(5):
        j = f.readline()
        latitude.append(j)
    f = open("flighttracker/longitude.json", "r")
    longitude = []
    for i in range(5):
        j = f.readline()
        longitude.append(j)

    context = {"lat": latitude, "long": longitude}
    return render(request, 'dashboard/map-integration.html', context)