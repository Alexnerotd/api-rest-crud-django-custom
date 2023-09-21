from django.urls import path

from .views import APIListUserView, APIPutUserView
urlpatterns = [
    path('users/', APIListUserView.as_view(), name='users'),
    path('users/<int:pk>/', APIPutUserView.as_view(), name='users-put'),
]