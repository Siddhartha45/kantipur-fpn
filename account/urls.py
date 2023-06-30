from django.urls import path
from . import views

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
    #office
    path('office/create/', views.create_office, name="office-create"),
    path('office/list/', views.office_list, name="office-list"),
    path('office/edit/<int:id>/', views.office_edit, name="office-edit"),
    path('office/delete/<int:id>/', views.office_delete, name="office-delete"),
    
    path('count/', views.progress_count, name="count"),
    path('amount/', views.progress_amount, name="amount"),
]