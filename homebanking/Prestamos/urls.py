
from django.urls import path
from . import views

urlpatterns = [
    path('prestamos/', views.LoanRequest.as_view(), name = 'prestamos'),
]