from django.urls import path
from . import views


urlpatterns = [
    #path('', views.home, name="home"),
    
    path('', views.namuna_bibaran, name="namuna"),
    path('forms/anugaman-bibaran/', views.anugaman, name="anugaman"),
    path('forms/logobitaran/', views.logobitaran, name="logobitaran"),
    path('forms/namuna-bisleysan/', views.namuna_bisleysan, name="namuna-bisleysan"),
    path('forms/prayogsala-bisleysan/', views.prayogsala_bisleysan, name="prayogsala-bisleysan"),
    path('forms/khadya-patrajari/', views.khadya1, name="khadya1"),
    path('forms/khadya-nabikaran/', views.khadya2, name="khadya2"),
    path('forms/udyog/', views.udyog, name="udyog"),
    path('forms/aayat/', views.aayat, name="aayat"),
    path('forms/ujuri/', views.ujuri, name="ujuri"),
    path('forms/khadya-prasodhan/', views.khadya_prasodhan, name="khadya-prasodhan"),
    path('forms/masik-bittiya/', views.masik_bittiya, name="masik-bittiya"),
    path('forms/masik-pragati/', views.masik_pragati, name="masik-pragati"),
    
    #details
    path('forms/details/anugaman/', views.detail_anugaman, name="detail-anugaman"),
    path('forms/details/gunasho/', views.detail_gunasho, name="detail-gunasho"),
    path('forms/details/hotel/', views.detail_hotel, name="detail-hotel"),
    path('forms/details/mudha/', views.detail_mudha, name="detail-mudha"),
    path('forms/details/rbpa/', views.detail_rbpa, name="detail-rbpa"),
    path('forms/details/registration/', views.detail_registration, name="detail-registration"),
    path('forms/details/renew/', views.detail_renew, name="detail-renew"),
    path('forms/details/udyog/', views.detail_udyog, name="detail-udyog"),
    
    
    #report
    path('report/anugaman/', views.anugaman_report, name="anugaman-report"),
]