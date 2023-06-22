from django.db import models
from fpn import commons
import nepali_datetime
from datetime import date
from django.utils import timezone


class NamunaBibaran(models.Model):
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
    
    
class AnugamanBibaran(models.Model):
    """model for निरीक्षण अनुगमन विवरण"""
    type = models.CharField(max_length=100, choices=commons.ANUGAMAN_CHOICES)
    patak = models.PositiveIntegerField(default=0, blank=True)
    sankhya = models.PositiveIntegerField(default=0, blank=True)
    pragati = models.PositiveIntegerField(default=0, blank=True)
    kaifiyat = models.TextField(default="", blank=True)
    
    
class Logobitaran(models.Model):
    """model for होटल स्तरीकरण लोगो वितरण सम्बन्धि विवरण"""
    type = models.CharField(max_length=50, choices=commons.LOGO_CHOICES)
    c_pragati = models.PositiveIntegerField(default=0, blank=True)
    h_pragati1 = models.PositiveIntegerField(default=0, blank=True)
    h_pragati2 = models.PositiveIntegerField(default=0, blank=True)
    kaifiyat = models.TextField(default="", blank=True)
    
    
class NamunaBisleysan(models.Model):
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
    
    
class PrayogsalaBisleysan(models.Model):
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
    
    
class PatraJari(models.Model):
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
    
    
class PatraNabikaran(models.Model):
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
    
    
class UdyogSifaris(models.Model):
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
    
    
class AayatNiryat(models.Model):
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


class UjuriGunaso(models.Model):
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
    
    
class KhadyaPrasodhan(models.Model):
    """model for खाद्य प्रसोधन, खाद्य पोषण, उद्योग, होटेल, पत्रकार, कार्यशाला आदि"""
    miti= models.DateField(blank=True, null=True)
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
    


class BittiyaBibaran(models.Model):
    """model for मासिक वित्तिय विवरण"""
    yearly_pujigat = models.FloatField(default=0, blank=True)
    yearly_chalu = models.FloatField(default=0, blank=True)
    monthly_pujigat = models.FloatField(default=0, blank=True)
    monthly_chalu= models.FloatField(default=0, blank=True)
    monthly_rajaswo = models.FloatField(default=0, blank=True)
    
    
class PragatiBibaran(models.Model):
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
    
    
# class MasikPragati(models.Model):
#     """model for मासिक वित्तिय विवरण"""
#     upasirshak = models.PositiveIntegerField(default=0, blank=True)
#     karyakram = models.CharField(max_length=255, default="", blank=True)
#     ekai = models.CharField(max_length=15, choices=commons.EKAI_CHOICES, blank=True)
#     b_lakshya = models.PositiveIntegerField(default=0, blank=True)
#     m_parina = models.PositiveIntegerField(default=0, blank=True)
#     t_lakshya = models.PositiveIntegerField(default=0, blank=True)
#     t_pragati = models.PositiveIntegerField(default=0, blank=True)
#     t_pratisat = models.PositiveIntegerField(default=0, blank=True)
#     h_parinam = models.PositiveIntegerField(default=0, blank=True)
#     h_pratisat = models.PositiveIntegerField(default=0, blank=True)
#     kaifiyat = models.TextField(default="", blank=True)




#Details Models

class DetailHotel(models.Model):
    """model for detail होटल रेष्टुरेण्टको स्तरकिरण लोगो वितरण"""
    naam = models.CharField(max_length=255, default="", blank=True)
    logo = models.CharField(max_length=10, choices=commons.DETAIL_LOGO_CHOICES, blank=True)
    thegana = models.CharField(max_length=255, default="", blank=True)
    samparka = models.CharField(max_length=255, default="", blank=True)
    jilla = models.CharField(max_length=255, default="", blank=True)
    j_miti = models.DateField(blank=True)
    n_miti = models.DateField(blank=True)
    karyalaya = models.CharField(max_length=255, default="", blank=True)
    kaifiyat = models.TextField(default="", blank=True)
    
    
class DetailRegistration(models.Model):
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
    j_miti = models.DateField(blank=True)
    n_miti = models.DateField(blank=True)
    kaifiyat = models.TextField(default="", blank=True) 
    
    
class DetailRenew(models.Model):
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
    j_miti = models.DateField(blank=True)
    n_miti = models.DateField(blank=True)
    kaifiyat = models.TextField(default="", blank=True)
    
    
class DetailUdyog(models.Model):
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
    j_miti = models.DateField(blank=True)
    n_miti = models.DateField(blank=True)
    kaifiyat = models.TextField(default="", blank=True)
    
    
class DetailAnugaman(models.Model):
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
    
    
class DetailMudha(models.Model):
    """model for detail मुद्धा दायरी"""
    naam = models.CharField(max_length=255, default="", blank=True)
    b_naam = models.CharField(max_length=255, default="", blank=True)
    n_miti = models.DateField(blank=True)
    n_sthan = models.CharField(max_length=255, default="", blank=True)
    n_khani = models.CharField(max_length=255, default="", blank=True)
    p_miti = models.DateField(blank=True)
    b_miti = models.DateField(blank=True)
    prakar = models.CharField(max_length=255, default="", blank=True)
    parameter = models.CharField(max_length=255, default="", blank=True)
    m_sthan = models.CharField(max_length=255, default="", blank=True)
    m_miti = models.DateField(blank=True)
    m_khani = models.CharField(max_length=255, default="", blank=True)
    karyalaya = models.CharField(max_length=255, default="", blank=True)
    kaifiyat = models.TextField(default="", blank=True)    


class DetailRbpa(models.Model):
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


class DetailGunaso(models.Model):
    """model for detail उजुरी गुनासो"""
    p_miti = models.DateField(blank=True)
    srot = models.CharField(max_length=10, choices=commons.DETAIL_SROT_CHOICES, blank=True)
    s_miti = models.DateField(blank=True)
    bibaran = models.TextField(default="", blank=True)

