from django.urls import path
from . import views

app_name = 'vehicles'

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    path('register/', views.register_vehicle, name='register_vehicle'),
    path('list_vehicles/', views.list_vehicles, name='list_vehicles'),
    path('edit/<int:pk>/', views.edit_vehicle, name='edit_vehicle'),
    path('details/<int:pk>/', views.view_vehicle_details,
         name='view_vehicle_details'),
]
