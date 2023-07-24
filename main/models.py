from django.db import models
from fpn import commons
from fpn.model_mixins import FPNBaseModel
from account.models import CustomUser


class BarsikLakshya(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="users")
    namuna_bibaran = models.PositiveIntegerField(default=0, blank=True)
    anugaman = models.PositiveIntegerField(default=0, blank=True)
    logo = models.PositiveIntegerField(default=0, blank=True)
    namuna_bisleysan = models.PositiveIntegerField(default=0, blank=True)
    prayogsala = models.PositiveIntegerField(default=0, blank=True)
    patrajari = models.PositiveIntegerField(default=0, blank=True)
    patranabikaran = models.PositiveIntegerField(default=0, blank=True)
    udyog_sifaris = models.PositiveIntegerField(default=0, blank=True)
    aayat_niryat = models.PositiveIntegerField(default=0, blank=True)
    ujuri_gunaso = models.PositiveIntegerField(default=0, blank=True)
    rbpr = models.PositiveIntegerField(default=0, blank=True)


class NamunaBibaran(FPNBaseModel):
    """model for खाद्य ऐन/नियम बमोजिम संकलित नमुना विवरण"""
    milk = models.PositiveIntegerField(default=0, blank=True)
    oil = models.PositiveIntegerField(default=0, blank=True)
    fruits = models.PositiveIntegerField(default=0, blank=True)
    spice = models.PositiveIntegerField(default=0, blank=True)
    tea = models.PositiveIntegerField(default=0, blank=True)
    salt = models.PositiveIntegerField(default=0, blank=True)
    khadanna = models.PositiveIntegerField(default=0, blank=True)
    water = models.PositiveIntegerField(default=0, blank=True)
    sweets = models.PositiveIntegerField(default=0, blank=True)
    confectionery = models.PositiveIntegerField(default=0, blank=True)
    meat = models.PositiveIntegerField(default=0, blank=True)
    grain = models.PositiveIntegerField(default=0, blank=True)
    others = models.PositiveIntegerField(default=0, blank=True)
    
    def namunabibaran_total_sum(self):
        fields = [
            'milk', 'oil', 'fruits', 'spice', 'tea', 'salt', 'khadanna',
            'water', 'sweets', 'confectionery', 'meat', 'grain', 'others',
        ]
        total_sum = sum(getattr(self, field) for field in fields)
        return total_sum
    
    
class AnugamanBibaran(FPNBaseModel):
    """model for निरीक्षण अनुगमन विवरण"""
    type = models.CharField(max_length=100, choices=commons.ANUGAMAN_CHOICES)
    patak = models.PositiveIntegerField(default=0, blank=True)
    sankhya = models.PositiveIntegerField(default=0, blank=True)
    pragati = models.PositiveIntegerField(default=0, blank=True)
    kaifiyat = models.TextField(default="", blank=True)
    
    def anugamanbibaran_total_sum(self):
        fields = [
            'patak', 'sankhya', 'pragati',
        ]
        total_sum = sum(getattr(self, field) for field in fields)
        return total_sum
    
    
class Logobitaran(FPNBaseModel):
    """model for होटल स्तरीकरण लोगो वितरण सम्बन्धि विवरण"""
    type = models.CharField(max_length=50, choices=commons.LOGO_CHOICES)
    c_pragati = models.PositiveIntegerField(default=0, blank=True)
    h_pragati1 = models.PositiveIntegerField(default=0, blank=True)
    h_pragati2 = models.PositiveIntegerField(default=0, blank=True)
    kaifiyat = models.TextField(default="", blank=True)
    
    def logobitaran_total_sum(self):
        fields = [
            'c_pragati', 'h_pragati1', 'h_pragati2',
        ]
        total_sum = sum(getattr(self, field) for field in fields)
        return total_sum
    
    
