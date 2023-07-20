from django.urls import path
from . import views


urlpatterns = [
    #table list for details part form
    path('report/detail/hotel/', views.detail_hotel_report, name="detail-hotel"),
    path('report/detail/anugaman/', views.detail_anugaman_report, name="detail-anugaman"),
    path('report/detail/gunaso/', views.detail_gunaso_report, name="detail-gunaso"),
    path('report/detail/mudha/', views.detail_mudha_report, name="detail-mudha"),
    path('report/detail/registration/', views.detail_registration_report, name="detail-registration"),
    path('report/detail/renew/', views.detail_renew_report, name="detail-renew"),
    path('report/detail/udyog/', views.detail_udyog_report, name="detail-udyog"),
]
