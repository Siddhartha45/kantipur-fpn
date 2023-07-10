from django import forms
from .models import (BittiyaBibaran, UjuriGunaso, NamunaBibaran, PatraJari, PatraNabikaran, UdyogSifaris, PrayogsalaBisleysan,
                    KhadyaPrasodhan, DetailAnugaman, DetailHotel, DetailRegistration, DetailRenew, DetailUdyog, BarsikLakshya,
                    DetailGunaso,KhadyaPrasodhan,UjuriGunaso, DetailMudha, DetailRbpa, PragatiBibaran, AnugamanBibaran, Logobitaran, NamunaBisleysan,AayatNiryat)
from fpn import commons


class BaseModelForm(forms.ModelForm):
    """base model form with common clean method"""
    
    def clean(self):
        cleaned_data = super().clean()
        for field in self.Meta.model._meta.fields:
            if field.name in cleaned_data and cleaned_data[field.name] is None:
                cleaned_data[field.name] = field.default    
        return cleaned_data
    
    
class BarsikLakshyaForm(BaseModelForm):
    class Meta:
        model = BarsikLakshya
        exclude = ["created_by",]


class BittiyaBibaranForm(BaseModelForm):
    """model form for मासिक वित्तिय विवरण"""
    class Meta:
        model = BittiyaBibaran
        exclude = ["created_by",]


class PatraJariForm(BaseModelForm):
    """model form for खाद्य तथा दाना अनुज्ञा पत्र जारी"""
    class Meta:
        model = PatraJari
        exclude = ["created_by",]
        

class PatraNabikaranForm(BaseModelForm):
    """model form for खाद्य तथा दाना अनुज्ञा पत्र नविकरण"""
    class Meta:
        model = PatraNabikaran
        exclude = ["created_by",]
    

class UdyogSifarisForm(BaseModelForm):
    """model form for उद्योग सिफारिस"""
    class Meta:
        model = UdyogSifaris
        exclude = ["created_by",]
    

class UjuriGunasoForm(BaseModelForm):
    """model form for उजुरी/गुनासो ब्येवस्थापन"""
    class Meta:
        model = UjuriGunaso
        exclude = ["created_by",]
    
    
class NamunaBibaranForm(BaseModelForm):
    """model form for खाद्य ऐन/नियम बमोजिम संकलित नमुना विवरण"""
    class Meta:
        model = NamunaBibaran
        exclude = ["created_by", ]


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
                

