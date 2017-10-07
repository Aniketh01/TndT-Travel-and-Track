# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from TndT import settings


def login(request, *args, **kwargs):
    return render(request, 'userauth/login.html')
