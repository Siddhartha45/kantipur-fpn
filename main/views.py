from django.shortcuts import render, HttpResponse, redirect
from .forms import (UjuriGunasoForm, BittiyaBibaranForm, NamunaBibaranForm, PatraJariForm, PatraNabikaranForm,
                    UdyogSifarisForm, AnugamanBibaranForm, NamunaBisleysanForm, AayatNiryatForm, PrayogsalaBisleysanForm,
                    LogobitaranForm, KhadyaPrasodhanForm, DetailAnugamanForm, DetailHotelForm, DetailRegistrationForm, DetailRenewForm,
                    DetailUdyogForm, DetailGunasoForm, DetailMudhaForm, DetailRbpaForm, MasikPragatiForm)
from .models import (AnugamanBibaran, NamunaBisleysan, AayatNiryat, PrayogsalaBisleysan, Logobitaran, BittiyaBibaran, UjuriGunaso,
                    NamunaBibaran, PragatiBibaran, DetailRbpa, UdyogSifaris, PatraNabikaran, PatraJari, KhadyaPrasodhan)
from fpn import commons
from django.contrib.auth.decorators import login_required
import datetime
import nepali_datetime


@login_required
def home(request):
    """view for dashboard"""
    return render(request, 'index.html')


#-----------------------FORMS PART BELOW -----------------------
def namuna_bibaran(request):
    """views for खाद्य ऐन/नियम बमोजिम संकलित नमुना विवरण"""
    
    if request.method == 'POST':
        form = NamunaBibaranForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("data saved")
    else:
        form = NamunaBibaranForm()
    context = {'form': form}
    return render(request, 'forms/namuna_bibaran/newentry.html', context)


def anugaman(request):
    """views for निरीक्षण अनुगमन विवरण"""
    if request.method == 'POST':
        form = AnugamanBibaranForm(request.POST)
        if form.is_valid():
            objects_to_create = []  #creating empty list to store different datas
            
            u_data = {
                'type' : 'udyog',
                'patak' : form.cleaned_data.get('u_patak'),
                'sankhya' : form.cleaned_data.get('u_sankhya'),
                'pragati': form.cleaned_data.get('u_pragati'),
                'kaifiyat': form.cleaned_data.get('u_kaifiyat'),
            }
            objects_to_create.append(AnugamanBibaran(**u_data))
        
            p_data = {
                'type' : 'pasal',
                'patak' : form.cleaned_data.get('p_patak'),
                'sankhya' : form.cleaned_data.get('p_sankhya'),
                'pragati': form.cleaned_data.get('p_pragati'),
                'kaifiyat': form.cleaned_data.get('p_kaifiyat'),
            }
            objects_to_create.append(AnugamanBibaran(**p_data))
        
            s_data = {
                'type' : 'supermarket',
                'patak' : form.cleaned_data.get('s_patak'),
                'sankhya' : form.cleaned_data.get('s_sankhya'),
                'pragati': form.cleaned_data.get('s_pragati'),
                'kaifiyat': form.cleaned_data.get('s_kaifiyat'),
            }
            objects_to_create.append(AnugamanBibaran(**s_data))
            
            g_data = {
                'type' : 'godam',
                'patak' : form.cleaned_data.get('g_patak'),
                'sankhya' : form.cleaned_data.get('g_sankhya'),
                'pragati': form.cleaned_data.get('g_pragati'),
                'kaifiyat': form.cleaned_data.get('g_kaifiyat'),
            }
            objects_to_create.append(AnugamanBibaran(**g_data))
            
            h_data = {
                'type' : 'hotel',
                'patak' : form.cleaned_data.get('h_patak'),
                'sankhya' : form.cleaned_data.get('h_sankhya'),
                'pragati': form.cleaned_data.get('h_pragati'),
                'kaifiyat': form.cleaned_data.get('h_kaifiyat'),
            }
            objects_to_create.append(AnugamanBibaran(**h_data))
            
            d_data = {
                'type' : 'dana',
                'patak' : form.cleaned_data.get('d_patak'),
                'sankhya' : form.cleaned_data.get('d_sankhya'),
                'pragati': form.cleaned_data.get('d_pragati'),
                'kaifiyat': form.cleaned_data.get('d_kaifiyat'),
            }
            objects_to_create.append(AnugamanBibaran(**d_data))
            
            a_data = {
                'type' : 'anya',
                'patak' : form.cleaned_data.get('a_patak'),
                'sankhya' : form.cleaned_data.get('a_sankhya'),
                'pragati': form.cleaned_data.get('a_pragati'),
                'kaifiyat': form.cleaned_data.get('a_kaifiyat'),
            }
            objects_to_create.append(AnugamanBibaran(**a_data))

            AnugamanBibaran.objects.bulk_create(objects_to_create)
            
            return HttpResponse("data saved")
    else:
        form = AnugamanBibaranForm()
    context = {'form': form}
    return render(request, 'forms/anugaman_bibaran/newentry.html', context)


def logobitaran(request):
    """views for होटल स्तरीकरण लोगो वितरण सम्बन्धि विवरण"""
    
    if request.method == 'POST':
        form = LogobitaranForm(request.POST)
        if form.is_valid():
            objects_to_create = []
            
            g_data = {
                'type': 'green',
                'c_pragati': form.cleaned_data.get('g_c_pragati'),
                'h_pragati1': form.cleaned_data.get('g_h_pragati1'),
                'h_pragati2': form.cleaned_data.get('g_h_pragati2'),
                'kaifiyat': form.cleaned_data.get('g_kaifiyat'),
            }
            objects_to_create.append(Logobitaran(**g_data))
            
            y1_data = {
                'type': 'yellow1',
                'c_pragati': form.cleaned_data.get('y1_c_pragati'),
                'h_pragati1': form.cleaned_data.get('y1_h_pragati1'),
                'h_pragati2': form.cleaned_data.get('y1_h_pragati2'),
                'kaifiyat': form.cleaned_data.get('y1_kaifiyat'),
            }
            objects_to_create.append(Logobitaran(**y1_data))
            
            y2_data = {
                'type': 'yellow2',
                'c_pragati': form.cleaned_data.get('y2_c_pragati'),
                'h_pragati1': form.cleaned_data.get('y2_h_pragati1'),
                'h_pragati2': form.cleaned_data.get('y2_h_pragati2'),
                'kaifiyat': form.cleaned_data.get('y2_kaifiyat'),
            }
            objects_to_create.append(Logobitaran(**y2_data))
            
            r_data = {
                'type': 'red',
                'c_pragati': form.cleaned_data.get('r_c_pragati'),
                'h_pragati1': form.cleaned_data.get('r_h_pragati1'),
                'h_pragati2': form.cleaned_data.get('r_h_pragati2'),
                'kaifiyat': form.cleaned_data.get('r_kaifiyat'),
            }
            objects_to_create.append(Logobitaran(**r_data))
            
            Logobitaran.objects.bulk_create(objects_to_create)
            
            return HttpResponse("data saved")
    else:
        form = LogobitaranForm()
    context = {'form': form}
    return render(request, 'forms/logobitaran_bibaran/newentry.html', context)


