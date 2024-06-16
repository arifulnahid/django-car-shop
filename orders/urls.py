from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>/', views.buy_now, name='buy_now'),
    path('', views.orders, name='orders'),
]
