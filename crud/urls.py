from django.urls import path
from . import views

urlpatterns = [
    path('info/', views.info, name='infouser'),
    path('insert/', views.insert, name='insertuser'),
    path('choice/', views.choiceUser, name='edit'),
    path('edit/', views.update, name='update'),
    path('edit/<int:pk>', views.edit, name='edit'),
    path('delete/<int:pk>', views.deleteUser, name='delete'),
]
