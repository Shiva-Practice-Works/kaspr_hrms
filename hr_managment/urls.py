from django.urls import path ,include
from .views import  Hr_login, Hr_registration
urlpatterns = [
    path('hrl/', Hr_login,name='Hr_login'),
    path('hrr/', Hr_registration, name='Hr_registration'),
]
