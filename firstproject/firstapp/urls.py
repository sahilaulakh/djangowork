from django.conf.urls import url
from . import views

urlpatters = [
    url(r'^index$', views.index, name='index'),
    #url(r'^$', views.fn1, name ='fn1'),
    #url(r'^$', views.fn2, name = 'fn2'),

]