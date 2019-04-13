from django.urls import path, include

from .views import HomeAuthPage
from .views import SuccesRegister

from . import views

urlpatterns = [
    path('', HomeAuthPage.as_view(), name='home_auth_page'),
    path('register/', views.register_check, name='register_check'),
    path('succes_register/', SuccesRegister.as_view(), name='succes_register'),

]