def namuna_bisleysan(request):
    """views for खाद्य तथा दाना नमुना विश्लेषण विवरण"""
    
    data = {
        'ekai': commons.EKAI_CHOICES,
    }
    
    if request.method == 'POST':
        form = NamunaBisleysanForm(request.POST)
        if form.is_valid():
            objects_to_create = []
            
            m_data = {
                'type': 'milk',
                'ekai': form.cleaned_data.get('m_ekai'),
                'lakshya': form.cleaned_data.get('m_lakshya'),
                'pragati1': form.cleaned_data.get('m_pragati1'),
                'mahina_pragati': form.cleaned_data.get('m_mahina_pragati'),
                'sankhya': form.cleaned_data.get('m_sankhya'),
                'parameter': form.cleaned_data.get('m_parameter'),
                'pragati2': form.cleaned_data.get('m_pragati2'),
                'pratisat': form.cleaned_data.get('m_pratisat'),
                'kaifiyat': form.cleaned_data.get('m_kaifiyat'),
            }
            objects_to_create.append(NamunaBisleysan(**m_data))
            
            o_data = {
                'type': 'oil',
                'ekai': form.cleaned_data.get('o_ekai'),
                'lakshya': form.cleaned_data.get('o_lakshya'),
                'pragati1': form.cleaned_data.get('o_pragati1'),
                'mahina_pragati': form.cleaned_data.get('o_mahina_pragati'),
                'sankhya': form.cleaned_data.get('o_sankhya'),
                'parameter': form.cleaned_data.get('o_parameter'),
                'pragati2': form.cleaned_data.get('o_pragati2'),
                'pratisat': form.cleaned_data.get('o_pratisat'),
                'kaifiyat': form.cleaned_data.get('o_kaifiyat'),
            }
            objects_to_create.append(NamunaBisleysan(**o_data))
            
            f_data = {
                'type': 'fruits',
                'ekai': form.cleaned_data.get('f_ekai'),
                'lakshya': form.cleaned_data.get('f_lakshya'),
                'pragati1': form.cleaned_data.get('f_pragati1'),
                'mahina_pragati': form.cleaned_data.get('f_mahina_pragati'),
                'sankhya': form.cleaned_data.get('f_sankhya'),
                'parameter': form.cleaned_data.get('f_parameter'),
                'pragati2': form.cleaned_data.get('f_pragati2'),
                'pratisat': form.cleaned_data.get('f_pratisat'),
                'kaifiyat': form.cleaned_data.get('f_kaifiyat'),
            }
            objects_to_create.append(NamunaBisleysan(**f_data))
            
            s_data = {
                'type': 'spice',
                'ekai': form.cleaned_data.get('s_ekai'),
                'lakshya': form.cleaned_data.get('s_lakshya'),
                'pragati1': form.cleaned_data.get('s_pragati1'),
                'mahina_pragati': form.cleaned_data.get('s_mahina_pragati'),
                'sankhya': form.cleaned_data.get('s_sankhya'),
                'parameter': form.cleaned_data.get('s_parameter'),
                'pragati2': form.cleaned_data.get('s_pragati2'),
                'pratisat': form.cleaned_data.get('s_pratisat'),
                'kaifiyat': form.cleaned_data.get('s_kaifiyat'),
            }
            objects_to_create.append(NamunaBisleysan(**s_data))
            
            t_data = {
                'type': 'tea',
                'ekai': form.cleaned_data.get('t_ekai'),
                'lakshya': form.cleaned_data.get('t_lakshya'),
                'pragati1': form.cleaned_data.get('t_pragati1'),
                'mahina_pragati': form.cleaned_data.get('t_mahina_pragati'),
                'sankhya': form.cleaned_data.get('t_sankhya'),
                'parameter': form.cleaned_data.get('t_parameter'),
                'pragati2': form.cleaned_data.get('t_pragati2'),
                'pratisat': form.cleaned_data.get('t_pratisat'),
                'kaifiyat': form.cleaned_data.get('t_kaifiyat'),
            }
            objects_to_create.append(NamunaBisleysan(**t_data))
            
            sa_data = {
                'type': 'salt',
                'ekai': form.cleaned_data.get('sa_ekai'),
                'lakshya': form.cleaned_data.get('sa_lakshya'),
                'pragati1': form.cleaned_data.get('sa_pragati1'),
                'mahina_pragati': form.cleaned_data.get('sa_mahina_pragati'),
                'sankhya': form.cleaned_data.get('sa_sankhya'),
                'parameter': form.cleaned_data.get('sa_parameter'),
                'pragati2': form.cleaned_data.get('sa_pragati2'),
                'pratisat': form.cleaned_data.get('sa_pratisat'),
                'kaifiyat': form.cleaned_data.get('sa_kaifiyat'),
            }
            objects_to_create.append(NamunaBisleysan(**sa_data))
            
            k_data = {
                'type': 'khadanna',
                'ekai': form.cleaned_data.get('k_ekai'),
                'lakshya': form.cleaned_data.get('k_lakshya'),
                'pragati1': form.cleaned_data.get('k_pragati1'),
                'mahina_pragati': form.cleaned_data.get('k_mahina_pragati'),
                'sankhya': form.cleaned_data.get('k_sankhya'),
                'parameter': form.cleaned_data.get('k_parameter'),
                'pragati2': form.cleaned_data.get('k_pragati2'),
                'pratisat': form.cleaned_data.get('k_pratisat'),
                'kaifiyat': form.cleaned_data.get('k_kaifiyat'),
            }
            objects_to_create.append(NamunaBisleysan(**k_data))
            
            w_data = {
                'type': 'water',
                'ekai': form.cleaned_data.get('w_ekai'),
                'lakshya': form.cleaned_data.get('w_lakshya'),
                'pragati1': form.cleaned_data.get('w_pragati1'),
                'mahina_pragati': form.cleaned_data.get('w_mahina_pragati'),
                'sankhya': form.cleaned_data.get('w_sankhya'),
                'parameter': form.cleaned_data.get('w_parameter'),
                'pragati2': form.cleaned_data.get('w_pragati2'),
                'pratisat': form.cleaned_data.get('w_pratisat'),
                'kaifiyat': form.cleaned_data.get('w_kaifiyat'),
            }
            objects_to_create.append(NamunaBisleysan(**w_data))
            
            sw_data = {
                'type': 'sweets',
                'ekai': form.cleaned_data.get('sw_ekai'),
                'lakshya': form.cleaned_data.get('sw_lakshya'),
                'pragati1': form.cleaned_data.get('sw_pragati1'),
                'mahina_pragati': form.cleaned_data.get('sw_mahina_pragati'),
                'sankhya': form.cleaned_data.get('sw_sankhya'),
                'parameter': form.cleaned_data.get('sw_parameter'),
                'pragati2': form.cleaned_data.get('sw_pragati2'),
                'pratisat': form.cleaned_data.get('sw_pratisat'),
                'kaifiyat': form.cleaned_data.get('sw_kaifiyat'),
            }
            objects_to_create.append(NamunaBisleysan(**sw_data))
            
            c_data = {
                'type': 'confectionery',
                'ekai': form.cleaned_data.get('c_ekai'),
                'lakshya': form.cleaned_data.get('c_lakshya'),
                'pragati1': form.cleaned_data.get('c_pragati1'),
                'mahina_pragati': form.cleaned_data.get('c_mahina_pragati'),
                'sankhya': form.cleaned_data.get('c_sankhya'),
                'parameter': form.cleaned_data.get('c_parameter'),
                'pragati2': form.cleaned_data.get('c_pragati2'),
                'pratisat': form.cleaned_data.get('c_pratisat'),
                'kaifiyat': form.cleaned_data.get('c_kaifiyat'),
            }
            objects_to_create.append(NamunaBisleysan(**c_data))
            
            me_data = {
                'type': 'meat',
                'ekai': form.cleaned_data.get('me_ekai'),
                'lakshya': form.cleaned_data.get('me_lakshya'),
                'pragati1': form.cleaned_data.get('me_pragati1'),
                'mahina_pragati': form.cleaned_data.get('me_mahina_pragati'),
                'sankhya': form.cleaned_data.get('me_sankhya'),
                'parameter': form.cleaned_data.get('me_parameter'),
                'pragati2': form.cleaned_data.get('me_pragati2'),
                'pratisat': form.cleaned_data.get('me_pratisat'),
                'kaifiyat': form.cleaned_data.get('me_kaifiyat'),
            }
            objects_to_create.append(NamunaBisleysan(**me_data))
            
            ot_data = {
                'type': 'others',
                'ekai': form.cleaned_data.get('ot_ekai'),
                'lakshya': form.cleaned_data.get('ot_lakshya'),
                'pragati1': form.cleaned_data.get('ot_pragati1'),
                'mahina_pragati': form.cleaned_data.get('ot_mahina_pragati'),
                'sankhya': form.cleaned_data.get('ot_sankhya'),
                'parameter': form.cleaned_data.get('ot_parameter'),
                'pragati2': form.cleaned_data.get('ot_pragati2'),
                'pratisat': form.cleaned_data.get('ot_pratisat'),
                'kaifiyat': form.cleaned_data.get('ot_kaifiyat'),
            }
            objects_to_create.append(NamunaBisleysan(**ot_data))
            
            g_data = {
                'type': 'grain',
                'ekai': form.cleaned_data.get('g_ekai'),
                'lakshya': form.cleaned_data.get('g_lakshya'),
                'pragati1': form.cleaned_data.get('g_pragati1'),
                'mahina_pragati': form.cleaned_data.get('g_mahina_pragati'),
                'sankhya': form.cleaned_data.get('g_sankhya'),
                'parameter': form.cleaned_data.get('g_parameter'),
                'pragati2': form.cleaned_data.get('g_pragati2'),
                'pratisat': form.cleaned_data.get('g_pratisat'),
                'kaifiyat': form.cleaned_data.get('g_kaifiyat'),
            }
            objects_to_create.append(NamunaBisleysan(**g_data))
            
            NamunaBisleysan.objects.bulk_create(objects_to_create)
            
            return HttpResponse("data saved")
    else:
        form = NamunaBisleysanForm()
    context = {'form': form, 'data': data}
    return render(request, 'forms/bisleysan_bibaran/newentry.html', context)


