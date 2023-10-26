from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),  # Define the login view
    path('signup/', views.signup_view, name='signup'),  # Define the signup view
]