class AayatNiryatForm(forms.Form):
    """form for आयात निर्यात गुण प्रमाणिकरण"""
    
    #milk
    m_ekai = forms.ChoiceField(choices=commons.EKAI_CHOICES, required=False)
    m_b_lakshya = forms.IntegerField(required=False)
    m_c_lakshya = forms.IntegerField(required=False)
    m_c_pragati = forms.IntegerField(required=False)
    m_m_pragati = forms.IntegerField(required=False)
    m_pratikul_n = forms.IntegerField(required=False)
    m_pratikul_p = forms.IntegerField(required=False)
    m_h_pragati = forms.IntegerField(required=False)
    m_h_pratisat = forms.IntegerField(required=False)
    m_kaifiyat = forms.CharField(required=False)
    
    #oil
    o_ekai = forms.ChoiceField(choices=commons.EKAI_CHOICES, required=False)
    o_b_lakshya = forms.IntegerField(required=False)
    o_c_lakshya = forms.IntegerField(required=False)
    o_c_pragati = forms.IntegerField(required=False)
    o_m_pragati = forms.IntegerField(required=False)
    o_pratikul_n = forms.IntegerField(required=False)
    o_pratikul_p = forms.IntegerField(required=False)
    o_h_pragati = forms.IntegerField(required=False)
    o_h_pratisat = forms.IntegerField(required=False)
    o_kaifiyat = forms.CharField(required=False)
    
    #fruits
    f_ekai = forms.ChoiceField(choices=commons.EKAI_CHOICES, required=False)
    f_b_lakshya = forms.IntegerField(required=False)
    f_c_lakshya = forms.IntegerField(required=False)
    f_c_pragati = forms.IntegerField(required=False)
    f_m_pragati = forms.IntegerField(required=False)
    f_pratikul_n = forms.IntegerField(required=False)
    f_pratikul_p = forms.IntegerField(required=False)
    f_h_pragati = forms.IntegerField(required=False)
    f_h_pratisat = forms.IntegerField(required=False)
    f_kaifiyat = forms.CharField(required=False)
    
    #spice
    s_ekai = forms.ChoiceField(choices=commons.EKAI_CHOICES, required=False)
    s_b_lakshya = forms.IntegerField(required=False)
    s_c_lakshya = forms.IntegerField(required=False)
    s_c_pragati = forms.IntegerField(required=False)
    s_m_pragati = forms.IntegerField(required=False)
    s_pratikul_n = forms.IntegerField(required=False)
    s_pratikul_p = forms.IntegerField(required=False)
    s_h_pragati = forms.IntegerField(required=False)
    s_h_pratisat = forms.IntegerField(required=False)
    s_kaifiyat = forms.CharField(required=False)
    
    #tea
    t_ekai = forms.ChoiceField(choices=commons.EKAI_CHOICES, required=False)
    t_b_lakshya = forms.IntegerField(required=False)
    t_c_lakshya = forms.IntegerField(required=False)
    t_c_pragati = forms.IntegerField(required=False)
    t_m_pragati = forms.IntegerField(required=False)
    t_pratikul_n = forms.IntegerField(required=False)
    t_pratikul_p = forms.IntegerField(required=False)
    t_h_pragati = forms.IntegerField(required=False)
    t_h_pratisat = forms.IntegerField(required=False)
    t_kaifiyat = forms.CharField(required=False)
    
    #salt
    sa_ekai = forms.ChoiceField(choices=commons.EKAI_CHOICES, required=False)
    sa_b_lakshya = forms.IntegerField(required=False)
    sa_c_lakshya = forms.IntegerField(required=False)
    sa_c_pragati = forms.IntegerField(required=False)
    sa_m_pragati = forms.IntegerField(required=False)
    sa_pratikul_n = forms.IntegerField(required=False)
    sa_pratikul_p = forms.IntegerField(required=False)
    sa_h_pragati = forms.IntegerField(required=False)
    sa_h_pratisat = forms.IntegerField(required=False)
    sa_kaifiyat = forms.CharField(required=False)
    
    #khadanna
    k_ekai = forms.ChoiceField(choices=commons.EKAI_CHOICES, required=False)
    k_b_lakshya = forms.IntegerField(required=False)
    k_c_lakshya = forms.IntegerField(required=False)
    k_c_pragati = forms.IntegerField(required=False)
    k_m_pragati = forms.IntegerField(required=False)
    k_pratikul_n = forms.IntegerField(required=False)
    k_pratikul_p = forms.IntegerField(required=False)
    k_h_pragati = forms.IntegerField(required=False)
    k_h_pratisat = forms.IntegerField(required=False)
    k_kaifiyat = forms.CharField(required=False)
    
    #water
    w_ekai = forms.ChoiceField(choices=commons.EKAI_CHOICES, required=False)
    w_b_lakshya = forms.IntegerField(required=False)
    w_c_lakshya = forms.IntegerField(required=False)
    w_c_pragati = forms.IntegerField(required=False)
    w_m_pragati = forms.IntegerField(required=False)
    w_pratikul_n = forms.IntegerField(required=False)
    w_pratikul_p = forms.IntegerField(required=False)
    w_h_pragati = forms.IntegerField(required=False)
    w_h_pratisat = forms.IntegerField(required=False)
    w_kaifiyat = forms.CharField(required=False)
    
    #sweets
    sw_ekai = forms.ChoiceField(choices=commons.EKAI_CHOICES, required=False)
    sw_b_lakshya = forms.IntegerField(required=False)
    sw_c_lakshya = forms.IntegerField(required=False)
    sw_c_pragati = forms.IntegerField(required=False)
    sw_m_pragati = forms.IntegerField(required=False)
    sw_pratikul_n = forms.IntegerField(required=False)
    sw_pratikul_p = forms.IntegerField(required=False)
    sw_h_pragati = forms.IntegerField(required=False)
    sw_h_pratisat = forms.IntegerField(required=False)
    sw_kaifiyat = forms.CharField(required=False)
    
    #confectionery
    c_ekai = forms.ChoiceField(choices=commons.EKAI_CHOICES, required=False)
    c_b_lakshya = forms.IntegerField(required=False)
    c_c_lakshya = forms.IntegerField(required=False)
    c_c_pragati = forms.IntegerField(required=False)
    c_m_pragati = forms.IntegerField(required=False)
    c_pratikul_n = forms.IntegerField(required=False)
    c_pratikul_p = forms.IntegerField(required=False)
    c_h_pragati = forms.IntegerField(required=False)
    c_h_pratisat = forms.IntegerField(required=False)
    c_kaifiyat = forms.CharField(required=False)
    
    #meat
    me_ekai = forms.ChoiceField(choices=commons.EKAI_CHOICES, required=False)
    me_b_lakshya = forms.IntegerField(required=False)
    me_c_lakshya = forms.IntegerField(required=False)
    me_c_pragati = forms.IntegerField(required=False)
    me_m_pragati = forms.IntegerField(required=False)
    me_pratikul_n = forms.IntegerField(required=False)
    me_pratikul_p = forms.IntegerField(required=False)
    me_h_pragati = forms.IntegerField(required=False)
    me_h_pratisat = forms.IntegerField(required=False)
    me_kaifiyat = forms.CharField(required=False)
    
    #others
    ot_ekai = forms.ChoiceField(choices=commons.EKAI_CHOICES, required=False)
    ot_b_lakshya = forms.IntegerField(required=False)
    ot_c_lakshya = forms.IntegerField(required=False)
    ot_c_pragati = forms.IntegerField(required=False)
    ot_m_pragati = forms.IntegerField(required=False)
    ot_pratikul_n = forms.IntegerField(required=False)
    ot_pratikul_p = forms.IntegerField(required=False)
    ot_h_pragati = forms.IntegerField(required=False)
    ot_h_pratisat = forms.IntegerField(required=False)
    ot_kaifiyat = forms.CharField(required=False)
    
    #grain
    g_ekai = forms.ChoiceField(choices=commons.EKAI_CHOICES, required=False)
    g_b_lakshya = forms.IntegerField(required=False)
    g_c_lakshya = forms.IntegerField(required=False)
    g_c_pragati = forms.IntegerField(required=False)
    g_m_pragati = forms.IntegerField(required=False)
    g_pratikul_n = forms.IntegerField(required=False)
    g_pratikul_p = forms.IntegerField(required=False)
    g_h_pragati = forms.IntegerField(required=False)
    g_h_pratisat = forms.IntegerField(required=False)
    g_kaifiyat = forms.CharField(required=False)
    
    def clean(self):
        cleaned_data = super().clean()
        label = [
            'm_b_lakshya', 'm_c_lakshya', 'm_c_pragati', 'm_m_pragati', 'm_pratikul_n', 'm_pratikul_p', 'm_h_pragati', 'm_h_pratisat',
            'o_b_lakshya', 'o_c_lakshya', 'o_c_pragati', 'o_m_pragati', 'o_pratikul_n', 'o_pratikul_p', 'o_h_pragati', 'o_h_pratisat',
            'f_b_lakshya', 'f_c_lakshya', 'f_c_pragati', 'f_m_pragati', 'f_pratikul_n', 'f_pratikul_p', 'f_h_pragati', 'f_h_pratisat',
            's_b_lakshya', 's_c_lakshya', 's_c_pragati', 's_m_pragati', 's_pratikul_n', 's_pratikul_p', 's_h_pragati', 's_h_pratisat',
            't_b_lakshya', 't_c_lakshya', 't_c_pragati', 't_m_pragati', 't_pratikul_n', 't_pratikul_p', 't_h_pragati', 't_h_pratisat',
            'sa_b_lakshya', 'sa_c_lakshya', 'sa_c_pragati', 'sa_m_pragati', 'sa_pratikul_n', 'sa_pratikul_p', 'sa_h_pragati', 'sa_h_pratisat',
            'k_b_lakshya', 'k_c_lakshya', 'k_c_pragati', 'k_m_pragati', 'k_pratikul_n', 'k_pratikul_p', 'k_h_pragati', 'k_h_pratisat',
            'w_b_lakshya', 'w_c_lakshya', 'w_c_pragati', 'w_m_pragati', 'w_pratikul_n', 'w_pratikul_p', 'w_h_pragati', 'w_h_pratisat',
            'sw_b_lakshya', 'sw_c_lakshya', 'sw_c_pragati', 'sw_m_pragati', 'sw_pratikul_n', 'sw_pratikul_p', 'sw_h_pragati', 'sw_h_pratisat',
            'c_b_lakshya', 'c_c_lakshya', 'c_c_pragati', 'c_m_pragati', 'c_pratikul_n', 'c_pratikul_p', 'c_h_pragati', 'c_h_pratisat',
            'me_b_lakshya', 'me_c_lakshya', 'me_c_pragati', 'me_m_pragati', 'me_pratikul_n', 'me_pratikul_p', 'me_h_pragati', 'me_h_pratisat',
            'ot_b_lakshya', 'ot_c_lakshya', 'ot_c_pragati', 'ot_m_pragati', 'ot_pratikul_n', 'ot_pratikul_p', 'ot_h_pragati', 'ot_h_pratisat',
            'g_b_lakshya', 'g_c_lakshya', 'g_c_pragati', 'g_m_pragati', 'g_pratikul_n', 'g_pratikul_p', 'g_h_pragati', 'g_h_pratisat',
        ]
        for field_name in label:
            if field_name in cleaned_data and cleaned_data[field_name] is None:
                cleaned_data[field_name] = 0
                
                
