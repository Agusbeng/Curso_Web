from django import http
from django.http import HttpResponse, request
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Practica Python!")\

def febrero(request):
    #esto es un comentario
    return HttpResponse("Haz ejercicio!")

def marzo(request):
    #esto es un comentario
    return HttpResponse("Come menos carne.")
