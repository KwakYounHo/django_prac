from django.shortcuts import render, HttpResponse

def index(request):
  return HttpResponse("Hello World")

def create(request):
  return HttpResponse("Create Section")

def read(request, id):
  return HttpResponse(f"Read seq: {id}")