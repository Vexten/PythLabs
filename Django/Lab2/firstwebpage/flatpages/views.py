from django.shortcuts import render
from django import template
from django.http import HttpResponse

def home(request):
    return render(request, 'templates/index.html')

def st_hd(request):
    return render(request, 'templates/static_handler.html')
