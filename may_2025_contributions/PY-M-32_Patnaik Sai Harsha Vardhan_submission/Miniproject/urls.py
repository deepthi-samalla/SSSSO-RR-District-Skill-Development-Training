#fileorganizer/urls.py
from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name='fileorganizer-index'),
]
