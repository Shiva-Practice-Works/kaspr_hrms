#dev Shiva gangula

from django.urls import path ,include
from integration.views import *
urlpatterns = [
    path('rhrmsg/',hr_student_conversions,name='hr_student_conversions'),
    path('hrside/',hr_request_accept_reject,name='hr_request_accept_reject'),
]
