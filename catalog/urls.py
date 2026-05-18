from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalog_view, name='catalog'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
