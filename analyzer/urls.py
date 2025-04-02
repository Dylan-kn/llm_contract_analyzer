from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_contract, name='upload_contract'),
    path('contract/<int:pk>/', views.view_contract, name='view_contract'),
]

