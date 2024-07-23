from django.shortcuts import render
from django.http import HttpResponse

def post(request):
    return HttpResponse('welcome to posts page, bro!')