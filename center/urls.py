

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('register/', views.register_customer,
         name='register_customer'),

    path('login/', views.customer_login,
         name='login'),

    path('dashboard/', views.dashboard,
         name='dashboard'),

    path('logout/', views.customer_logout,
         name='logout'),
]