class PrayogsalaBisleysanForm(forms.Form):
    """form for प्रयोगशाला विश्लेषण प्रतिवेदन सारांश"""
    
    #milk
    m_b_sankhya = forms.IntegerField(required=False)
    m_b_pratikul = forms.IntegerField(required=False)
    m_u_sankhya = forms.IntegerField(required=False)
    m_u_pratikul = forms.IntegerField(required=False)
    m_ay_sankhya = forms.IntegerField(required=False)
    m_ay_pratikul = forms.IntegerField(required=False)
    m_v_sankhya = forms.IntegerField(required=False)
    m_v_pratikul = forms.IntegerField(required=False)
    m_k_sankhya = forms.IntegerField(required=False)
    m_k_pratikul = forms.IntegerField(required=False)
    m_a_sankhya = forms.IntegerField(required=False)
    m_a_pratikul = forms.IntegerField(required=False)
    m_kul_sankhya = forms.IntegerField(required=False)
    m_kul_pratikul = forms.IntegerField(required=False)
    m_sample = forms.IntegerField(required=False)
    m_kaifiyat = forms.CharField(required=False)
    
    #oil
    o_b_sankhya = forms.IntegerField(required=False)
    o_b_pratikul = forms.IntegerField(required=False)
    o_u_sankhya = forms.IntegerField(required=False)
    o_u_pratikul = forms.IntegerField(required=False)
    o_ay_sankhya = forms.IntegerField(required=False)
    o_ay_pratikul = forms.IntegerField(required=False)
    o_v_sankhya = forms.IntegerField(required=False)
    o_v_pratikul = forms.IntegerField(required=False)
    o_k_sankhya = forms.IntegerField(required=False)
    o_k_pratikul = forms.IntegerField(required=False)
    o_a_sankhya = forms.IntegerField(required=False)
    o_a_pratikul = forms.IntegerField(required=False)
    o_kul_sankhya = forms.IntegerField(required=False)
    o_kul_pratikul = forms.IntegerField(required=False)
    o_sample = forms.IntegerField(required=False)
    o_kaifiyat = forms.CharField(required=False)
    
    #fruits
    f_b_sankhya = forms.IntegerField(required=False)
    f_b_pratikul = forms.IntegerField(required=False)
    f_u_sankhya = forms.IntegerField(required=False)
    f_u_pratikul = forms.IntegerField(required=False)
    f_ay_sankhya = forms.IntegerField(required=False)
    f_ay_pratikul = forms.IntegerField(required=False)
    f_v_sankhya = forms.IntegerField(required=False)
    f_v_pratikul = forms.IntegerField(required=False)
    f_k_sankhya = forms.IntegerField(required=False)
    f_k_pratikul = forms.IntegerField(required=False)
    f_a_sankhya = forms.IntegerField(required=False)
    f_a_pratikul = forms.IntegerField(required=False)
    f_kul_sankhya = forms.IntegerField(required=False)
    f_kul_pratikul = forms.IntegerField(required=False)
    f_sample = forms.IntegerField(required=False)
    f_kaifiyat = forms.CharField(required=False)
    
    #spice
    s_b_sankhya = forms.IntegerField(required=False)
    s_b_pratikul = forms.IntegerField(required=False)
    s_u_sankhya = forms.IntegerField(required=False)
    s_u_pratikul = forms.IntegerField(required=False)
    s_ay_sankhya = forms.IntegerField(required=False)
    s_ay_pratikul = forms.IntegerField(required=False)
    s_v_sankhya = forms.IntegerField(required=False)
    s_v_pratikul = forms.IntegerField(required=False)
    s_k_sankhya = forms.IntegerField(required=False)
    s_k_pratikul = forms.IntegerField(required=False)
    s_a_sankhya = forms.IntegerField(required=False)
    s_a_pratikul = forms.IntegerField(required=False)
    s_kul_sankhya = forms.IntegerField(required=False)
    s_kul_pratikul = forms.IntegerField(required=False)
    s_sample = forms.IntegerField(required=False)
    s_kaifiyat = forms.CharField(required=False)
    
    #tea
    t_b_sankhya = forms.IntegerField(required=False)
    t_b_pratikul = forms.IntegerField(required=False)
    t_u_sankhya = forms.IntegerField(required=False)
    t_u_pratikul = forms.IntegerField(required=False)
    t_ay_sankhya = forms.IntegerField(required=False)
    t_ay_pratikul = forms.IntegerField(required=False)
    t_v_sankhya = forms.IntegerField(required=False)
    t_v_pratikul = forms.IntegerField(required=False)
    t_k_sankhya = forms.IntegerField(required=False)
    t_k_pratikul = forms.IntegerField(required=False)
    t_a_sankhya = forms.IntegerField(required=False)
    t_a_pratikul = forms.IntegerField(required=False)
    t_kul_sankhya = forms.IntegerField(required=False)
    t_kul_pratikul = forms.IntegerField(required=False)
    t_sample = forms.IntegerField(required=False)
    t_kaifiyat = forms.CharField(required=False)
    
    #salt
    sa_b_sankhya = forms.IntegerField(required=False)
    sa_b_pratikul = forms.IntegerField(required=False)
    sa_u_sankhya = forms.IntegerField(required=False)
    sa_u_pratikul = forms.IntegerField(required=False)
    sa_ay_sankhya = forms.IntegerField(required=False)
    sa_ay_pratikul = forms.IntegerField(required=False)
    sa_v_sankhya = forms.IntegerField(required=False)
    sa_v_pratikul = forms.IntegerField(required=False)
    sa_k_sankhya = forms.IntegerField(required=False)
    sa_k_pratikul = forms.IntegerField(required=False)
    sa_a_sankhya = forms.IntegerField(required=False)
    sa_a_pratikul = forms.IntegerField(required=False)
    sa_kul_sankhya = forms.IntegerField(required=False)
    sa_kul_pratikul = forms.IntegerField(required=False)
    sa_sample = forms.IntegerField(required=False)
    sa_kaifiyat = forms.CharField(required=False)
    
    #khadanna
    k_b_sankhya = forms.IntegerField(required=False)
    k_b_pratikul = forms.IntegerField(required=False)
    k_u_sankhya = forms.IntegerField(required=False)
    k_u_pratikul = forms.IntegerField(required=False)
    k_ay_sankhya = forms.IntegerField(required=False)
    k_ay_pratikul = forms.IntegerField(required=False)
    k_v_sankhya = forms.IntegerField(required=False)
    k_v_pratikul = forms.IntegerField(required=False)
    k_k_sankhya = forms.IntegerField(required=False)
    k_k_pratikul = forms.IntegerField(required=False)
    k_a_sankhya = forms.IntegerField(required=False)
    k_a_pratikul = forms.IntegerField(required=False)
    k_kul_sankhya = forms.IntegerField(required=False)
    k_kul_pratikul = forms.IntegerField(required=False)
    k_sample = forms.IntegerField(required=False)
    k_kaifiyat = forms.CharField(required=False)
    
    #water
    w_b_sankhya = forms.IntegerField(required=False)
    w_b_pratikul = forms.IntegerField(required=False)
    w_u_sankhya = forms.IntegerField(required=False)
    w_u_pratikul = forms.IntegerField(required=False)
    w_ay_sankhya = forms.IntegerField(required=False)
    w_ay_pratikul = forms.IntegerField(required=False)
    w_v_sankhya = forms.IntegerField(required=False)
    w_v_pratikul = forms.IntegerField(required=False)
    w_k_sankhya = forms.IntegerField(required=False)
    w_k_pratikul = forms.IntegerField(required=False)
    w_a_sankhya = forms.IntegerField(required=False)
    w_a_pratikul = forms.IntegerField(required=False)
    w_kul_sankhya = forms.IntegerField(required=False)
    w_kul_pratikul = forms.IntegerField(required=False)
    w_sample = forms.IntegerField(required=False)
    w_kaifiyat = forms.CharField(required=False)
    
    #sweets
    sw_b_sankhya = forms.IntegerField(required=False)
    sw_b_pratikul = forms.IntegerField(required=False)
    sw_u_sankhya = forms.IntegerField(required=False)
    sw_u_pratikul = forms.IntegerField(required=False)
    sw_ay_sankhya = forms.IntegerField(required=False)
    sw_ay_pratikul = forms.IntegerField(required=False)
    sw_v_sankhya = forms.IntegerField(required=False)
    sw_v_pratikul = forms.IntegerField(required=False)
    sw_k_sankhya = forms.IntegerField(required=False)
    sw_k_pratikul = forms.IntegerField(required=False)
    sw_a_sankhya = forms.IntegerField(required=False)
    sw_a_pratikul = forms.IntegerField(required=False)
    sw_kul_sankhya = forms.IntegerField(required=False)
    sw_kul_pratikul = forms.IntegerField(required=False)
    sw_sample = forms.IntegerField(required=False)
    sw_kaifiyat = forms.CharField(required=False)
    
    #confectionery
    c_b_sankhya = forms.IntegerField(required=False)
    c_b_pratikul = forms.IntegerField(required=False)
    c_u_sankhya = forms.IntegerField(required=False)
    c_u_pratikul = forms.IntegerField(required=False)
    c_ay_sankhya = forms.IntegerField(required=False)
    c_ay_pratikul = forms.IntegerField(required=False)
    c_v_sankhya = forms.IntegerField(required=False)
    c_v_pratikul = forms.IntegerField(required=False)
    c_k_sankhya = forms.IntegerField(required=False)
    c_k_pratikul = forms.IntegerField(required=False)
    c_a_sankhya = forms.IntegerField(required=False)
    c_a_pratikul = forms.IntegerField(required=False)
    c_kul_sankhya = forms.IntegerField(required=False)
    c_kul_pratikul = forms.IntegerField(required=False)
    c_sample = forms.IntegerField(required=False)
    c_kaifiyat = forms.CharField(required=False)
    
    #meat
    me_b_sankhya = forms.IntegerField(required=False)
    me_b_pratikul = forms.IntegerField(required=False)
    me_u_sankhya = forms.IntegerField(required=False)
    me_u_pratikul = forms.IntegerField(required=False)
    me_ay_sankhya = forms.IntegerField(required=False)
    me_ay_pratikul = forms.IntegerField(required=False)
    me_v_sankhya = forms.IntegerField(required=False)
    me_v_pratikul = forms.IntegerField(required=False)
    me_k_sankhya = forms.IntegerField(required=False)
    me_k_pratikul = forms.IntegerField(required=False)
    me_a_sankhya = forms.IntegerField(required=False)
    me_a_pratikul = forms.IntegerField(required=False)
    me_kul_sankhya = forms.IntegerField(required=False)
    me_kul_pratikul = forms.IntegerField(required=False)
    me_sample = forms.IntegerField(required=False)
    me_kaifiyat = forms.CharField(required=False)
    
    #grain
    g_b_sankhya = forms.IntegerField(required=False)
    g_b_pratikul = forms.IntegerField(required=False)
    g_u_sankhya = forms.IntegerField(required=False)
    g_u_pratikul = forms.IntegerField(required=False)
    g_ay_sankhya = forms.IntegerField(required=False)
    g_ay_pratikul = forms.IntegerField(required=False)
    g_v_sankhya = forms.IntegerField(required=False)
    g_v_pratikul = forms.IntegerField(required=False)
    g_k_sankhya = forms.IntegerField(required=False)
    g_k_pratikul = forms.IntegerField(required=False)
    g_a_sankhya = forms.IntegerField(required=False)
    g_a_pratikul = forms.IntegerField(required=False)
    g_kul_sankhya = forms.IntegerField(required=False)
    g_kul_pratikul = forms.IntegerField(required=False)
    g_sample = forms.IntegerField(required=False)
    g_kaifiyat = forms.CharField(required=False)
    
    #others
    ot_b_sankhya = forms.IntegerField(required=False)
    ot_b_pratikul = forms.IntegerField(required=False)
    ot_u_sankhya = forms.IntegerField(required=False)
    ot_u_pratikul = forms.IntegerField(required=False)
    ot_ay_sankhya = forms.IntegerField(required=False)
    ot_ay_pratikul = forms.IntegerField(required=False)
    ot_v_sankhya = forms.IntegerField(required=False)
    ot_v_pratikul = forms.IntegerField(required=False)
    ot_k_sankhya = forms.IntegerField(required=False)
    ot_k_pratikul = forms.IntegerField(required=False)
    ot_a_sankhya = forms.IntegerField(required=False)
    ot_a_pratikul = forms.IntegerField(required=False)
    ot_kul_sankhya = forms.IntegerField(required=False)
    ot_kul_pratikul = forms.IntegerField(required=False)
    ot_sample = forms.IntegerField(required=False)
    ot_kaifiyat = forms.CharField(required=False)
    
    def clean(self):
        cleaned_data = super().clean()
        label = [
            'm_b_sankhya', 'm_b_pratikul', 'm_u_sankhya', 'm_u_pratikul', 'm_ay_sankhya', 'm_ay_pratikul', 'm_v_sankhya', 'm_v_pratikul', 'm_k_sankhya', 'm_k_pratikul', 'm_a_sankhya', 'm_a_pratikul', 'm_kul_sankhya', 'm_kul_pratikul', 'm_sample',
            'o_b_sankhya', 'o_b_pratikul', 'o_u_sankhya', 'o_u_pratikul', 'o_ay_sankhya', 'o_ay_pratikul', 'o_v_sankhya', 'o_v_pratikul', 'o_k_sankhya', 'o_k_pratikul', 'o_a_sankhya', 'o_a_pratikul', 'o_kul_sankhya', 'o_kul_pratikul', 'o_sample',
            'f_b_sankhya', 'f_b_pratikul', 'f_u_sankhya', 'f_u_pratikul', 'f_ay_sankhya', 'f_ay_pratikul', 'f_v_sankhya', 'f_v_pratikul', 'f_k_sankhya', 'f_k_pratikul', 'f_a_sankhya', 'f_a_pratikul', 'f_kul_sankhya', 'f_kul_pratikul', 'f_sample',
            's_b_sankhya', 's_b_pratikul', 's_u_sankhya', 's_u_pratikul', 's_ay_sankhya', 's_ay_pratikul', 's_v_sankhya', 's_v_pratikul', 's_k_sankhya', 's_k_pratikul', 's_a_sankhya', 's_a_pratikul', 's_kul_sankhya', 's_kul_pratikul', 's_sample',
            't_b_sankhya', 't_b_pratikul', 't_u_sankhya', 't_u_pratikul', 't_ay_sankhya', 't_ay_pratikul', 't_v_sankhya', 't_v_pratikul', 't_k_sankhya', 't_k_pratikul', 't_a_sankhya', 't_a_pratikul', 't_kul_sankhya', 't_kul_pratikul', 't_sample',
            'sa_b_sankhya', 'sa_b_pratikul', 'sa_u_sankhya', 'sa_u_pratikul', 'sa_ay_sankhya', 'sa_ay_pratikul', 'sa_v_sankhya', 'sa_v_pratikul', 'sa_k_sankhya', 'sa_k_pratikul', 'sa_a_sankhya', 'sa_a_pratikul', 'sa_kul_sankhya', 'sa_kul_pratikul', 'sa_sample',
            'k_b_sankhya', 'k_b_pratikul', 'k_u_sankhya', 'k_u_pratikul', 'k_ay_sankhya', 'k_ay_pratikul', 'k_v_sankhya', 'k_v_pratikul', 'k_k_sankhya', 'k_k_pratikul', 'k_a_sankhya', 'k_a_pratikul', 'k_kul_sankhya', 'k_kul_pratikul', 'k_sample',
            'w_b_sankhya', 'w_b_pratikul', 'w_u_sankhya', 'w_u_pratikul', 'w_ay_sankhya', 'w_ay_pratikul', 'w_v_sankhya', 'w_v_pratikul', 'w_k_sankhya', 'w_k_pratikul', 'w_a_sankhya', 'w_a_pratikul', 'w_kul_sankhya', 'w_kul_pratikul', 'w_sample',
            'sw_b_sankhya', 'sw_b_pratikul', 'sw_u_sankhya', 'sw_u_pratikul', 'sw_ay_sankhya', 'sw_ay_pratikul', 'sw_v_sankhya', 'sw_v_pratikul', 'sw_k_sankhya', 'sw_k_pratikul', 'sw_a_sankhya', 'sw_a_pratikul', 'sw_kul_sankhya', 'sw_kul_pratikul', 'sw_sample',
            'c_b_sankhya', 'c_b_pratikul', 'c_u_sankhya', 'c_u_pratikul', 'c_ay_sankhya', 'c_ay_pratikul', 'c_v_sankhya', 'c_v_pratikul', 'c_k_sankhya', 'c_k_pratikul', 'c_a_sankhya', 'c_a_pratikul', 'c_kul_sankhya', 'c_kul_pratikul', 'c_sample',
            'me_b_sankhya', 'me_b_pratikul', 'me_u_sankhya', 'me_u_pratikul', 'me_ay_sankhya', 'me_ay_pratikul', 'me_v_sankhya', 'me_v_pratikul', 'me_k_sankhya', 'me_k_pratikul', 'me_a_sankhya', 'me_a_pratikul', 'me_kul_sankhya', 'me_kul_pratikul', 'me_sample',
            'g_b_sankhya', 'g_b_pratikul', 'g_u_sankhya', 'g_u_pratikul', 'g_ay_sankhya', 'g_ay_pratikul', 'g_v_sankhya', 'g_v_pratikul', 'g_k_sankhya', 'g_k_pratikul', 'g_a_sankhya', 'g_a_pratikul', 'g_kul_sankhya', 'g_kul_pratikul', 'g_sample',
            'ot_b_sankhya', 'ot_b_pratikul', 'ot_u_sankhya', 'ot_u_pratikul', 'ot_ay_sankhya', 'ot_ay_pratikul', 'ot_v_sankhya', 'ot_v_pratikul', 'ot_k_sankhya', 'ot_k_pratikul', 'ot_a_sankhya', 'ot_a_pratikul', 'ot_kul_sankhya', 'ot_kul_pratikul', 'ot_sample',
        ]
        for field_name in label:
            if field_name in cleaned_data and cleaned_data[field_name] is None:
                cleaned_data[field_name] = 0


