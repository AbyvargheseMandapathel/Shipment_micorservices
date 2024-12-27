from django.urls import path
from . import views

urlpatterns = [
    path('awb/', views.list_awbs, name='list_awbs'),
    path('awb/add/', views.add_awb, name='add_awb'),
]
