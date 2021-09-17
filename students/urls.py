from django.urls import path
from students.views import Home, Marksheet

urlpatterns = [
    path('home', Home.as_view(), name='home'),
    path('marks2/<str:Name>', Marksheet.as_view(), name='marks2'),
    ]