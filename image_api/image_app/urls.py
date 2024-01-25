from django.urls import path
from . import views

urlpatterns = [
    path('generate_image/', views.generate_dalle_image, name='generate_dalle_image'),
    path('generate_text/', views.generate_text_from_image, name='generate_text_from_image'),
]
