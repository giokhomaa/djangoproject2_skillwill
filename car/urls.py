from django.urls import path
from . import views

urlpatterns = [
    path('', views.SelectCarsView.as_view(), name = 'selectallcars'),
    path('add/', views.AddCarView.as_view(), name = 'addcar'),
    path('delete/<int:pk>', views.DeleteCarView.as_view(), name = 'deletecar')
]