class LogobitaranForm(forms.Form):
    """form for होटल स्तरीकरण लोगो वितरण सम्बन्धि विवरण"""
    
    #green
    g_c_pragati = forms.IntegerField(required=False)
    g_h_pragati1 = forms.IntegerField(required=False)
    g_h_pragati2 = forms.IntegerField(required=False)
    g_kaifiyat = forms.CharField(required=False)
    
    #yellow1
    y1_c_pragati = forms.IntegerField(required=False)
    y1_h_pragati1 = forms.IntegerField(required=False)
    y1_h_pragati2 = forms.IntegerField(required=False)
    y1_kaifiyat = forms.CharField(required=False)
    
    #yellow2
    y2_c_pragati = forms.IntegerField(required=False)
    y2_h_pragati1 = forms.IntegerField(required=False)
    y2_h_pragati2 = forms.IntegerField(required=False)
    y2_kaifiyat = forms.CharField(required=False)
    
    #red
    r_c_pragati = forms.IntegerField(required=False)
    r_h_pragati1 = forms.IntegerField(required=False)
    r_h_pragati2 = forms.IntegerField(required=False)
    r_kaifiyat = forms.CharField(required=False)
    
    def clean(self):
        cleaned_data = super().clean()
        label = [
            'g_c_pragati', 'g_h_pragati1', 'g_h_pragati2', 
            'y1_c_pragati', 'y1_h_pragati1', 'y1_h_pragati2',
            'y2_c_pragati', 'y2_h_pragati1', 'y2_h_pragati2',
            'r_c_pragati', 'r_h_pragati1', 'r_h_pragati2',
        ]
        for field_name in label:
            if field_name in cleaned_data and cleaned_data[field_name] is None:
                cleaned_data[field_name] = 0
                

