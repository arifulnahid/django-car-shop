from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.customer_login, name='login'),
    path('signup/', views.customer_signup, name='signup'),
    path('logout/', views.customer_logout, name='logout'),
    path('profile/', views.customer_profile, name='profile')
]