def prayogsala_bisleysan(request):
    """views for प्रयोगशाला विश्लेषण प्रतिवेदन सारांश"""
    
    if request.method == 'POST':
        form = PrayogsalaBisleysanForm(request.POST)
        if form.is_valid():
            objects_to_create = []
            
            m_data = {
                'type': 'milk',
                'b_sankhya': form.cleaned_data.get('m_b_sankhya'),
                'b_pratikul': form.cleaned_data.get('m_b_pratikul'),
                'u_sankhya': form.cleaned_data.get('m_u_sankhya'),
                'u_pratikul': form.cleaned_data.get('m_u_pratikul'),
                'ay_sankhya': form.cleaned_data.get('m_ay_sankhya'),
                'ay_pratikul': form.cleaned_data.get('m_ay_pratikul'),
                'v_sankhya': form.cleaned_data.get('m_v_sankhya'),
                'v_pratikul': form.cleaned_data.get('m_v_pratikul'),
                'k_sankhya': form.cleaned_data.get('m_k_sankhya'),
                'k_pratikul': form.cleaned_data.get('m_k_pratikul'),
                'a_sankhya': form.cleaned_data.get('m_a_sankhya'),
                'a_pratikul': form.cleaned_data.get('m_a_pratikul'),
                'kul_sankhya': form.cleaned_data.get('m_kul_sankhya'),
                'kul_pratikul': form.cleaned_data.get('m_kul_pratikul'),
                'sample': form.cleaned_data.get('m_sample'),
                'kaifiyat': form.cleaned_data.get('m_kaifiyat'),
            }
            objects_to_create.append(PrayogsalaBisleysan(**m_data))
            
            o_data = {
                'type': 'oil',
                'b_sankhya': form.cleaned_data.get('o_b_sankhya'),
                'b_pratikul': form.cleaned_data.get('o_b_pratikul'),
                'u_sankhya': form.cleaned_data.get('o_u_sankhya'),
                'u_pratikul': form.cleaned_data.get('o_u_pratikul'),
                'ay_sankhya': form.cleaned_data.get('o_ay_sankhya'),
                'ay_pratikul': form.cleaned_data.get('o_ay_pratikul'),
                'v_sankhya': form.cleaned_data.get('o_v_sankhya'),
                'v_pratikul': form.cleaned_data.get('o_v_pratikul'),
                'k_sankhya': form.cleaned_data.get('o_k_sankhya'),
                'k_pratikul': form.cleaned_data.get('o_k_pratikul'),
                'a_sankhya': form.cleaned_data.get('o_a_sankhya'),
                'a_pratikul': form.cleaned_data.get('o_a_pratikul'),
                'kul_sankhya': form.cleaned_data.get('o_kul_sankhya'),
                'kul_pratikul': form.cleaned_data.get('o_kul_pratikul'),
                'sample': form.cleaned_data.get('o_sample'),
                'kaifiyat': form.cleaned_data.get('o_kaifiyat'),
            }
            objects_to_create.append(PrayogsalaBisleysan(**o_data))
            
            f_data = {
                'type': 'fruits',
                'b_sankhya': form.cleaned_data.get('f_b_sankhya'),
                'b_pratikul': form.cleaned_data.get('f_b_pratikul'),
                'u_sankhya': form.cleaned_data.get('f_u_sankhya'),
                'u_pratikul': form.cleaned_data.get('f_u_pratikul'),
                'ay_sankhya': form.cleaned_data.get('f_ay_sankhya'),
                'ay_pratikul': form.cleaned_data.get('f_ay_pratikul'),
                'v_sankhya': form.cleaned_data.get('f_v_sankhya'),
                'v_pratikul': form.cleaned_data.get('f_v_pratikul'),
                'k_sankhya': form.cleaned_data.get('f_k_sankhya'),
                'k_pratikul': form.cleaned_data.get('f_k_pratikul'),
                'a_sankhya': form.cleaned_data.get('f_a_sankhya'),
                'a_pratikul': form.cleaned_data.get('f_a_pratikul'),
                'kul_sankhya': form.cleaned_data.get('f_kul_sankhya'),
                'kul_pratikul': form.cleaned_data.get('f_kul_pratikul'),
                'sample': form.cleaned_data.get('f_sample'),
                'kaifiyat': form.cleaned_data.get('f_kaifiyat'),
            }
            objects_to_create.append(PrayogsalaBisleysan(**f_data))
            
            s_data = {
                'type': 'spice',
                'b_sankhya': form.cleaned_data.get('s_b_sankhya'),
                'b_pratikul': form.cleaned_data.get('s_b_pratikul'),
                'u_sankhya': form.cleaned_data.get('s_u_sankhya'),
                'u_pratikul': form.cleaned_data.get('s_u_pratikul'),
                'ay_sankhya': form.cleaned_data.get('s_ay_sankhya'),
                'ay_pratikul': form.cleaned_data.get('s_ay_pratikul'),
                'v_sankhya': form.cleaned_data.get('s_v_sankhya'),
                'v_pratikul': form.cleaned_data.get('s_v_pratikul'),
                'k_sankhya': form.cleaned_data.get('s_k_sankhya'),
                'k_pratikul': form.cleaned_data.get('s_k_pratikul'),
                'a_sankhya': form.cleaned_data.get('s_a_sankhya'),
                'a_pratikul': form.cleaned_data.get('s_a_pratikul'),
                'kul_sankhya': form.cleaned_data.get('s_kul_sankhya'),
                'kul_pratikul': form.cleaned_data.get('s_kul_pratikul'),
                'sample': form.cleaned_data.get('s_sample'),
                'kaifiyat': form.cleaned_data.get('s_kaifiyat'),
            }
            objects_to_create.append(PrayogsalaBisleysan(**s_data))
            
            t_data = {
                'type': 'tea',
                'b_sankhya': form.cleaned_data.get('t_b_sankhya'),
                'b_pratikul': form.cleaned_data.get('t_b_pratikul'),
                'u_sankhya': form.cleaned_data.get('t_u_sankhya'),
                'u_pratikul': form.cleaned_data.get('t_u_pratikul'),
                'ay_sankhya': form.cleaned_data.get('t_ay_sankhya'),
                'ay_pratikul': form.cleaned_data.get('t_ay_pratikul'),
                'v_sankhya': form.cleaned_data.get('t_v_sankhya'),
                'v_pratikul': form.cleaned_data.get('t_v_pratikul'),
                'k_sankhya': form.cleaned_data.get('t_k_sankhya'),
                'k_pratikul': form.cleaned_data.get('t_k_pratikul'),
                'a_sankhya': form.cleaned_data.get('t_a_sankhya'),
                'a_pratikul': form.cleaned_data.get('t_a_pratikul'),
                'kul_sankhya': form.cleaned_data.get('t_kul_sankhya'),
                'kul_pratikul': form.cleaned_data.get('t_kul_pratikul'),
                'sample': form.cleaned_data.get('t_sample'),
                'kaifiyat': form.cleaned_data.get('t_kaifiyat'),
            }
            objects_to_create.append(PrayogsalaBisleysan(**t_data))
            
            sa_data = {
                'type': 'salt',
                'b_sankhya': form.cleaned_data.get('sa_b_sankhya'),
                'b_pratikul': form.cleaned_data.get('sa_b_pratikul'),
                'u_sankhya': form.cleaned_data.get('sa_u_sankhya'),
                'u_pratikul': form.cleaned_data.get('sa_u_pratikul'),
                'ay_sankhya': form.cleaned_data.get('sa_ay_sankhya'),
                'ay_pratikul': form.cleaned_data.get('sa_ay_pratikul'),
                'v_sankhya': form.cleaned_data.get('sa_v_sankhya'),
                'v_pratikul': form.cleaned_data.get('sa_v_pratikul'),
                'k_sankhya': form.cleaned_data.get('sa_k_sankhya'),
                'k_pratikul': form.cleaned_data.get('sa_k_pratikul'),
                'a_sankhya': form.cleaned_data.get('sa_a_sankhya'),
                'a_pratikul': form.cleaned_data.get('sa_a_pratikul'),
                'kul_sankhya': form.cleaned_data.get('sa_kul_sankhya'),
                'kul_pratikul': form.cleaned_data.get('sa_kul_pratikul'),
                'sample': form.cleaned_data.get('sa_sample'),
                'kaifiyat': form.cleaned_data.get('sa_kaifiyat'),
            }
            objects_to_create.append(PrayogsalaBisleysan(**sa_data))
            
            k_data = {
                'type': 'khadanna',
                'b_sankhya': form.cleaned_data.get('k_b_sankhya'),
                'b_pratikul': form.cleaned_data.get('k_b_pratikul'),
                'u_sankhya': form.cleaned_data.get('k_u_sankhya'),
                'u_pratikul': form.cleaned_data.get('k_u_pratikul'),
                'ay_sankhya': form.cleaned_data.get('k_ay_sankhya'),
                'ay_pratikul': form.cleaned_data.get('k_ay_pratikul'),
                'v_sankhya': form.cleaned_data.get('k_v_sankhya'),
                'v_pratikul': form.cleaned_data.get('k_v_pratikul'),
                'k_sankhya': form.cleaned_data.get('k_k_sankhya'),
                'k_pratikul': form.cleaned_data.get('k_k_pratikul'),
                'a_sankhya': form.cleaned_data.get('k_a_sankhya'),
                'a_pratikul': form.cleaned_data.get('k_a_pratikul'),
                'kul_sankhya': form.cleaned_data.get('k_kul_sankhya'),
                'kul_pratikul': form.cleaned_data.get('k_kul_pratikul'),
                'sample': form.cleaned_data.get('k_sample'),
                'kaifiyat': form.cleaned_data.get('k_kaifiyat'),
            }
            objects_to_create.append(PrayogsalaBisleysan(**k_data))
            
            w_data = {
                'type': 'water',
                'b_sankhya': form.cleaned_data.get('w_b_sankhya'),
                'b_pratikul': form.cleaned_data.get('w_b_pratikul'),
                'u_sankhya': form.cleaned_data.get('w_u_sankhya'),
                'u_pratikul': form.cleaned_data.get('w_u_pratikul'),
                'ay_sankhya': form.cleaned_data.get('w_ay_sankhya'),
                'ay_pratikul': form.cleaned_data.get('w_ay_pratikul'),
                'v_sankhya': form.cleaned_data.get('w_v_sankhya'),
                'v_pratikul': form.cleaned_data.get('w_v_pratikul'),
                'k_sankhya': form.cleaned_data.get('w_k_sankhya'),
                'k_pratikul': form.cleaned_data.get('w_k_pratikul'),
                'a_sankhya': form.cleaned_data.get('w_a_sankhya'),
                'a_pratikul': form.cleaned_data.get('w_a_pratikul'),
                'kul_sankhya': form.cleaned_data.get('w_kul_sankhya'),
                'kul_pratikul': form.cleaned_data.get('w_kul_pratikul'),
                'sample': form.cleaned_data.get('w_sample'),
                'kaifiyat': form.cleaned_data.get('w_kaifiyat'),
            }
            objects_to_create.append(PrayogsalaBisleysan(**w_data))
            
            sw_data = {
                'type': 'sweets',
                'b_sankhya': form.cleaned_data.get('sw_b_sankhya'),
                'b_pratikul': form.cleaned_data.get('sw_b_pratikul'),
                'u_sankhya': form.cleaned_data.get('sw_u_sankhya'),
                'u_pratikul': form.cleaned_data.get('sw_u_pratikul'),
                'ay_sankhya': form.cleaned_data.get('sw_ay_sankhya'),
                'ay_pratikul': form.cleaned_data.get('sw_ay_pratikul'),
                'v_sankhya': form.cleaned_data.get('sw_v_sankhya'),
                'v_pratikul': form.cleaned_data.get('sw_v_pratikul'),
                'k_sankhya': form.cleaned_data.get('sw_k_sankhya'),
                'k_pratikul': form.cleaned_data.get('sw_k_pratikul'),
                'a_sankhya': form.cleaned_data.get('sw_a_sankhya'),
                'a_pratikul': form.cleaned_data.get('sw_a_pratikul'),
                'kul_sankhya': form.cleaned_data.get('sw_kul_sankhya'),
                'kul_pratikul': form.cleaned_data.get('sw_kul_pratikul'),
                'sample': form.cleaned_data.get('sw_sample'),
                'kaifiyat': form.cleaned_data.get('sw_kaifiyat'),
            }
            objects_to_create.append(PrayogsalaBisleysan(**sw_data))
            
            c_data = {
                'type': 'confectionery',
                'b_sankhya': form.cleaned_data.get('c_b_sankhya'),
                'b_pratikul': form.cleaned_data.get('c_b_pratikul'),
                'u_sankhya': form.cleaned_data.get('c_u_sankhya'),
                'u_pratikul': form.cleaned_data.get('c_u_pratikul'),
                'ay_sankhya': form.cleaned_data.get('c_ay_sankhya'),
                'ay_pratikul': form.cleaned_data.get('c_ay_pratikul'),
                'v_sankhya': form.cleaned_data.get('c_v_sankhya'),
                'v_pratikul': form.cleaned_data.get('c_v_pratikul'),
                'k_sankhya': form.cleaned_data.get('c_k_sankhya'),
                'k_pratikul': form.cleaned_data.get('c_k_pratikul'),
                'a_sankhya': form.cleaned_data.get('c_a_sankhya'),
                'a_pratikul': form.cleaned_data.get('c_a_pratikul'),
                'kul_sankhya': form.cleaned_data.get('c_kul_sankhya'),
                'kul_pratikul': form.cleaned_data.get('c_kul_pratikul'),
                'sample': form.cleaned_data.get('c_sample'),
                'kaifiyat': form.cleaned_data.get('c_kaifiyat'),
            }
            objects_to_create.append(PrayogsalaBisleysan(**c_data))
            
            me_data = {
                'type': 'meat',
                'b_sankhya': form.cleaned_data.get('me_b_sankhya'),
                'b_pratikul': form.cleaned_data.get('me_b_pratikul'),
                'u_sankhya': form.cleaned_data.get('me_u_sankhya'),
                'u_pratikul': form.cleaned_data.get('me_u_pratikul'),
                'ay_sankhya': form.cleaned_data.get('me_ay_sankhya'),
                'ay_pratikul': form.cleaned_data.get('me_ay_pratikul'),
                'v_sankhya': form.cleaned_data.get('me_v_sankhya'),
                'v_pratikul': form.cleaned_data.get('me_v_pratikul'),
                'k_sankhya': form.cleaned_data.get('me_k_sankhya'),
                'k_pratikul': form.cleaned_data.get('me_k_pratikul'),
                'a_sankhya': form.cleaned_data.get('me_a_sankhya'),
                'a_pratikul': form.cleaned_data.get('me_a_pratikul'),
                'kul_sankhya': form.cleaned_data.get('me_kul_sankhya'),
                'kul_pratikul': form.cleaned_data.get('me_kul_pratikul'),
                'sample': form.cleaned_data.get('me_sample'),
                'kaifiyat': form.cleaned_data.get('me_kaifiyat'),
            }
            objects_to_create.append(PrayogsalaBisleysan(**me_data))
            
            g_data = {
                'type': 'grain',
                'b_sankhya': form.cleaned_data.get('g_b_sankhya'),
                'b_pratikul': form.cleaned_data.get('g_b_pratikul'),
                'u_sankhya': form.cleaned_data.get('g_u_sankhya'),
                'u_pratikul': form.cleaned_data.get('g_u_pratikul'),
                'ay_sankhya': form.cleaned_data.get('g_ay_sankhya'),
                'ay_pratikul': form.cleaned_data.get('g_ay_pratikul'),
                'v_sankhya': form.cleaned_data.get('g_v_sankhya'),
                'v_pratikul': form.cleaned_data.get('g_v_pratikul'),
                'k_sankhya': form.cleaned_data.get('g_k_sankhya'),
                'k_pratikul': form.cleaned_data.get('g_k_pratikul'),
                'a_sankhya': form.cleaned_data.get('g_a_sankhya'),
                'a_pratikul': form.cleaned_data.get('g_a_pratikul'),
                'kul_sankhya': form.cleaned_data.get('g_kul_sankhya'),
                'kul_pratikul': form.cleaned_data.get('g_kul_pratikul'),
                'sample': form.cleaned_data.get('g_sample'),
                'kaifiyat': form.cleaned_data.get('g_kaifiyat'),
            }
            objects_to_create.append(PrayogsalaBisleysan(**g_data))
            
            ot_data = {
                'type': 'others',
                'b_sankhya': form.cleaned_data.get('ot_b_sankhya'),
                'b_pratikul': form.cleaned_data.get('ot_b_pratikul'),
                'u_sankhya': form.cleaned_data.get('ot_u_sankhya'),
                'u_pratikul': form.cleaned_data.get('ot_u_pratikul'),
                'ay_sankhya': form.cleaned_data.get('ot_ay_sankhya'),
                'ay_pratikul': form.cleaned_data.get('ot_ay_pratikul'),
                'v_sankhya': form.cleaned_data.get('ot_v_sankhya'),
                'v_pratikul': form.cleaned_data.get('ot_v_pratikul'),
                'k_sankhya': form.cleaned_data.get('ot_k_sankhya'),
                'k_pratikul': form.cleaned_data.get('ot_k_pratikul'),
                'a_sankhya': form.cleaned_data.get('ot_a_sankhya'),
                'a_pratikul': form.cleaned_data.get('ot_a_pratikul'),
                'kul_sankhya': form.cleaned_data.get('ot_kul_sankhya'),
                'kul_pratikul': form.cleaned_data.get('ot_kul_pratikul'),
                'sample': form.cleaned_data.get('ot_sample'),
                'kaifiyat': form.cleaned_data.get('ot_kaifiyat'),
            }
            objects_to_create.append(PrayogsalaBisleysan(**ot_data))
            
            PrayogsalaBisleysan.objects.bulk_create(objects_to_create)
            
            return HttpResponse("data saved")
    else:
        form = PrayogsalaBisleysanForm()
    context = {'form': form}
    return render(request, 'forms/pratibedan_bibaran/newentry.html', context)


