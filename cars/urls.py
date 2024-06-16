from django.urls import path
from . import views

urlpatterns = [
    path('', views.Cars.as_view(), name='cars'),
    path('<int:id>/', views.cars, name='car'),
    path('details/<int:id>/', views.car, name='car_details'),
]
