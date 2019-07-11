from django.urls import path

from .views import HomePageView

urlpatterns = [
    path('messages/', HomePageView.as_view(), name='home')
]