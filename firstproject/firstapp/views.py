from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    my_dict = {'insert':'Now you are inside the insert function'}
    return render(request, 'templates/index.html', context = my_dict )

def fn1(response):
    return HttpResponse('I am the statement 1')

def fn2(response):
    return HttpResponse('I am the second statement')