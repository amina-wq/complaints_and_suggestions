from django.urls import path

from . import views

urlpatterns = [
    path('', views.suggestions, name='suggestions'),
    path('complaints/', views.complaints, name='complaints'),
    path('suggestions/', views.suggestions, name='suggestions'),
    path('create_complaints/', views.create_complaints, name='create_complaints'),
    path('create_suggestions/', views.create_suggestions, name='create_suggestions')
]
