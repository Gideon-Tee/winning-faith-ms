from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('enroll', views.enroll, name='enroll'),
    path('students', views.display_students, name='students'),
    path('new_class', views.add_new_class, name='add_new_class'),
    path('classes', views.display_classes, name='classes'),
    path('settings', views.settings, name='settings')
]