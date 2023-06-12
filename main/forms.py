from django import forms
from .models import (BittiyaBibaran, UjuriGunaso, NamunaBibaran, PatraJari, PatraNabikaran, UdyogSifaris,
                    )
from fpn import commons


class BaseModelForm(forms.ModelForm):
    """base model form with common clean method"""
    def clean(self):
        cleaned_data = super().clean()
        for field in self.Meta.model._meta.fields:
            if field.name in cleaned_data and cleaned_data[field.name] is None:
                cleaned_data[field.name] = field.default
        return cleaned_data


class BittiyaBibaranForm(BaseModelForm):
    """model form for मासिक वित्तिय विवरण"""
    class Meta:
        model = BittiyaBibaran
        fields = '__all__'


class PatraJariForm(BaseModelForm):
    """model form for खाद्य तथा दाना अनुज्ञा पत्र जारी"""
    class Meta:
        model = PatraJari
        fields = '__all__'
        

class PatraNabikaranForm(BaseModelForm):
    """model form for खाद्य तथा दाना अनुज्ञा पत्र नविकरण"""
    class Meta:
        model = PatraNabikaran
        fields = '__all__'
    

class UdyogSifarisForm(BaseModelForm):
    """model form for उद्योग सिफारिस"""
    class Meta:
        model = UdyogSifaris
        fields = '__all__'
    

class UjuriGunasoForm(BaseModelForm):
    """model form for उजुरी/गुनासो ब्येवस्थापन"""
    class Meta:
        model = UjuriGunaso
        fields = '__all__'
    
    
class NamunaBibaranForm(BaseModelForm):
    """model form for खाद्य ऐन/नियम बमोजिम संकलित नमुना विवरण"""
    class Meta:
        model = NamunaBibaran
        fields = '__all__'


class AnugamanBibaranForm(forms.Form):
    """form for निरीक्षण अनुगमन विवरण"""
    
    #udhyog
    u_patak = forms.IntegerField(required=False)
    u_sankhya = forms.IntegerField(required=False)
    u_pragati = forms.IntegerField(required=False)
    u_kaifiyat = forms.CharField(required=False)
    
    #pasal
    p_patak = forms.IntegerField(required=False)
    p_sankhya = forms.IntegerField(required=False)
    p_pragati = forms.IntegerField(required=False)
    p_kaifiyat = forms.CharField(required=False)
    
    #supermarket
    s_patak = forms.IntegerField(required=False)
    s_sankhya = forms.IntegerField(required=False)
    s_pragati = forms.IntegerField(required=False)
    s_kaifiyat = forms.CharField(required=False)
    
    #godam
    g_patak = forms.IntegerField(required=False)
    g_sankhya = forms.IntegerField(required=False)
    g_pragati = forms.IntegerField(required=False)
    g_kaifiyat = forms.CharField(required=False)
    
    #hotel
    h_patak = forms.IntegerField(required=False)
    h_sankhya = forms.IntegerField(required=False)
    h_pragati = forms.IntegerField(required=False)
    h_kaifiyat = forms.CharField(required=False)
    
    #dana
    d_patak = forms.IntegerField(required=False)
    d_sankhya = forms.IntegerField(required=False)
    d_pragati = forms.IntegerField(required=False)
    d_kaifiyat = forms.CharField(required=False)
    
    #anya
    a_patak = forms.IntegerField(required=False)
    a_sankhya = forms.IntegerField(required=False)
    a_pragati = forms.IntegerField(required=False)
    a_kaifiyat = forms.CharField(required=False)
    
    def clean(self):
        cleaned_data = super().clean()
        label = [
                'u_patak', 'u_sankhya', 'u_pragati', 
                'p_patak', 'p_sankhya', 'p_pragati', 
                's_patak', 's_sankhya', 's_pragati',
                'g_patak', 'g_sankhya', 'g_pragati',
                'h_patak', 'h_sankhya', 'h_pragati',
                'd_patak', 'd_sankhya', 'd_pragati',
                'a_patak', 'a_sankhya', 'a_pragati',
                ]
        for field_name in label:
            if field_name in cleaned_data and cleaned_data[field_name] is None:
                cleaned_data[field_name] = 0
                
                