def khadya1(request):
    """views for खाद्य तथा दाना अनुज्ञा पत्र जारी"""
    
    if request.method == 'POST':
        form = PatraJariForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("ok")
    else:
        form = PatraJariForm()
    context = {'form': form}
    return render(request, 'forms/registration/new.html', context)


def khadya2(request):
    """views for खाद्य तथा दाना अनुज्ञा पत्र नविकरण"""
    
    if request.method == 'POST':
        form = PatraNabikaranForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("ok")
    else:
        form = PatraNabikaranForm()
    context = {'form': form}
    return render(request, 'forms/registration/renew.html')


def udyog(request):
    """views for उद्योग सिफारिस"""
    
    if request.method == 'POST':
        form = UdyogSifarisForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("ok")
    else:
        form = UdyogSifarisForm()
    context = {'form': form}
    return render(request, 'forms/registration/udyog.html')


def aayat(request):
    """views for आयात निर्यात गुण प्रमाणिकरण"""
    
    data = {
        'ekai': commons.EKAI_CHOICES,
    }
    
    if request.method == 'POST':
        form = AayatNiryatForm(request.POST)
        if form.is_valid():
            objects_to_create = []
            
            m_data = {
                'type': 'milk',
                'ekai': form.cleaned_data.get('m_ekai'),
                'b_lakshya': form.cleaned_data.get('m_b_lakshya'),
                'c_lakshya': form.cleaned_data.get('m_c_lakshya'),
                'c_pragati': form.cleaned_data.get('m_c_pragati'),
                'm_pragati': form.cleaned_data.get('m_m_pragati'),
                'pratikul_n': form.cleaned_data.get('m_pratikul_n'),
                'pratikul_p': form.cleaned_data.get('m_pratikul_p'),
                'h_pragati': form.cleaned_data.get('m_h_pragati'),
                'h_pratisat': form.cleaned_data.get('m_h_pratisat'),
                'kaifiyat': form.cleaned_data.get('m_kaifiyat'),
            }
            objects_to_create.append(AayatNiryat(**m_data))
            
            o_data = {
                'type': 'oil',
                'ekai': form.cleaned_data.get('o_ekai'),
                'b_lakshya': form.cleaned_data.get('o_b_lakshya'),
                'c_lakshya': form.cleaned_data.get('o_c_lakshya'),
                'c_pragati': form.cleaned_data.get('o_c_pragati'),
                'm_pragati': form.cleaned_data.get('o_m_pragati'),
                'pratikul_n': form.cleaned_data.get('o_pratikul_n'),
                'pratikul_p': form.cleaned_data.get('o_pratikul_p'),
                'h_pragati': form.cleaned_data.get('o_h_pragati'),
                'h_pratisat': form.cleaned_data.get('o_h_pratisat'),
                'kaifiyat': form.cleaned_data.get('o_kaifiyat'),
            }
            objects_to_create.append(AayatNiryat(**o_data))
            
            f_data = {
                'type': 'fruits',
                'ekai': form.cleaned_data.get('f_ekai'),
                'b_lakshya': form.cleaned_data.get('f_b_lakshya'),
                'c_lakshya': form.cleaned_data.get('f_c_lakshya'),
                'c_pragati': form.cleaned_data.get('f_c_pragati'),
                'm_pragati': form.cleaned_data.get('f_m_pragati'),
                'pratikul_n': form.cleaned_data.get('f_pratikul_n'),
                'pratikul_p': form.cleaned_data.get('f_pratikul_p'),
                'h_pragati': form.cleaned_data.get('f_h_pragati'),
                'h_pratisat': form.cleaned_data.get('f_h_pratisat'),
                'kaifiyat': form.cleaned_data.get('f_kaifiyat'),
            }
            objects_to_create.append(AayatNiryat(**f_data))
            
            s_data = {
                'type': 'spice',
                'ekai': form.cleaned_data.get('s_ekai'),
                'b_lakshya': form.cleaned_data.get('s_b_lakshya'),
                'c_lakshya': form.cleaned_data.get('s_c_lakshya'),
                'c_pragati': form.cleaned_data.get('s_c_pragati'),
                'm_pragati': form.cleaned_data.get('s_m_pragati'),
                'pratikul_n': form.cleaned_data.get('s_pratikul_n'),
                'pratikul_p': form.cleaned_data.get('s_pratikul_p'),
                'h_pragati': form.cleaned_data.get('s_h_pragati'),
                'h_pratisat': form.cleaned_data.get('s_h_pratisat'),
                'kaifiyat': form.cleaned_data.get('s_kaifiyat'),
            }
            objects_to_create.append(AayatNiryat(**s_data))
            
            t_data = {
                'type': 'tea',
                'ekai': form.cleaned_data.get('t_ekai'),
                'b_lakshya': form.cleaned_data.get('t_b_lakshya'),
                'c_lakshya': form.cleaned_data.get('t_c_lakshya'),
                'c_pragati': form.cleaned_data.get('t_c_pragati'),
                'm_pragati': form.cleaned_data.get('t_m_pragati'),
                'pratikul_n': form.cleaned_data.get('t_pratikul_n'),
                'pratikul_p': form.cleaned_data.get('t_pratikul_p'),
                'h_pragati': form.cleaned_data.get('t_h_pragati'),
                'h_pratisat': form.cleaned_data.get('t_h_pratisat'),
                'kaifiyat': form.cleaned_data.get('t_kaifiyat'),
            }
            objects_to_create.append(AayatNiryat(**t_data))
            
            sa_data = {
                'type': 'salt',
                'ekai': form.cleaned_data.get('sa_ekai'),
                'b_lakshya': form.cleaned_data.get('sa_b_lakshya'),
                'c_lakshya': form.cleaned_data.get('sa_c_lakshya'),
                'c_pragati': form.cleaned_data.get('sa_c_pragati'),
                'm_pragati': form.cleaned_data.get('sa_m_pragati'),
                'pratikul_n': form.cleaned_data.get('sa_pratikul_n'),
                'pratikul_p': form.cleaned_data.get('sa_pratikul_p'),
                'h_pragati': form.cleaned_data.get('sa_h_pragati'),
                'h_pratisat': form.cleaned_data.get('sa_h_pratisat'),
                'kaifiyat': form.cleaned_data.get('sa_kaifiyat'),
            }
            objects_to_create.append(AayatNiryat(**sa_data))
            
            k_data = {
                'type': 'khadanna',
                'ekai': form.cleaned_data.get('k_ekai'),
                'b_lakshya': form.cleaned_data.get('k_b_lakshya'),
                'c_lakshya': form.cleaned_data.get('k_c_lakshya'),
                'c_pragati': form.cleaned_data.get('k_c_pragati'),
                'm_pragati': form.cleaned_data.get('k_m_pragati'),
                'pratikul_n': form.cleaned_data.get('k_pratikul_n'),
                'pratikul_p': form.cleaned_data.get('k_pratikul_p'),
                'h_pragati': form.cleaned_data.get('k_h_pragati'),
                'h_pratisat': form.cleaned_data.get('k_h_pratisat'),
                'kaifiyat': form.cleaned_data.get('k_kaifiyat'),
            }
            objects_to_create.append(AayatNiryat(**k_data))
            
            w_data = {
                'type': 'water',
                'ekai': form.cleaned_data.get('w_ekai'),
                'b_lakshya': form.cleaned_data.get('w_b_lakshya'),
                'c_lakshya': form.cleaned_data.get('w_c_lakshya'),
                'c_pragati': form.cleaned_data.get('w_c_pragati'),
                'm_pragati': form.cleaned_data.get('w_m_pragati'),
                'pratikul_n': form.cleaned_data.get('w_pratikul_n'),
                'pratikul_p': form.cleaned_data.get('w_pratikul_p'),
                'h_pragati': form.cleaned_data.get('w_h_pragati'),
                'h_pratisat': form.cleaned_data.get('w_h_pratisat'),
                'kaifiyat': form.cleaned_data.get('w_kaifiyat'),
            }
            objects_to_create.append(AayatNiryat(**w_data))
            
            sw_data = {
                'type': 'sweets',
                'ekai': form.cleaned_data.get('sw_ekai'),
                'b_lakshya': form.cleaned_data.get('sw_b_lakshya'),
                'c_lakshya': form.cleaned_data.get('sw_c_lakshya'),
                'c_pragati': form.cleaned_data.get('sw_c_pragati'),
                'm_pragati': form.cleaned_data.get('sw_m_pragati'),
                'pratikul_n': form.cleaned_data.get('sw_pratikul_n'),
                'pratikul_p': form.cleaned_data.get('sw_pratikul_p'),
                'h_pragati': form.cleaned_data.get('sw_h_pragati'),
                'h_pratisat': form.cleaned_data.get('sw_h_pratisat'),
                'kaifiyat': form.cleaned_data.get('sw_kaifiyat'),
            }
            objects_to_create.append(AayatNiryat(**sw_data))
            
            c_data = {
                'type': 'confectionery',
                'ekai': form.cleaned_data.get('c_ekai'),
                'b_lakshya': form.cleaned_data.get('c_b_lakshya'),
                'c_lakshya': form.cleaned_data.get('c_c_lakshya'),
                'c_pragati': form.cleaned_data.get('c_c_pragati'),
                'm_pragati': form.cleaned_data.get('c_m_pragati'),
                'pratikul_n': form.cleaned_data.get('c_pratikul_n'),
                'pratikul_p': form.cleaned_data.get('c_pratikul_p'),
                'h_pragati': form.cleaned_data.get('c_h_pragati'),
                'h_pratisat': form.cleaned_data.get('c_h_pratisat'),
                'kaifiyat': form.cleaned_data.get('c_kaifiyat'),
            }
            objects_to_create.append(AayatNiryat(**c_data))
            
            me_data = {
                'type': 'meat',
                'ekai': form.cleaned_data.get('me_ekai'),
                'b_lakshya': form.cleaned_data.get('me_b_lakshya'),
                'c_lakshya': form.cleaned_data.get('me_c_lakshya'),
                'c_pragati': form.cleaned_data.get('me_c_pragati'),
                'm_pragati': form.cleaned_data.get('me_m_pragati'),
                'pratikul_n': form.cleaned_data.get('me_pratikul_n'),
                'pratikul_p': form.cleaned_data.get('me_pratikul_p'),
                'h_pragati': form.cleaned_data.get('me_h_pragati'),
                'h_pratisat': form.cleaned_data.get('me_h_pratisat'),
                'kaifiyat': form.cleaned_data.get('me_kaifiyat'),
            }
            objects_to_create.append(AayatNiryat(**me_data))
            
            ot_data = {
                'type': 'others',
                'ekai': form.cleaned_data.get('ot_ekai'),
                'b_lakshya': form.cleaned_data.get('ot_b_lakshya'),
                'c_lakshya': form.cleaned_data.get('ot_c_lakshya'),
                'c_pragati': form.cleaned_data.get('ot_c_pragati'),
                'm_pragati': form.cleaned_data.get('ot_m_pragati'),
                'pratikul_n': form.cleaned_data.get('ot_pratikul_n'),
                'pratikul_p': form.cleaned_data.get('ot_pratikul_p'),
                'h_pragati': form.cleaned_data.get('ot_h_pragati'),
                'h_pratisat': form.cleaned_data.get('ot_h_pratisat'),
                'kaifiyat': form.cleaned_data.get('ot_kaifiyat'),
            }
            objects_to_create.append(AayatNiryat(**ot_data))
            
            g_data = {
                'type': 'grain',
                'ekai': form.cleaned_data.get('g_ekai'),
                'b_lakshya': form.cleaned_data.get('g_b_lakshya'),
                'c_lakshya': form.cleaned_data.get('g_c_lakshya'),
                'c_pragati': form.cleaned_data.get('g_c_pragati'),
                'm_pragati': form.cleaned_data.get('g_m_pragati'),
                'pratikul_n': form.cleaned_data.get('g_pratikul_n'),
                'pratikul_p': form.cleaned_data.get('g_pratikul_p'),
                'h_pragati': form.cleaned_data.get('g_h_pragati'),
                'h_pratisat': form.cleaned_data.get('g_h_pratisat'),
                'kaifiyat': form.cleaned_data.get('g_kaifiyat'),
            }
            objects_to_create.append(AayatNiryat(**g_data))
            
            AayatNiryat.objects.bulk_create(objects_to_create)
            
            return HttpResponse("saved")
    else:
        form = AayatNiryatForm()
    context = {
        'form': form,
        'data': data,
    }
    return render(request, 'forms/import-export/index.html', context)


