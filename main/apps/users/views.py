# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(req):
    response = "placeholder for some users stuff"
    return HttpResponse(response)