class KhadyaPrasodhanForm(BaseModelForm):
    """modelform for खाद्य प्रसोधन, खाद्य पोषण, उद्योग, होटेल, पत्रकार, कार्यशाला आदि"""
    class Meta:
        model = KhadyaPrasodhan
        exclude = ["created_by", ]


class MasikPragatiForm(BaseModelForm):
    """modelform for maski pragati"""
    class Meta:
        model = PragatiBibaran
        exclude = ["created_by", ]




#----------------------------------------------------Detail Part Forms----------------------------------------------------------------

class DetailHotelForm(BaseModelForm):
    class Meta:
        model = DetailHotel
        exclude = ["created_by",]


class DetailRegistrationForm(BaseModelForm):
    class Meta:
        model = DetailRegistration
        exclude = ["created_by",]
        
        
class DetailRenewForm(BaseModelForm):
    class Meta:
        model = DetailRenew
        exclude = ["created_by",]


class DetailUdyogForm(BaseModelForm):
    class Meta:
        model = DetailUdyog
        exclude = ["created_by",]


class DetailAnugamanForm(BaseModelForm):
    class Meta:
        model = DetailAnugaman
        exclude = ["created_by",]  


class DetailMudhaForm(BaseModelForm):
    class Meta:
        model = DetailMudha
        exclude = ["created_by",]


