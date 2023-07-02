from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import CustomPasswordResetView


urlpatterns = [
    #authentication
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="logout"),
    #user
    path('user/create/', views.user_create, name="user-create"),
    path('user/display/', views.user_list, name="user-list"),
    path('user/profile/<int:user_id>/', views.user_profile, name="user-profile"),
    path('user/edit/<int:id>/', views.user_edit, name="user-edit"),
    path('user/delete/<int:id>/', views.user_delete, name="user-delete"),
    path('user/password-change/<int:id>', views.password_change, name="password-change"),
    #office
    path('office/create/', views.create_office, name="office-create"),
    path('office/list/', views.office_list, name="office-list"),
    path('office/edit/<int:id>/', views.office_edit, name="office-edit"),
    path('office/delete/<int:id>/', views.office_delete, name="office-delete"),
    
    path('count/', views.progress_count, name="count"),
    path('amount/', views.progress_amount, name="amount"),
    #url paths for password resetting    
    path('password_reset/',CustomPasswordResetView.as_view(template_name='user/forgetpassword.html'), name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='user/resetpassword.html'), name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]