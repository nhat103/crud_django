from django.urls import path
from . import views

urlpatterns = [
    path('info/', views.show),
    path('insert/', views.insert),
    path('choice/', views.choiceUser, name='edit'),
    path('edit/', views.update, name='update'),
]