def ujuri(request):
    """views for उजुरी/गुनासो ब्येवस्थापन"""
    
    if request.method == 'POST':
        form = UjuriGunasoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("data saved")
    else:
        form = UjuriGunasoForm()
    context = {'form': form}
    return render(request, 'forms/gunasho/index.html', context)


def khadya_prasodhan(request):
    """views for खाद्य प्रसोधन, खाद्य पोषण, उद्योग, होटेल, पत्रकार, कार्यशाला आदि"""
    
    if request.method == 'POST':
        k_miti = request.POST.getlist('miti[]')        
        k_abadhi = request.POST.getlist('abadhi[]')
        k_naam = request.POST.getlist('naam[]')
        k_sthan = request.POST.getlist('sthan[]')
        k_m_sankhya = request.POST.getlist('m_sankhya[]')
        k_p_sankhya = request.POST.getlist('p_sankhya[]')
        k_sanyojak = request.POST.getlist('sanyojak[]')
        k_phone = request.POST.getlist('phone[]')
        k_prasikshak = request.POST.getlist('prasikshak[]')
        k_nikaya = request.POST.getlist('nikaya[]')
        k_bisaya = request.POST.getlist('bisaya[]')
        k_kaifiyat = request.POST.getlist('kaifiyat[]')

        for miti, abadhi, naam, sthan, m_sankhya, p_sankhya, sanyojak, phone, prasikshak, nikaya, bisaya, kaifiyat in zip(
            k_miti, k_abadhi, k_naam, k_sthan, k_m_sankhya, k_p_sankhya, k_sanyojak, k_phone, k_prasikshak, k_nikaya, k_bisaya, k_kaifiyat):
            
            form_data = {
                'miti': miti,
                'abadhi': abadhi,
                'naam': naam,
                'sthan': sthan,
                'm_sankhya': m_sankhya,
                'p_sankhya': p_sankhya,
                'sanyojak': sanyojak,
                'phone': phone,
                'prasikshak': prasikshak,
                'nikaya': nikaya,
                'bisaya': bisaya,
                'kaifiyat': kaifiyat
            }
            form = KhadyaPrasodhanForm(form_data)
            if form.is_valid():
                khadya_object = form.save(commit=False)
                khadya_object.save()
        
        
    else:
        form = KhadyaPrasodhanForm()
    context = {'form': form}
    return render(request, 'forms/hotel-patrakar/index.html', context)


