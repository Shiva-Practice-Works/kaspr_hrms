#dev Shiva gangula

from django.urls import path ,include
from student_managment import views
urlpatterns = [
    path('',views.student_register,name='student_register'),
    path('student_register_details/',views.student_register,name='student_register_details'),
    path('student_login/',views.student_login,name='student_login'),
    path('student_login_details/',views.student_login,name='student_login_details'),
    
]
