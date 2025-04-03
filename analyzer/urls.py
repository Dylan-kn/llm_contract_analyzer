from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_contract, name='upload_contract'),
    path('contract/<int:pk>/', views.view_contract, name='view_contract'),
    path('contracts/', views.contract_list, name='contract_list'),
    path('contract/<int:pk>/delete/', views.delete_contract, name='delete_contract'),
    path('contract/<int:pk>/ask/', views.ask_question, name='ask_question'),
    path('', views.landing_page, name='landing_page')
]

