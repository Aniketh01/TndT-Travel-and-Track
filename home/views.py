# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.



def home(request, *args, **kwargs):
    return render(request, 'home/index.html')

def about(request):
    return render(request, 'userauth/about.html')