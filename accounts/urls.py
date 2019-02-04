from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('novo-usuario/', views.add_user, name='add_user'),
    path('login/', views.user_login, name='user_login'),
    path('logout-usuario/', views.user_logout, name='user_logout'),
    path('alterar-senha/', views.change_password, name='change_password'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_don.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complet.html'), name='password_reset_complete'),
]