def masik_bittiya(request):
    """views for मासिक वित्तिय विवरण"""
    
    if request.method == 'POST':
        form = BittiyaBibaranForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("saved data with modelform")
    else:
        form = BittiyaBibaranForm()
    context = {'form': form}
    return render(request, 'forms/account/summary.html', context)


def masik_pragati(request):
    """views for मासिक प्रगति विवरण"""
    
    data = {
        'months': commons.MONTHS_CHOICES,
        'ekai': commons.EKAI_CHOICES,
        'kharcha': commons.KHARCHA_CHOICES,
    }
    if request.method =='POST':
        months = request.POST.get('months')
        p_kharcha_type = request.POST.getlist('kharcha_type[]')
        p_upasirshak = request.POST.getlist('upasirshak[]')
        p_karya = request.POST.getlist('karya[]')
        p_ekai = request.POST.getlist('ekai[]')
        p_b_lakshya = request.POST.getlist('b_lakshya[]')
        p_m_parinam = request.POST.getlist('m_parinam[]')
        p_t_lakshya = request.POST.getlist('t_lakshya[]')
        p_t_pragati = request.POST.getlist('t_pragati[]')
        p_t_pratisat = request.POST.getlist('t_pratisat[]')
        p_h_pragati = request.POST.getlist('h_pragati[]')
        p_h_pratisat = request.POST.getlist('h_pratisat[]')
        p_kaifiyat = request.POST.getlist('kaifiyat[]')
        
        for kharcha_type, upasirshak, karya, ekai, b_lakshya, m_parinam, t_lakshya, t_pragati, t_pratisat, h_pragati, h_pratisat, kaifiyat in zip(
            p_kharcha_type, p_upasirshak, p_karya, p_ekai, p_b_lakshya, p_m_parinam, p_t_lakshya, p_t_pragati, p_t_pratisat, 
            p_h_pragati, p_h_pratisat, p_kaifiyat
        ):
            form_data = {
                'months': months,
                'kharcha_type': kharcha_type,
                'upasirshak': upasirshak,
                'karya': karya,
                'ekai': ekai,
                'b_lakshya': b_lakshya,
                'm_parinam': m_parinam,
                't_lakshya': t_lakshya,
                't_pragati': t_pragati,
                't_pratisat': t_pratisat,
                'h_pragati': h_pragati,
                'h_pratisat': h_pratisat,
                'kaifiyat': kaifiyat,
            }
            form = MasikPragatiForm(form_data)
            if form.is_valid():
                masik_object = form.save(commit=False)
                masik_object.save()
        return HttpResponse("data saved")
    else:
        form = MasikPragatiForm()
    context = {'form': form, 'data': data}
    return render(request, 'forms/report/summary.html', context)


#-------------------- DETAILS FORM BELOW ---------------------------


