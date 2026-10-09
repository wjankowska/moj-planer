from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('toggle/<int:item_id>/', views.toggle_task, name='toggle_task'),
]
