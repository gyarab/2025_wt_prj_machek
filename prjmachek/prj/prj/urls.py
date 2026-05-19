from django.urls import path
from . import views

urlpatterns = [


    path('api-playground/', views.api_playground, name='api_playground'),


    path('api/polozky/', views.api_polozky, name='api_polozky'),
]
