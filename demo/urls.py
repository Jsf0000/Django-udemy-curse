from django.urls import path
from . import views
from .models import Book

urlpatterns = [
    path('first', views.first)
    # path('another', Another.as_view()),
]