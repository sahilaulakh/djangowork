from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(response):
    return HttpResponse('We are getting this from index function, views.py')

def fn1(response):
    return HttpResponse('I am the statement 1')

def fn2(response):
    return HttpResponse('I am the second statement')