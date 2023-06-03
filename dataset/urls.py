from django.urls import path
from . import views

urlpatterns = [
    path('', views.dataset_list, name='dataset-list'),
    path('dataset/details/<int:dataset_id>/', views.dataset_details, name='dataset-details'),
]
