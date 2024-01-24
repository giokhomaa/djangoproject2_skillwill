from django.urls import path
from . import views

urlpatterns = [
    path('', views.SelectAnimalsView.as_view(), name = 'selectallanimals'),
    path('add/', views.AddAnimalView.as_view(), name = 'addanimals'),
    path('delete/<int:pk>', views.DeleteAnimalView.as_view(), name = 'deleteanimals')
]