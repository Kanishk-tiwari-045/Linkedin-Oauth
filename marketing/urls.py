from django.urls import path
from . import views

urlpatterns = [
    path('org/create', views.OrganizationView, name='create-organization'),
    path('org/verify', views.VerifyOTPView, name='verify-')
    path('job/create', views.JobView, name='create-job'),
]