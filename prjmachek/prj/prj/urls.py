from django.urls import path
from . import views

urlpatterns = [
    path('api-playground/', views.api_playground, name='api_playground'),
    path('api/books/', views.api_books, name='api_books'),
]
