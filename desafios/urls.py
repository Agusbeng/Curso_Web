from django.urls import path
from . import views



urlpatterns = [
    path('enero', views.index)


]