from django.conf.urls import url
from firstapp import views

urlpatters = [
    url(r'^$', views.index, name= 'index'),
    url(r'^$', views.fn1, name ='fn1'),
    url(r'^$', views.fn2, name = 'fn2'),

]