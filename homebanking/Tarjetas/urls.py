
from django.urls import path
from . import views

urlpatterns = [
    path('tarjetas/', views.index3, name = 'tarjetas'),
]