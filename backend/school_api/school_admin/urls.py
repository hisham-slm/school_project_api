from . import views
from django.urls import path

app_name = 'admin'

urlpatterns = [
    path('login',views.admin_login, name='admin_login'),
    path('view_student',views.view_student, name='view_student'),
    path('view_teacher',views.view_teacher, name='view_teacher'),
    path('add_teacher',views.add_teacher, name='add_teacher'),

]