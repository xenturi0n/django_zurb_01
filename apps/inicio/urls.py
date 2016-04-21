from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^prueba/$', views.prueba),
    url(r'^barra_01/$', views.barra_01),
    url(r'^$', views.inicio),    
]