class DetailRbpaForm(BaseModelForm):
    class Meta:
        model = DetailRbpa
        exclude = ["created_by",]    

        
class DetailGunasoForm(BaseModelForm):
    class Meta:
        model = DetailGunaso
        exclude = ["created_by",]


#-------------------------------------------------------------------EDIT FORMS----------------------------------------------------------

class AnugamanEditForm(forms.ModelForm):
    class Meta:
        model = AnugamanBibaran
        exclude = ["created_on_np_date", "created_by", "type"]
        
        
class KhadyaactEditForm(forms.ModelForm):
    class Meta:
        model = NamunaBibaran
        exclude = ["created_on_np_date", "created_by"]
        
        
class HotelEditForm(forms.ModelForm):
    class Meta:
        model = Logobitaran
        exclude = ["created_on_np_date", "created_by", "type"]
        
        
class KhadyaEditForm(forms.ModelForm):
    class Meta:
        model = NamunaBisleysan
        exclude = ["created-on_np_date", "created_by", "type"]
        
        
class PrayogsalaEditForm(forms.ModelForm):
    class Meta:
        model = PrayogsalaBisleysan
        exclude = ["created_on_np_date", "created_by", "type"]
        
        
class RbpaEditForm(forms.ModelForm):
    class Meta:
        model = DetailRbpa
        exclude = ["created_on_np_date", "created_by"]
        
        
