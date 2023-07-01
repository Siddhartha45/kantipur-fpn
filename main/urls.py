from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    #forms path
    path('forms/namuna-bibaran', views.namuna_bibaran, name="namuna"),
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
    #details form path
    path('forms/details/anugaman/', views.detail_anugaman, name="detail-anugaman"),
    path('forms/details/gunasho/', views.detail_gunasho, name="detail-gunasho"),
    path('forms/details/hotel/', views.detail_hotel, name="detail-hotel"),
    path('forms/details/mudha/', views.detail_mudha, name="detail-mudha"),
    path('forms/details/rbpa/', views.detail_rbpa, name="detail-rbpa"),
    path('forms/details/registration/', views.detail_registration, name="detail-registration"),
    path('forms/details/renew/', views.detail_renew, name="detail-renew"),
    path('forms/details/udyog/', views.detail_udyog, name="detail-udyog"),
    #reports path
    path('report/khadya-act/', views.khadyaact_report, name="khadya-act-report"),
    path('report/anugaman/', views.anugaman_report, name="anugaman-report"),
    path('report/hotel/', views.hotel_report, name="hotel-report"),
    path('report/khadya/', views.khadya_report, name="khadya-report"),
    path('report/prayogsala/', views.prayogsala_report, name="prayogsala-report"),
    path('report/rbpa/', views.rbpa_report, name="rbpa-report"),
    path('report/import-export/', views.importexport_report, name="import-export-report"),
    path('report/gunasho/', views.gunasho_report, name="gunasho-report"),
    path('report/patrakar/', views.patrakar_report, name="patrakar-report"),
    path('report/patrajari/', views.patrajari_report, name="patrajari-report"),
    path('report/renew/', views.renew_report, name="renew-report"),
    path('report/udyog/', views.udyog_report, name="udyog-report"),
    path('report/finance/', views.finance_report, name="finance-report"),
    path('report/monthly/', views.monthly_report, name="monthly-report"),
    #edit path
    path('edit/khadyaact/<int:id>/', views.khadyaact_edit, name="namunabibaran-edit"),
    path('edit/anugaman/<int:id>/', views.anugaman_edit, name="anugaman-edit"),
    path('edit/hotel/<int:id>/', views.hotel_edit, name="hotel-edit"),
    path('edit/khadya/<int:id>/', views.khadya_edit, name="khadya-edit"),
    path('edit/prayogsala/<int:id>/', views.prayogsala_edit, name="prayogsala-edit"),
    path('edit/rbpa/<int:id>/', views.rbpa_edit, name="rbpa-edit"),
    path('edit/import-export/<int:id>/', views.importexport_edit, name="importexport-edit"),
    path('edit/gunasho/<int:id>/', views.gunasho_edit, name="gunasho-edit"),
    path('edit/patrakar/<int:id>/', views.patrakar_edit, name="patrakar-edit"),
    path('edit/patrajari/<int:id>/', views.patrajari_edit, name="patrajari-edit"),
    path('edit/renew/<int:id>/', views.renew_edit, name="renew-edit"),
    path('edit/udyog/<int:id>/', views.udyog_edit, name="udyog-edit"),
    path('edit/finance/<int:id>/', views.finance_edit, name="finance-edit"),
    path('edit/monthly/<int:id>/', views.monthly_edit, name="monthly-edit"),
    #delete path
    path('anugaman/delete/<int:id>/', views.anugaman_report_delete, name="anugaman-delete")
]