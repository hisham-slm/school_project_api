from . import views
from django.urls import path

app_name = 'teacher'

urlpatterns = [
    path('',views.home, name='home'),
    path('add_student/',views.add_student, name='add_student'),
    path('view_student/',views.view_student, name='view_student'),
    path('change_password/<int:teacher_id>',views.change_password, name='change_password'),

]