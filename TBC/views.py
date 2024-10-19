from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from django.views.decorators.cache import cache_control

def home_view(request):
    render(request, 'home.html')