class NamunaBisleysan(FPNBaseModel):
    """model for खाद्य तथा दाना नमुना विश्लेषण विवरण"""
    type = models.CharField(max_length=100, choices=commons.TYPES_CHOICES)
    ekai = models.CharField(max_length=10, choices=commons.EKAI_CHOICES, blank=True)
    lakshya = models.PositiveIntegerField(default=0, blank=True)
    pragati1 = models.PositiveIntegerField(default=0, blank=True)
    mahina_pragati = models.PositiveIntegerField(default=0, blank=True)
    sankhya = models.PositiveIntegerField(default=0, blank=True)
    parameter = models.PositiveIntegerField(default=0, blank=True)
    pragati2 = models.PositiveIntegerField(default=0, blank=True)
    pratisat = models.FloatField(default=0, blank=True)
    kaifiyat = models.TextField(default="", blank=True)
    
    def namunabisleysan_total_sum(self):
        fields = [
            'lakshya', 'pragati1', 'mahina_pragati', 'sankhya',
            'parameter', 'pragati2', 'pratisat',
        ]
        total_sum = sum(getattr(self, field) for field in fields)
        return total_sum
    
    
class PrayogsalaBisleysan(FPNBaseModel):
    """model for प्रयोगशाला विश्लेषण प्रतिवेदन सारांश"""
    type = models.CharField(max_length=100, choices=commons.TYPES_CHOICES)
    b_sankhya = models.PositiveIntegerField(default=0, blank=True)
    b_pratikul = models.PositiveIntegerField(default=0, blank=True)
    u_sankhya = models.PositiveIntegerField(default=0, blank=True)
    u_pratikul = models.PositiveIntegerField(default=0, blank=True)
    ay_sankhya = models.PositiveIntegerField(default=0, blank=True)
    ay_pratikul = models.PositiveIntegerField(default=0, blank=True)
    v_sankhya = models.PositiveIntegerField(default=0, blank=True)
    v_pratikul = models.PositiveIntegerField(default=0, blank=True)
    k_sankhya = models.PositiveIntegerField(default=0, blank=True)
    k_pratikul = models.PositiveIntegerField(default=0, blank=True)
    a_sankhya = models.PositiveIntegerField(default=0, blank=True)
    a_pratikul = models.PositiveIntegerField(default=0, blank=True)
    kul_sankhya = models.PositiveIntegerField(default=0, blank=True)
    kul_pratikul = models.PositiveIntegerField(default=0, blank=True)
    sample = models.PositiveIntegerField(default=0, blank=True)
    kaifiyat = models.TextField(default="", blank=True)
    
    def prayogsalabisleysan_total_sum(self):
        fields = [
            'b_sankhya', 'b_pratikul', 'u_sankhya', 'u_pratikul',
            'ay_sankhya', 'ay_pratikul', 'v_sankhya', 'v_pratikul',
            'k_sankhya', 'k_pratikul', 'a_sankhya', 'a_pratikul',
            'kul_sankhya', 'kul_pratikul', 'sample',
        ]
        total_sum = sum(getattr(self, field) for field in fields)
        return total_sum
    
    
class PatraJari(FPNBaseModel):
    """model for खाद्य तथा दाना अनुज्ञा पत्र जारी"""
    milk = models.PositiveIntegerField(default=0, blank=True)
    oil = models.PositiveIntegerField(default=0, blank=True)
    fruits = models.PositiveIntegerField(default=0, blank=True)
    spice = models.PositiveIntegerField(default=0, blank=True)
    tea = models.PositiveIntegerField(default=0, blank=True)
    salt = models.PositiveIntegerField(default=0, blank=True)
    khadanna = models.PositiveIntegerField(default=0, blank=True)
    water = models.PositiveIntegerField(default=0, blank=True)
    sweets = models.PositiveIntegerField(default=0, blank=True)
    confectionery = models.PositiveIntegerField(default=0, blank=True)
    meat = models.PositiveIntegerField(default=0, blank=True)
    grain = models.PositiveIntegerField(default=0, blank=True)
    others = models.PositiveIntegerField(default=0, blank=True)
    
    def patrajari_total_sum(self):
        fields = [
            'milk', 'oil', 'fruits', 'spice',
            'tea', 'salt', 'khadanna', 'water',
            'sweets', 'confectionery', 'meat', 'grain',
            'others',
        ]
        total_sum = sum(getattr(self, field) for field in fields)
        return total_sum
    
    
