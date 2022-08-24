from django.urls import path
from . import views

urlpatterns = [
    path('info/', views.show),
    path('insert/', views.insert),
]
