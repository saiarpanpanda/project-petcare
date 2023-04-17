
from django.urls import path, re_path
from . import views
from django.urls import reverse


urlpatterns = [

    re_path('^$', views.login_view, name='login'),
    path('login/', views.login_view, name='login'),
    path('main/', views.main_view, name='main'),
    path('register/', views.register_view, name='register'),
    path('blood_report/', views.blood_report, name='blood_report'),
    path('search_results/', views.search_results , name='search_results'),
    path('dog_patient_detail/<int:registration_no>/', views.dog_patient_detail, name='dog_patient_detail'),

]


