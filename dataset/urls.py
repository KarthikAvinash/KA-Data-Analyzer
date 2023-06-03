from django.urls import path
from dataset.views import dataset_list, dataset_details, scatter_plot

app_name = 'dataset'

urlpatterns = [
    path('', dataset_details, name='dataset_list'),
    # path('datasets/<str:dataset_id>/', dataset_details, name='dataset_details'),
    # path('datasets/<str:dataset_id>/<float:min_conf>/<float:min_support>/', scatter_plot, name='scatter_plot'),
]
