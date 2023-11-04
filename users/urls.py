import os, sys
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from users.views import MyPasswordResetView, MyPasswordResetCompleteView, MyPasswordResetConfirmView, MyPasswordResetDoneView, RegisterView, ProfileView, EmailConfirmationView
sys.path.append(os.getcwd())


from django.urls import path, reverse_lazy
from users.apps import UsersConfig

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name = "users/login.html"), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('register/', RegisterView.as_view(), name='register'),
    path('register/confirm/', EmailConfirmationView.as_view(), name='email_confirmation'),

    path('profile/', ProfileView.as_view(), name='profile'),

    path('password_reset/', MyPasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', MyPasswordResetDoneView.as_view(), name='password_reset_done'), 
    path('password_reset_confirm/<uidb64>/<token>/', MyPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/', MyPasswordResetCompleteView.as_view(), name='password_reset_complete'),


]