class PatraNabikaran(FPNBaseModel):
    """model for खाद्य तथा दाना अनुज्ञा पत्र नविकरण"""
    milk = models.PositiveIntegerField(default=0, blank=True)
    oil = models.PositiveIntegerField(default=0, blank=True)
    fruits = models.PositiveIntegerField(default=0, blank=True)
    spice = models.PositiveIntegerField(default=0, blank=True)
    tea = models.PositiveIntegerField(default=0, blank=True)
    salt = models.PositiveIntegerField(default=0, blank=True)
    khadanna = models.PositiveIntegerField(default=0, blank=True)
    water = models.PositiveIntegerField(default=0, blank=True)
    sweets = models.PositiveIntegerField(default=0, blank=True)
    confectionery = models.PositiveIntegerField(default=0, blank=True)
    meat = models.PositiveIntegerField(default=0, blank=True)
    grain = models.PositiveIntegerField(default=0, blank=True)
    others = models.PositiveIntegerField(default=0, blank=True)
    
    def patranabikaran_total_sum(self):
        fields = [
            'milk', 'oil', 'fruits', 'spice',
            'tea', 'salt', 'khadanna', 'water',
            'sweets', 'confectionery', 'meat', 'grain',
            'others',
        ]
        total_sum = sum(getattr(self, field) for field in fields)
        return total_sum
    
    
class UdyogSifaris(FPNBaseModel):
    """model for उद्योग सिफारिस"""
    milk = models.PositiveIntegerField(default=0, blank=True)
    oil = models.PositiveIntegerField(default=0, blank=True)
    fruits = models.PositiveIntegerField(default=0, blank=True)
    spice = models.PositiveIntegerField(default=0, blank=True)
    tea = models.PositiveIntegerField(default=0, blank=True)
    salt = models.PositiveIntegerField(default=0, blank=True)
    khadanna = models.PositiveIntegerField(default=0, blank=True)
    water = models.PositiveIntegerField(default=0, blank=True)
    sweets = models.PositiveIntegerField(default=0, blank=True)
    confectionery = models.PositiveIntegerField(default=0, blank=True)
    meat = models.PositiveIntegerField(default=0, blank=True)
    grain = models.PositiveIntegerField(default=0, blank=True)
    others = models.PositiveIntegerField(default=0, blank=True)
    
    def udyogsifaris_total_sum(self):
        fields = [
            'milk', 'oil', 'fruits', 'spice',
            'tea', 'salt', 'khadanna', 'water',
            'sweets', 'confectionery', 'meat', 'grain',
            'others',
        ]
        total_sum = sum(getattr(self, field) for field in fields)
        return total_sum
    
    
class AayatNiryat(FPNBaseModel):
    """model for आयात निर्यात गुण प्रमाणिकरण"""
    type = models.CharField(max_length=100, choices=commons.TYPES_CHOICES)
    ekai = models.CharField(max_length=10, choices=commons.EKAI_CHOICES, blank=True)
    b_lakshya = models.PositiveIntegerField(default=0, blank=True)
    c_lakshya = models.PositiveIntegerField(default=0, blank=True)
    c_pragati = models.PositiveIntegerField(default=0, blank=True)
    m_pragati = models.PositiveIntegerField(default=0, blank=True)
    pratikul_n = models.PositiveIntegerField(default=0, blank=True)
    pratikul_p = models.PositiveIntegerField(default=0, blank=True)
    h_pragati = models.PositiveIntegerField(default=0, blank=True)
    h_pratisat = models.PositiveIntegerField(default=0, blank=True)
    kaifiyat = models.TextField(default="", blank=True)
    
    def aayatniryat_total_sum(self):
        fields = [
            'b_lakshya', 'c_lakshya', 'c_pragati', 'm_pragati',
            'pratikul_n', 'pratikul_p', 'h_pragati', 'h_pratisat',
        ]
        total_sum = sum(getattr(self, field) for field in fields)
        return total_sum    


