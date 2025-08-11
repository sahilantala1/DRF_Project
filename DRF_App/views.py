from django.http import HttpResponse  # ✅ correct import
from django.shortcuts import render

def home(request):
    return HttpResponse("HELLo")
