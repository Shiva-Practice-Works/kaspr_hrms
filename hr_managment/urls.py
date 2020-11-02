from django.urls import path ,include
from .views import Hr_dashboard, Hr_login, Hr_registration
urlpatterns = [
    path('hrd/', Hr_dashboard),
    path('hrl/', Hr_login),
    path('hrr/', Hr_registration),
   
]
