from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.account_home, name='account_home'),
    path('login/',views.login_view, name='login_view'),
    path('register',views.register_view, name='register_view'),
    path('logout', views.logoutUser, name="logoutUser"),
     path('profile',views.profile_view, name='profile_view'),
    path('changepassword',views.userchangepass, name='userchangepass'),

     #==Reset-Password========================================#
    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="account/forget-temp/password_reset.html"), name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="account/forget-temp/password_reset_sent.html"), name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="account/forget-temp/password_reset_form.html"), name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="account/forget-temp/password_reset_done.html"), name="password_reset_complete"),

] 