def detail_hotel(request):
    """views for detail होटल रेष्टुरेण्टको स्तरकिरण लोगो वितरण"""
    
    data = {
        'logo': commons.DETAIL_LOGO_CHOICES,
    }
    if request.method == 'POST':
        d_naam = request.POST.getlist('naam[]')
        d_logo = request.POST.getlist('logo[]')
        d_thegana = request.POST.getlist('thegana[]')
        d_samparka = request.POST.getlist('samparka[]')
        d_jilla = request.POST.getlist('jilla[]')
        d_j_miti = request.POST.getlist('j_miti[]')
        d_n_miti = request.POST.getlist('n_miti[]')
        d_karyalaya = request.POST.getlist('karyalaya[]')
        d_kaifiyat = request.POST.getlist('kaifiyat[]')
        
        for naam, logo, thegana, samparka, jilla, j_miti, n_miti, karyalaya, kaifiyat in zip(
            d_naam, d_logo, d_thegana, d_samparka, d_jilla, d_j_miti, d_n_miti, d_karyalaya, d_kaifiyat
        ):
            form_data = {
                'naam': naam,
                'logo': logo,
                'thegana': thegana,
                'samparka': samparka,
                'jilla': jilla,
                'j_miti': j_miti,
                'n_miti': n_miti,
                'karyalaya': karyalaya,
                'kaifiyat': kaifiyat,
            }
            form = DetailHotelForm(form_data)
            if form.is_valid():
                hotel_object = form.save(commit=False)
                hotel_object.save()
        return HttpResponse("data saved")
    else:
        form = DetailHotelForm()
    context = {'form': form, 'data': data}

    return render(request, 'forms/details/hotel.html', context)


def detail_registration(request):
    """views for detail अनुज्ञापत्र जारी"""
    
    data = {
        'samuha': commons.DETAIL_SAMUHA_CHOICES,
    }
    if request.method == 'POST':
        d_samuha = request.POST.getlist('samuha[]')
        d_naam = request.POST.getlist('naam[]')
        d_thegana = request.POST.getlist('thegana[]')
        d_byakti = request.POST.getlist('byakti[]')
        d_samparka = request.POST.getlist('samparka[]')
        d_jilla = request.POST.getlist('jilla[]')
        d_mukhya = request.POST.getlist('mukhya[]')
        d_brand = request.POST.getlist('brand[]')
        d_karyalaya = request.POST.getlist('karyalaya[]')
        d_j_miti = request.POST.getlist('j_miti[]')
        d_n_miti = request.POST.getlist('n_miti[]')
        d_kaifiyat = request.POST.getlist('kaifiyat[]')
        
        for samuha, naam, thegana, byakti, samparka, jilla, mukhya, brand, karyalaya, j_miti, n_miti, kaifiyat in zip(
            d_samuha, d_naam, d_thegana, d_byakti, d_samparka, d_jilla, d_mukhya, d_brand, d_karyalaya, d_j_miti, d_n_miti, d_kaifiyat 
        ):
            form_data = {
                'samuha': samuha,
                'naam': naam,
                'thegana': thegana,
                'byakti': byakti,
                'samparka': samparka,
                'jilla': jilla,
                'mukhya': mukhya,
                'brand': brand,
                'karyalaya': karyalaya,
                'j_miti': j_miti,
                'n_miti': n_miti,
                'kaifiyat': kaifiyat,
            }
            form = DetailRegistrationForm(form_data)
            if form.is_valid():
                reg_object = form.save(commit=False)
                reg_object.save()
        return HttpResponse("data saved")
    else:
        form = DetailRegistrationForm()
    context = {'form': form, 'data': data}
    return render(request, 'forms/details/registration.html', context)


def detail_renew(request):
    """views for detail अनुज्ञापत्र नवकिरण"""
    
    data = {
        'samuha': commons.DETAIL_SAMUHA_CHOICES,
    }
    if request.method == 'POST':
        d_samuha = request.POST.getlist('samuha[]')
        d_naam = request.POST.getlist('naam[]')
        d_thegana = request.POST.getlist('thegana[]')
        d_byakti = request.POST.getlist('byakti[]')
        d_samparka = request.POST.getlist('samparka[]')
        d_jilla = request.POST.getlist('jilla[]')
        d_mukhya = request.POST.getlist('mukhya[]')
        d_brand = request.POST.getlist('brand[]')
        d_karyalaya = request.POST.getlist('karyalaya[]')
        d_j_miti = request.POST.getlist('j_miti[]')
        d_n_miti = request.POST.getlist('n_miti[]')
        d_kaifiyat = request.POST.getlist('kaifiyat[]')
        
        for samuha, naam, thegana, byakti, samparka, jilla, mukhya, brand, karyalaya, j_miti, n_miti, kaifiyat in zip(
            d_samuha, d_naam, d_thegana, d_byakti, d_samparka, d_jilla, d_mukhya, d_brand, d_karyalaya, d_j_miti, d_n_miti, d_kaifiyat 
        ):
            form_data = {
                'samuha': samuha,
                'naam': naam,
                'thegana': thegana,
                'byakti': byakti,
                'samparka': samparka,
                'jilla': jilla,
                'mukhya': mukhya,
                'brand': brand,
                'karyalaya': karyalaya,
                'j_miti': j_miti,
                'n_miti': n_miti,
                'kaifiyat': kaifiyat,
            }
            form = DetailRenewForm(form_data)
            if form.is_valid():
                reg_object = form.save(commit=False)
                reg_object.save()
        return HttpResponse("data saved")
    else:
        form = DetailRenewForm()
    context = {'form': form, 'data': data}
    return render(request, 'forms/details/renew.html', context)


def detail_udyog(request):
    """views for detail उद्योग सिफारिस"""
    
    data = {
        'samuha': commons.DETAIL_SAMUHA_CHOICES,
    }
    if request.method == 'POST':
        d_samuha = request.POST.getlist('samuha[]')
        d_naam = request.POST.getlist('naam[]')
        d_thegana = request.POST.getlist('thegana[]')
        d_byakti = request.POST.getlist('byakti[]')
        d_samparka = request.POST.getlist('samparka[]')
        d_jilla = request.POST.getlist('jilla[]')
        d_mukhya = request.POST.getlist('mukhya[]')
        d_brand = request.POST.getlist('brand[]')
        d_karyalaya = request.POST.getlist('karyalaya[]')
        d_j_miti = request.POST.getlist('j_miti[]')
        d_n_miti = request.POST.getlist('n_miti[]')
        d_kaifiyat = request.POST.getlist('kaifiyat[]')
        
        for samuha, naam, thegana, byakti, samparka, jilla, mukhya, brand, karyalaya, j_miti, n_miti, kaifiyat in zip(
            d_samuha, d_naam, d_thegana, d_byakti, d_samparka, d_jilla, d_mukhya, d_brand, d_karyalaya, d_j_miti, d_n_miti, d_kaifiyat 
        ):
            form_data = {
                'samuha': samuha,
                'naam': naam,
                'thegana': thegana,
                'byakti': byakti,
                'samparka': samparka,
                'jilla': jilla,
                'mukhya': mukhya,
                'brand': brand,
                'karyalaya': karyalaya,
                'j_miti': j_miti,
                'n_miti': n_miti,
                'kaifiyat': kaifiyat,
            }
            form = DetailUdyogForm(form_data)
            if form.is_valid():
                reg_object = form.save(commit=False)
                reg_object.save()
        return HttpResponse("data saved")
    else:
        form = DetailUdyogForm()
    context = {'form': form, 'data': data}
    return render(request, 'forms/details/udyog.html', context)


def detail_anugaman(request):
    """views for detail अनुगमन निरीक्षण"""
    
    data = {
        'anugaman': commons.DETAIL_ANUGAMAN_CHOICES,
    }
    if request.method == 'POST':
        
        a_nirichad = request.POST.getlist('nirichad[]')
        a_miti = request.POST.getlist('miti[]')
        a_naam = request.POST.getlist('naam[]')
        a_thegana = request.POST.getlist('thegana[]')
        a_nikaya = request.POST.getlist('nikaya[]')
        a_a_bibaran = request.POST.getlist('a_bibaran[]')
        a_silbandi = request.POST.getlist('silbandi[]')
        a_parinam = request.POST.getlist('parinam[]')
        a_mulya = request.POST.getlist('mulya[]')
        a_nirdesan = request.POST.getlist('nirdesan[]')
        a_d_bibaran = request.POST.getlist('d_bibaran[]')
        a_kaifiyat = request.POST.getlist('kaifiyat[]')
        
        for nirichad, miti, naam, thegana, nikaya, a_bibaran, silbandi, parinam, mulya, nirdesan, d_bibaran, kaifiyat in zip (
            a_nirichad, a_miti, a_naam, a_thegana, a_nikaya, a_a_bibaran, a_silbandi, a_parinam, a_mulya, a_nirdesan, a_d_bibaran, a_kaifiyat
        ):
            form_data = {
                'nirichad': nirichad,
                'miti': miti,
                'naam': naam,
                'thegana': thegana,
                'nikaya': nikaya,
                'a_bibaran': a_bibaran,
                'silbandi': silbandi,
                'parinam': parinam,
                'mulya': mulya,
                'nirdesan': nirdesan,
                'd_bibaran': d_bibaran,
                'kaifiyat': kaifiyat,
            }
    
            form = DetailAnugamanForm(form_data)
            if form.is_valid():
                anugaman_object = form.save(commit=False)
                anugaman_object.save()
        return HttpResponse("data saved")
    else:
        form = DetailAnugamanForm()
    context = {'form': form, 'data': data}
    return render(request, 'forms/details/anugaman.html', context)


