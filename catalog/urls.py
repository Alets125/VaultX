from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome_view, name='welcome'),
    path('catalog/', views.catalog_view, name='catalog'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
