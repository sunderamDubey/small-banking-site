
from xml.etree.ElementInclude import include
from django.urls import path
from . import views
from .views import signup

urlpatterns = [
    path('login/', views.index1, name = 'index1'),
    path('signup/', signup.as_view(), name = 'signup'),

]