class AayatNiryatEditForm(forms.ModelForm):
    class Meta:
        model= AayatNiryat
        exclude = ["created_on_np_date", "created_by", 'type']
        
class UjuriGunasoEditForm(forms.ModelForm):
    class Meta:
        model=UjuriGunaso
        exclude = ["created_on_np_date", "created_by"]
        
        
class KhadyaPrasodhanEditForm(forms.ModelForm):
    class Meta:
        model=KhadyaPrasodhan
        
        exclude = ["created_on_np_date", "created_by"]
        
class BittiyaBibaranEditForm(forms.ModelForm):
    class Meta:
        model=BittiyaBibaran
        exclude = ["created_on_np_date", "created_by"]
        
        
class PragatiBibaranEditForm(forms.ModelForm):
    class Meta:
        model=PragatiBibaran
        exclude = ["created_on_np_date", "created_by"]
        
class UdyogSifarisEditForm(forms.ModelForm):
    class Meta:
        model=UdyogSifaris
        exclude = ["created_on_np_date", "created_by"]
        
class PatraNabikaranEditForm(forms.ModelForm):
    class Meta:
        model=PatraNabikaran
        exclude = ["created_on_np_date", "created_by"]

class PatraJariEditForm(forms.ModelForm):
    class Meta:
        model=PatraJari
        exclude = ["created_on_np_date", "created_by"]
        
    