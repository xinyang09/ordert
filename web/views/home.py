from django.shortcuts import render, redirect
from web import models

def home(request):
    return render(request, "home.html")