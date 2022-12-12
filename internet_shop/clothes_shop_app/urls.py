from django.urls import path

from .views import *


urlpatterns = [
    path('', Home.as_view(), name='index'),
    path('cloth/<int:pk>/', Retrieve_clothes.as_view(), name='retrieve'),
    path('categories', Categories.as_view(), name='categories'),
]