class UjuriGunaso(FPNBaseModel):
    """model for उजुरी/गुनासो ब्येवस्थापन"""
    gunaso_petika = models.PositiveIntegerField(default=0, blank=True)
    gunaso_adhikari = models.PositiveIntegerField(default=0, blank=True)
    zilla = models.PositiveIntegerField(default=0, blank=True)
    banijya = models.PositiveIntegerField(default=0, blank=True)
    patra = models.PositiveIntegerField(default=0, blank=True)
    akhtiyar = models.PositiveIntegerField(default=0, blank=True)
    patrakar = models.PositiveIntegerField(default=0, blank=True)
    sarkar = models.PositiveIntegerField(default=0, blank=True)
    upavokta = models.PositiveIntegerField(default=0, blank=True)
    others = models.PositiveIntegerField(default=0, blank=True)
    jamma = models.PositiveIntegerField(default=0, blank=True)
    sambodhan = models.PositiveIntegerField(default=0, blank=True)
    
    def ujurigunaso_total_sum(self):
        fields = [
            'gunaso_petika', 'gunaso_adhikari', 'zilla', 'banijya',
            'patra', 'akhtiyar', 'patrakar', 'sarkar', 'upavokta',
            'others', 'jamma', 'sambodhan',
        ]
        total_sum = sum(getattr(self, field) for field in fields)
        return total_sum
    
    
class KhadyaPrasodhan(FPNBaseModel):
    """model for खाद्य प्रसोधन, खाद्य पोषण, उद्योग, होटेल, पत्रकार, कार्यशाला आदि"""
    miti= models.CharField(max_length=10, blank=True, null=True)
    abadhi = models.CharField(max_length=255, default="", blank=True)
    naam = models.CharField(max_length=255, default="", blank=True)
    sthan = models.CharField(max_length=255, default="", blank=True)
    m_sankhya = models.PositiveIntegerField(default=0, blank=True)
    p_sankhya = models.PositiveIntegerField(default=0, blank=True)
    sanyojak = models.CharField(max_length=255, default="", blank=True)
    phone = models.CharField(max_length=15, default="", blank=True)
    prasikshak = models.CharField(max_length=255, default="", blank=True)
    nikaya = models.TextField(default="", blank=True)
    bisaya = models.TextField(default="", blank=True)
    kaifiyat = models.TextField(default="", blank=True)
    
    def khadyaprasodhan_total_sum(self):
        fields = [
            'm_sankhya', 'p_sankhya',
        ]
        total_sum = sum(getattr(self, field) for field in fields)
        return total_sum


class BittiyaBibaran(FPNBaseModel):
    """model for मासिक वित्तिय विवरण"""
    yearly_pujigat = models.FloatField(default=0, blank=True)
    yearly_chalu = models.FloatField(default=0, blank=True)
    monthly_pujigat = models.FloatField(default=0, blank=True)
    monthly_chalu= models.FloatField(default=0, blank=True)
    monthly_rajaswo = models.FloatField(default=0, blank=True)
    
    def bittiyabibaran_total_sum(self):
        fields = [
            'yearly_pujigat', 'yearly_chalu', 'monthly_pujigat', 'monthly_chalu', 'monthly_rajaswo',
        ]
        total_sum = sum(getattr(self, field) for field in fields)
        return total_sum


