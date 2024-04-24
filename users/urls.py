from django.urls import path
from . import views
from django.contrib.auth import views as vw

 
urlpatterns = [
     path('', views.index, name="index"),
     path("login/", views.user_login, name="login"),
     path('logout/', views.logout_view, name='logout'),   
     path('password_change/', vw.PasswordChangeView.as_view(template_name="users/password_reset_form.html"), name="password_change"),
     path('password_change/done/',vw.PasswordChangeDoneView.as_view(template_name="users/password_change_done.html"), name="password_change_done"),
     path('password_reset/', vw.PasswordResetView.as_view(template_name="users/password_forgot_form.html"), name="password_reset"),
     path('password_reset_confirm/', vw.PasswordResetDoneView.as_view(template_name="users/password_forgot_done.html"), name='password_reset_done'),
     path('reset/<uidb64>/<token>/', vw.PasswordResetConfirmView.as_view(template_name="users/password_reset_confirm.html"), name="password_reset_confirm"),
     path('reset/done', vw.PasswordResetCompleteView.as_view(template_name="users/password_reset_done.html"), name="password_reset_complete"),
     path('register/', views.RegisterPage, name="Register"),
     path('edit/', views.edit, name='edit'),
 ] 
