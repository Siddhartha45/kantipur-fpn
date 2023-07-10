from django.contrib import admin
from .models import (BarsikLakshya, NamunaBibaran, PatraJari, PatraNabikaran, UdyogSifaris, UjuriGunaso, BittiyaBibaran, AnugamanBibaran,
                    NamunaBisleysan, AayatNiryat, PrayogsalaBisleysan, Logobitaran, KhadyaPrasodhan, PragatiBibaran,
                    DetailHotel, DetailRegistration, DetailRenew, DetailUdyog, DetailAnugaman, DetailGunaso, DetailMudha, DetailRbpa)
# Register your models here.

admin.site.register(BarsikLakshya)
#admin.site.register(NamunaBibaran)
admin.site.register(PatraJari)
admin.site.register(PatraNabikaran)
admin.site.register(UdyogSifaris)
admin.site.register(UjuriGunaso)
admin.site.register(BittiyaBibaran)
#admin.site.register(AnugamanBibaran)
admin.site.register(NamunaBisleysan)
admin.site.register(AayatNiryat)
admin.site.register(PrayogsalaBisleysan)
admin.site.register(Logobitaran)
admin.site.register(KhadyaPrasodhan)
admin.site.register(PragatiBibaran)

admin.site.register(DetailHotel)
admin.site.register(DetailRegistration)
admin.site.register(DetailRenew)
admin.site.register(DetailUdyog)
admin.site.register(DetailAnugaman)
admin.site.register(DetailGunaso)
admin.site.register(DetailMudha)
admin.site.register(DetailRbpa)


@admin.register(AnugamanBibaran)
class AnugamanBibaranModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_office', 'created_by', 'get_category']
    
    def get_office(self, obj):
        return obj.created_by.office
    
    def get_category(self, obj):
        return obj.created_by.department_category
    
    
@admin.register(NamunaBibaran)
class NamunaBibaranModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_office', 'created_by', 'get_category']
    
    def get_office(self, obj):
        return obj.created_by.office
    
    def get_category(self, obj):
        return obj.created_by.department_category