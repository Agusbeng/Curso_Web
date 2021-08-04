from django.urls import path
from . import views

#otro comentario

urlpatterns = [
    path('enero', views.index),
    path('febrero', views.febrero),
    path('marzo', views.marzo),


]