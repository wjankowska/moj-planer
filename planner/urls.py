from django.urls import path
from . import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),  # <-- dodaj tę linijkę
    path('toggle/<int:item_id>/', views.toggle_task, name='toggle_task'),
]

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('toggle/<int:item_id>/', views.toggle_task, name='toggle_task'),
]