from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='homePage'),
    path('bio/', views.bioPage, name='bioPage')
]
