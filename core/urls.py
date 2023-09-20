from django.urls import path

from .views import APIListUserView
urlpatterns = [
    path('users/', APIListUserView.as_view(), name='users'),
]