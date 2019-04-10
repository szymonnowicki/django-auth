from django.urls import path, include

from .views import HomeAuthPage

urlpatterns = [
    path('', HomeAuthPage.as_view(), name='home_auth_page'),
    
]