class PragatiBibaran(FPNBaseModel):
    """model for मासिक प्रगति विवरण"""
    months = models.CharField(max_length=10, choices=commons.MONTHS_CHOICES, blank=True)
    kharcha_type = models.CharField(max_length=10, choices=commons.KHARCHA_CHOICES, blank=True)
    upasirshak = models.CharField(max_length=50, default="", blank=True)
    karya = models.CharField(max_length=255, default="", blank=True)
    ekai = models.CharField(max_length=10, choices=commons.EKAI_CHOICES, blank=True)
    b_lakshya = models.PositiveIntegerField(default=0, blank=True)
    m_parinam = models.PositiveIntegerField(default=0, blank=True)
    t_lakshya = models.PositiveIntegerField(default=0, blank=True)
    t_pragati = models.PositiveIntegerField(default=0, blank=True)
    t_pratisat = models.FloatField(default=0, blank=True)
    h_pragati = models.PositiveIntegerField(default=0, blank=True)
    h_pratisat = models.FloatField(default=0, blank=True)
    kaifiyat = models.TextField(default="", blank=True)
    
    def pragatibibaran_total_sum(self):
        fields = [
            'b_lakshya', 'm_parinam', 't_lakshya', 't_pragati', 't_pratisat', 'h_pragati', 'h_pratisat',
        ]
        total_sum = sum(getattr(self, field) for field in fields)
        return total_sum


#Details Models


class DetailHotel(FPNBaseModel):
    """model for detail होटल रेष्टुरेण्टको स्तरकिरण लोगो वितरण"""
    naam = models.CharField(max_length=255, default="", blank=True)
    logo = models.CharField(max_length=10, choices=commons.DETAIL_LOGO_CHOICES, blank=True)
    thegana = models.CharField(max_length=255, default="", blank=True)
    samparka = models.CharField(max_length=255, default="", blank=True)
    jilla = models.CharField(max_length=255, default="", blank=True)
    j_miti = models.CharField(max_length=10, default="", blank=True)
    n_miti = models.CharField(max_length=10, default="", blank=True)
    karyalaya = models.CharField(max_length=255, default="", blank=True)
    kaifiyat = models.TextField(default="", blank=True)
    
    
class DetailRegistration(FPNBaseModel):
    """model for detail अनुज्ञापत्र जारी"""
    samuha = models.CharField(max_length=10, choices=commons.DETAIL_SAMUHA_CHOICES, blank=True)
    naam = models.CharField(max_length=255, default="", blank=True)
    thegana = models.CharField(max_length=255, default="", blank=True)
    byakti = models.CharField(max_length=255, default="", blank=True)
    samparka = models.CharField(max_length=15, default="", blank=True)
    jilla = models.CharField(max_length=255, default="", blank=True)
    mukhya = models.CharField(max_length=255, default="", blank=True)
    brand = models.CharField(max_length=255, default="", blank=True)
    karyalaya = models.CharField(max_length=255, default="", blank=True)
    j_miti = models.CharField(max_length=10, default="", blank=True)
    n_miti = models.CharField(max_length=10, default="", blank=True)
    kaifiyat = models.TextField(default="", blank=True) 
    
    
class DetailRenew(FPNBaseModel):
    """model for detail अनुज्ञापत्र नवकिरण"""
    samuha = models.CharField(max_length=10, choices=commons.DETAIL_SAMUHA_CHOICES, blank=True)
    naam = models.CharField(max_length=255, default="", blank=True)
    thegana = models.CharField(max_length=255, default="", blank=True)
    byakti = models.CharField(max_length=255, default="", blank=True)
    samparka = models.CharField(max_length=15, default="", blank=True)
    jilla = models.CharField(max_length=255, default="", blank=True)
    mukhya = models.CharField(max_length=255, default="", blank=True)
    brand = models.CharField(max_length=255, default="", blank=True)
    karyalaya = models.CharField(max_length=255, default="", blank=True)
    j_miti = models.CharField(max_length=10, default="", blank=True)
    n_miti = models.CharField(max_length=10, default="", blank=True)
    kaifiyat = models.TextField(default="", blank=True)
    
    
