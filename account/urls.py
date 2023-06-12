from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="logout"),
    
    path('user/create/', views.user_create, name="user-create"),
    path('user/display/', views.user_list, name="user-list"),
    path('user/profile/<int:user_id>/', views.user_profile, name="user-profile"),
    
    
]