class NamunaBisleysanForm(forms.Form):
    """form for खाद्य तथा दाना नमुना विश्लेषण विवरण"""
    
    #milk
    m_ekai = forms.ChoiceField(choices=commons.EKAI_CHOICES, required=False)
    m_lakshya = forms.IntegerField(required=False)
    m_pragati1 = forms.IntegerField(required=False)
    m_mahina_pragati = forms.IntegerField(required=False)
    m_sankhya = forms.IntegerField(required=False)
    m_parameter = forms.IntegerField(required=False)
    m_pragati2 = forms.IntegerField(required=False)
    m_pratisat = forms.FloatField(required=False)
    m_kaifiyat = forms.CharField(required=False)
    
    #oil
    o_ekai = forms.ChoiceField(choices=commons.EKAI_CHOICES, required=False)
    o_lakshya = forms.IntegerField(required=False)
    o_pragati1 = forms.IntegerField(required=False)
    o_mahina_pragati = forms.IntegerField(required=False)
    o_sankhya = forms.IntegerField(required=False)
    o_parameter = forms.IntegerField(required=False)
    o_pragati2 = forms.IntegerField(required=False)
    o_pratisat = forms.FloatField(required=False)
    o_kaifiyat = forms.CharField(required=False)
    
    #fruits
    f_ekai = forms.ChoiceField(choices=commons.EKAI_CHOICES, required=False)
    f_lakshya = forms.IntegerField(required=False)
    f_pragati1 = forms.IntegerField(required=False)
    f_mahina_pragati = forms.IntegerField(required=False)
    f_sankhya = forms.IntegerField(required=False)
    f_parameter = forms.IntegerField(required=False)
    f_pragati2 = forms.IntegerField(required=False)
    f_pratisat = forms.FloatField(required=False)
    f_kaifiyat = forms.CharField(required=False)
    
    #spice
    s_ekai = forms.ChoiceField(choices=commons.EKAI_CHOICES, required=False)
    s_lakshya = forms.IntegerField(required=False)
    s_pragati1 = forms.IntegerField(required=False)
    s_mahina_pragati = forms.IntegerField(required=False)
    s_sankhya = forms.IntegerField(required=False)
    s_parameter = forms.IntegerField(required=False)
    s_pragati2 = forms.IntegerField(required=False)
    s_pratisat = forms.FloatField(required=False)
    s_kaifiyat = forms.CharField(required=False)
    
    #tea
    t_ekai = forms.ChoiceField(choices=commons.EKAI_CHOICES, required=False)
    t_lakshya = forms.IntegerField(required=False)
    t_pragati1 = forms.IntegerField(required=False)
    t_mahina_pragati = forms.IntegerField(required=False)
    t_sankhya = forms.IntegerField(required=False)
    t_parameter = forms.IntegerField(required=False)
    t_pragati2 = forms.IntegerField(required=False)
    t_pratisat = forms.FloatField(required=False)
    t_kaifiyat = forms.CharField(required=False)
    
    #salt
    sa_ekai = forms.ChoiceField(choices=commons.EKAI_CHOICES, required=False)
    sa_lakshya = forms.IntegerField(required=False)
    sa_pragati1 = forms.IntegerField(required=False)
    sa_mahina_pragati = forms.IntegerField(required=False)
    sa_sankhya = forms.IntegerField(required=False)
    sa_parameter = forms.IntegerField(required=False)
    sa_pragati2 = forms.IntegerField(required=False)
    sa_pratisat = forms.FloatField(required=False)
    sa_kaifiyat = forms.CharField(required=False)
    
    #khadanna
    k_ekai = forms.ChoiceField(choices=commons.EKAI_CHOICES, required=False)
    k_lakshya = forms.IntegerField(required=False)
    k_pragati1 = forms.IntegerField(required=False)
    k_mahina_pragati = forms.IntegerField(required=False)
    k_sankhya = forms.IntegerField(required=False)
    k_parameter = forms.IntegerField(required=False)
    k_pragati2 = forms.IntegerField(required=False)
    k_pratisat = forms.FloatField(required=False)
    k_kaifiyat = forms.CharField(required=False)
    
    #water
    w_ekai = forms.ChoiceField(choices=commons.EKAI_CHOICES, required=False)
    w_lakshya = forms.IntegerField(required=False)
    w_pragati1 = forms.IntegerField(required=False)
    w_mahina_pragati = forms.IntegerField(required=False)
    w_sankhya = forms.IntegerField(required=False)
    w_parameter = forms.IntegerField(required=False)
    w_pragati2 = forms.IntegerField(required=False)
    w_pratisat = forms.FloatField(required=False)
    w_kaifiyat = forms.CharField(required=False)
    
    #sweets
    sw_ekai = forms.ChoiceField(choices=commons.EKAI_CHOICES, required=False)
    sw_lakshya = forms.IntegerField(required=False)
    sw_pragati1 = forms.IntegerField(required=False)
    sw_mahina_pragati = forms.IntegerField(required=False)
    sw_sankhya = forms.IntegerField(required=False)
    sw_parameter = forms.IntegerField(required=False)
    sw_pragati2 = forms.IntegerField(required=False)
    sw_pratisat = forms.FloatField(required=False)
    sw_kaifiyat = forms.CharField(required=False)
    
    #confectionery
    c_ekai = forms.ChoiceField(choices=commons.EKAI_CHOICES, required=False)
    c_lakshya = forms.IntegerField(required=False)
    c_pragati1 = forms.IntegerField(required=False)
    c_mahina_pragati = forms.IntegerField(required=False)
    c_sankhya = forms.IntegerField(required=False)
    c_parameter = forms.IntegerField(required=False)
    c_pragati2 = forms.IntegerField(required=False)
    c_pratisat = forms.FloatField(required=False)
    c_kaifiyat = forms.CharField(required=False)
    
    #meat
    me_ekai = forms.ChoiceField(choices=commons.EKAI_CHOICES, required=False)
    me_lakshya = forms.IntegerField(required=False)
    me_pragati1 = forms.IntegerField(required=False)
    me_mahina_pragati = forms.IntegerField(required=False)
    me_sankhya = forms.IntegerField(required=False)
    me_parameter = forms.IntegerField(required=False)
    me_pragati2 = forms.IntegerField(required=False)
    me_pratisat = forms.FloatField(required=False)
    me_kaifiyat = forms.CharField(required=False)
    
    #grain
    g_ekai = forms.ChoiceField(choices=commons.EKAI_CHOICES, required=False)
    g_lakshya = forms.IntegerField(required=False)
    g_pragati1 = forms.IntegerField(required=False)
    g_mahina_pragati = forms.IntegerField(required=False)
    g_sankhya = forms.IntegerField(required=False)
    g_parameter = forms.IntegerField(required=False)
    g_pragati2 = forms.IntegerField(required=False)
    g_pratisat = forms.FloatField(required=False)
    g_kaifiyat = forms.CharField(required=False)
    
    #others
    ot_ekai = forms.ChoiceField(choices=commons.EKAI_CHOICES, required=False)
    ot_lakshya = forms.IntegerField(required=False)
    ot_pragati1 = forms.IntegerField(required=False)
    ot_mahina_pragati = forms.IntegerField(required=False)
    ot_sankhya = forms.IntegerField(required=False)
    ot_parameter = forms.IntegerField(required=False)
    ot_pragati2 = forms.IntegerField(required=False)
    ot_pratisat = forms.FloatField(required=False)
    ot_kaifiyat = forms.CharField(required=False)
    
    def clean(self):
        cleaned_data = super().clean()
        label = [
                'm_lakshya', 'm_pragati1', 'm_mahina_pragati', 'm_sankhya', 'm_parameter', 'm_pragati2', 'm_pratisat',
                'o_lakshya', 'o_pragati1', 'o_mahina_pragati', 'o_sankhya', 'o_parameter', 'o_pragati2', 'o_pratisat',
                'f_lakshya', 'f_pragati1', 'f_mahina_pragati', 'f_sankhya', 'f_parameter', 'f_pragati2', 'f_pratisat',
                's_lakshya', 's_pragati1', 's_mahina_pragati', 's_sankhya', 's_parameter', 's_pragati2', 's_pratisat',
                't_lakshya', 't_pragati1', 't_mahina_pragati', 't_sankhya', 't_parameter', 't_pragati2', 't_pratisat',
                'sa_lakshya', 'sa_pragati1', 'sa_mahina_pragati', 'sa_sankhya', 'sa_parameter', 'sa_pragati2', 'sa_pratisat',
                'k_lakshya', 'k_pragati1', 'k_mahina_pragati', 'k_sankhya', 'k_parameter', 'k_pragati2', 'k_pratisat',
                'w_lakshya', 'w_pragati1', 'w_mahina_pragati', 'w_sankhya', 'w_parameter', 'w_pragati2', 'w_pratisat',
                'sw_lakshya', 'sw_pragati1', 'sw_mahina_pragati', 'sw_sankhya', 'sw_parameter', 'sw_pragati2', 'sw_pratisat',
                'c_lakshya', 'c_pragati1', 'c_mahina_pragati', 'c_sankhya', 'c_parameter', 'c_pragati2', 'c_pratisat',
                'me_lakshya', 'me_pragati1', 'me_mahina_pragati', 'me_sankhya', 'me_parameter', 'me_pragati2', 'me_pratisat',
                'g_lakshya', 'g_pragati1', 'g_mahina_pragati', 'g_sankhya', 'g_parameter', 'g_pragati2', 'g_pratisat',
                'ot_lakshya', 'ot_pragati1', 'ot_mahina_pragati', 'ot_sankhya', 'ot_parameter', 'ot_pragati2', 'ot_pratisat',
                ]
        for field_name in label:
            if field_name in cleaned_data and cleaned_data[field_name] is None:
                cleaned_data[field_name] = 0