class DetailUdyog(FPNBaseModel):
    """अmodel for detail उद्योग सिफारिस"""
    samuha = models.CharField(max_length=10, choices=commons.DETAIL_SAMUHA_CHOICES, blank=True)
    naam = models.CharField(max_length=255, default="", blank=True)
    thegana = models.CharField(max_length=255, default="", blank=True)
    byakti = models.CharField(max_length=255, default="", blank=True)
    samparka = models.CharField(max_length=15, default="", blank=True)
    jilla = models.CharField(max_length=255, default="", blank=True)
    mukhya = models.CharField(max_length=255, default="", blank=True)
    brand = models.CharField(max_length=255, default="", blank=True)
    karyalaya = models.CharField(max_length=255, default="", blank=True)
    j_miti = models.CharField(max_length=10, default="", blank=True)
    n_miti = models.CharField(max_length=10, default="", blank=True)
    kaifiyat = models.TextField(default="", blank=True)
    
    
class DetailAnugaman(FPNBaseModel):
    """model for detail अनुगमन निरीक्षण"""
    nirichad = models.CharField(max_length=100, choices=commons.DETAIL_ANUGAMAN_CHOICES, blank=True)
    miti = models.DateField(blank=True)
    naam = models.CharField(max_length=255, default="", blank=True)
    thegana = models.CharField(max_length=255, default="", blank=True)
    nikaya = models.CharField(max_length=255, default="", blank=True)
    a_bibaran = models.CharField(max_length=255, default="", blank=True)
    silbandi = models.CharField(max_length=255, default="", blank=True)
    parinam = models.CharField(max_length=255, default="", blank=True)
    mulya = models.CharField(max_length=255, default="", blank=True)
    nirdesan = models.CharField(max_length=255, default="", blank=True)
    d_bibaran = models.CharField(max_length=255, default="", blank=True)
    kaifiyat = models.CharField(max_length=255, default="", blank=True)
    
    
class DetailMudha(FPNBaseModel):
    """model for detail मुद्धा दायरी"""
    naam = models.CharField(max_length=255, default="", blank=True)
    b_naam = models.CharField(max_length=255, default="", blank=True)
    n_miti = models.CharField(max_length=10, default="", blank=True)
    n_sthan = models.CharField(max_length=255, default="", blank=True)
    n_khani = models.CharField(max_length=255, default="", blank=True)
    p_miti = models.CharField(max_length=10, default="", blank=True)
    b_miti = models.CharField(max_length=10, default="", blank=True)
    prakar = models.CharField(max_length=255, default="", blank=True)
    parameter = models.CharField(max_length=255, default="", blank=True)
    m_sthan = models.CharField(max_length=255, default="", blank=True)
    m_miti = models.CharField(max_length=10, default="", blank=True)
    m_khani = models.CharField(max_length=255, default="", blank=True)
    karyalaya = models.CharField(max_length=255, default="", blank=True)
    kaifiyat = models.TextField(default="", blank=True)    


class DetailRbpa(FPNBaseModel):
    """model for detail RBPA Analysis"""
    date = models.DateField(blank=True)
    commodity1 = models.CharField(max_length=255, default="", blank=True)
    sample1 = models.PositiveIntegerField(default=0, blank=True)
    quantity1 = models.PositiveIntegerField(default=0, blank=True)
    sample2 = models.PositiveIntegerField(default=0, blank=True)
    quantity2 = models.PositiveIntegerField(default=0, blank=True)
    commodity2 = models.CharField(max_length=255, default="", blank=True)
    sample3 = models.PositiveIntegerField(default=0, blank=True)
    quantity3 = models.PositiveIntegerField(default=0, blank=True)
    commodity3 = models.CharField(max_length=255, default="", blank=True)
    
    def rbpa_total_sum(self):
        fields = [
            'sample1', 'quantity1', 'sample2', 'quantity2', 'sample3', 'quantity3',
        ]
        total_sum = sum(getattr(self, field) for field in fields)
        return total_sum


class DetailGunaso(FPNBaseModel):
    """model for detail उजुरी गुनासो"""
    p_miti = models.CharField(max_length=10, default="", blank=True)
    srot = models.CharField(max_length=10, choices=commons.DETAIL_SROT_CHOICES, blank=True)
    s_miti = models.CharField(max_length=10, default="", blank=True)
    bibaran = models.TextField(default="", blank=True)

