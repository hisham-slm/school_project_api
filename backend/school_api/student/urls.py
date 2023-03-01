from . import views
from django.urls import path

app_name = 'student'

urlpatterns = [
    path('',views.home, name='home'),
    path('profile/<int:stud_id>',views.profile, name='profile'),
    path('change_password/<int:stud_id>',views.change_password, name='change_password'),
]