def detail_mudha(request):
    """views for detail मुद्धा दायरी"""
    
    if request.method == 'POST':
        d_naam = request.POST.getlist('naam[]')
        d_b_naam = request.POST.getlist('b_naam[]')
        d_n_miti = request.POST.getlist('n_miti[]')
        d_n_sthan = request.POST.getlist('n_sthan[]')
        d_n_khani = request.POST.getlist('n_khani[]')
        d_p_miti = request.POST.getlist('p_miti[]')
        d_b_miti = request.POST.getlist('b_miti[]')
        d_prakar = request.POST.getlist('prakar[]')
        d_parameter = request.POST.getlist('parameter[]')
        d_m_sthan = request.POST.getlist('m_sthan[]')
        d_m_miti = request.POST.getlist('m_miti[]')
        d_m_khani = request.POST.getlist('m_khani[]')
        d_karyalaya = request.POST.getlist('karyalaya[]')
        d_kaifiyat = request.POST.getlist('kaifiyat[]')
        
        for naam, b_naam, n_miti, n_sthan, n_khani, p_miti, b_miti, prakar, parameter, m_sthan, m_miti, m_khani, karyalaya, kaifiyat in zip(
            d_naam, d_b_naam, d_n_miti, d_n_sthan, d_n_khani, d_p_miti, d_b_miti, d_prakar, d_parameter, d_m_sthan, d_m_miti, d_m_khani, 
            d_karyalaya, d_kaifiyat):
            form_data = {
                'naam': naam,
                'b_naam': b_naam,
                'n_miti': n_miti,
                'n_sthan': n_sthan,
                'n_khani': n_khani,
                'p_miti': p_miti,
                'b_miti': b_miti,
                'prakar': prakar,
                'parameter': parameter,
                'm_sthan': m_sthan,
                'm_miti': m_miti,
                'm_khani': m_khani,
                'karyalaya': karyalaya,
                'kaifiyat': kaifiyat,
            }
            form = DetailMudhaForm(form_data)
            if form.is_valid():
                mudha_object = form.save(commit=False)
                mudha_object.save()
        return HttpResponse("data saved")
    else:
        form = DetailMudhaForm()
    context = {'form': form}
    return render(request, 'forms/details/mudha.html', context)


def detail_rbpa(request):
    """views for detail RBPA Analysis"""
    
    if request.method == 'POST':
        d_date = request.POST.getlist('date[]')
        d_commodity1 = request.POST.getlist('commodity1[]')
        d_sample1 = request.POST.getlist('sample1[]')
        d_quantity1 = request.POST.getlist('quantity1[]')
        d_sample2 = request.POST.getlist('sample2[]')
        d_quantity2 = request.POST.getlist('quantity2[]')
        d_commodity2 = request.POST.getlist('commodity2[]')
        d_sample3 = request.POST.getlist('sample3[]')
        d_quantity3 = request.POST.getlist('quantity3[]')
        d_commodity3 = request.POST.getlist('commodity3[]')
        
        for date, commodity1, sample1, quantity1, sample2, quantity2, commodity2, sample3, quantity3, commodity3 in zip(d_date, d_commodity1,
            d_sample1, d_quantity1, d_sample2, d_quantity2, d_commodity2, d_sample3, d_quantity3, d_commodity3):
            form_data = {
                'date': date,
                'commodity1': commodity1,
                'sample1': sample1,
                'quantity1': quantity1,
                'sample2': sample2,
                'quantity2': quantity2,
                'commodity2': commodity2,
                'sample3': sample3,
                'quantity3': quantity3,
                'commodity3': commodity3,
            }
            form = DetailRbpaForm(form_data)
            if form.is_valid():
                rbpa_object = form.save(commit=False)
                rbpa_object.save()
        return HttpResponse("data saved")
    else:
        form = DetailRbpaForm()
    context = {'form': form}
    return render(request, 'forms/details/rbpa.html', context)


def detail_gunasho(request):
    """views for detail उजुरी गुनासो"""
    
    data = {
        'srot': commons.DETAIL_SROT_CHOICES,
        'current_nepali_date': nepali_datetime.date.today().strftime("%Y/%m/%d"),
        'current_nepali_year': nepali_datetime.date.today().strftime("%Y"),
    }
    if request.method == 'POST':
        d_p_miti = request.POST.getlist('p_miti[]')
        d_srot = request.POST.getlist('srot[]')
        d_s_miti = request.POST.getlist('s_miti[]')
        d_bibaran = request.POST.getlist('bibaran[]')
        
        for p_miti, srot, s_miti, bibaran in zip (d_p_miti, d_srot, d_s_miti, d_bibaran):
            form_data = {
                'p_miti': p_miti,
                'srot': srot,
                's_miti': s_miti,
                'bibaran': bibaran,
            }
            form = DetailGunasoForm(form_data)
            if form.is_valid():
                gunaso_object = form.save(commit=False)
                gunaso_object.save()
        return HttpResponse("saved")
    else:
        form = DetailGunasoForm()
    context = {'form': form, 'data': data}
    return render(request, 'forms/details/gunasho.html', context)


#--------------------- REPORT PART BELOW --------------------------

#working
def khadyaact_report(request):
    """table list for खाद्य ऐन/नियम बमोजिम संकलित नमुना विवरण"""
    
    data = NamunaBibaran.objects.all()
    context = {'data': data}
    return render(request, 'report/khadyaact.html', context)

#working
def anugaman_report(request):
    """table list for निरीक्षण अनुगमन विवरण"""
    
    data = AnugamanBibaran.objects.all()
    context = {'data': data}
    return render(request, 'report/anugaman.html', context)

#working
def hotel_report(request):
    """table list for होटल स्तरीकरण लोगो वितरण सम्बन्धि विवरण"""
    
    data = Logobitaran.objects.all()
    context = {'data': data}
    return render(request, 'report/hotel.html', context)

#working
def khadya_report(request):
    """table list for खाद्य तथा दाना नमुना विश्लेषण विवरण"""
    
    data = NamunaBisleysan.objects.all()
    context = {'data': data}
    return render(request, 'report/khadyanamuna.html', context)

#working
def prayogsala_report(request):
    """table list for प्रयोगशाला विश्लेषण प्रतिवेदन सारांश"""
    
    data = PrayogsalaBisleysan.objects.all()
    context = {'data': data}
    return render(request, 'report/prayogsala.html', context)

#working
def rbpa_report(request):
    """table list for RBPA Analysis Report"""
    
    data = DetailRbpa.objects.all()
    context = {'data': data}
    return render(request, 'report/rbpa.html', context)

#working
def importexport_report(request):
    """table list for आयात निर्यात गुण प्रमाणिकरण"""
    
    data = AayatNiryat.objects.all()
    context = {'data': data}
    return render(request, 'report/importexport.html', context)

#working
def gunasho_report(request):
    """table list for उजुरी/गुनासो ब्येवस्थापन"""
    
    data = UjuriGunaso.objects.all()
    context = {'data': data}
    return render(request, 'report/gunasho.html', context)

#working
def patrakar_report(request):
    """table list for खाद्य प्रसोधन, खाद्य पोषण, उद्योग, होटेल, पत्रकार, कार्यशाला आदि"""
    
    data = KhadyaPrasodhan.objects.all()
    context = {'data': data}
    return render(request, 'report/patrakar.html', context)

#working
def patrajari_report(request):
    """table list for खाद्य तथा दाना अनुज्ञा पत्र जारी"""
    
    data = PatraJari.objects.all()
    context = {'data': data}
    return render(request, 'report/patrajari.html', context)

#working
def renew_report(request):
    """table list for खाद्य तथा दाना अनुज्ञा पत्र नविकरण"""
    
    data = PatraNabikaran.objects.all()
    context = {'data': data}
    return render(request, 'report/renew.html', context)

#not working
def udyog_report(request):
    """table list for उद्योग सिफारिस"""
    
    data = UdyogSifaris.objects.all()
    context = {'data': data}
    return render(request, 'report/udyog.html', context)

#working
def finance_report(request):
    """table list for मासिक वित्तिय विवरण"""
    
    data = BittiyaBibaran.objects.all()
    context = {'data': data}
    return render(request, 'report/finance.html', context)

#working
def monthly_report(request):
    """table list for मासिक प्रगति विवरण"""
    
    data = PragatiBibaran.objects.all()
    context = {'data': data}
    return render(request, 'report/monthly.html', context)



















