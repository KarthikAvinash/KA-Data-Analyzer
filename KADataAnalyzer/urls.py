from django.urls import path, include

urlpatterns = [
    # Other URL patterns
    
    path('dataset/', include('dataset.urls')),
    
    # Other URL patterns
]
