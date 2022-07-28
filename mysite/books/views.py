from django.shortcuts import render
from django.http import HttpResponse


def mine(request):
    return HttpResponse("My name is Nata")
