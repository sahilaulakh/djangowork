from django.conf.urls import url
from firstapp import views

urlpatterns = [
     url(r'^$', views.index, name='index'),
     #url(r'^secfunction/', views.secfunction, name='secfunction'),
     #url(r'^thirdfunction/', views.thirdfunction, name='thirdfunction'),
]
