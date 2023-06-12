from django.db import models
from fpn import commons


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
    
    
class BittiyaBibaran(models.Model):
    """model for मासिक वित्तिय विवरण"""
    yearly_pujigat = models.FloatField(default=0, blank=True)
    yearly_chalu = models.FloatField(default=0, blank=True)
    monthly_pujigat = models.FloatField(default=0, blank=True)
    monthly_chalu= models.FloatField(default=0, blank=True)
    monthly_rajaswo = models.FloatField(default=0, blank=True)
    
    
class AnugamanBibaran(models.Model):
    """model for निरीक्षण अनुगमन विवरण"""
    type = models.CharField(max_length=100, choices=commons.ANUGAMAN_CHOICES)
    patak = models.PositiveIntegerField(default=0, blank=True)
    sankhya = models.PositiveIntegerField(default=0, blank=True)
    pragati = models.PositiveIntegerField(default=0, blank=True)
    kaifiyat = models.TextField(default="", blank=True)
    
    
class NamunaBisleysan(models.Model):
    """model for खाद्य तथा दाना नमुना विश्लेषण विवरण"""
    type = models.CharField(max_length=100, choices=commons.NAMUNA_BISLEYSAN_CHOICES)
    ekai = models.CharField(max_length=10, choices=commons.EKAI_CHOICES, blank=True)
    lakshya = models.PositiveIntegerField(default=0, blank=True)
    pragati1 = models.PositiveIntegerField(default=0, blank=True)
    mahina_pragati = models.PositiveIntegerField(default=0, blank=True)
    sankhya = models.PositiveIntegerField(default=0, blank=True)
    parameter = models.PositiveIntegerField(default=0, blank=True)
    pragati2 = models.PositiveIntegerField(default=0, blank=True)
    pratisat = models.FloatField(default=0, blank=True)
    kaifiyat = models.TextField(default="", blank=True)