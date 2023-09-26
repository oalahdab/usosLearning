"""
URL mappings for the user API.
"""
from django.urls import path

from user import views


app_name = 'user'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('me/', views.ManageUserView.as_view(), name='me'),
]


# from .views import *
# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# 
# router = DefaultRouter()
# router.register('data', GetMethod, basename='data')
# urlpatterns = router.urls
