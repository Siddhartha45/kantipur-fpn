from django.shortcuts import render, HttpResponse, redirect
from .forms import (UjuriGunasoForm, BittiyaBibaranForm, NamunaBibaranForm, PatraJariForm, PatraNabikaranForm,
                    UdyogSifarisForm, AnugamanBibaranForm, NamunaBisleysanForm)
from .models import AnugamanBibaran, NamunaBisleysan
from fpn import commons


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
    return render(request, 'forms/logobitaran_bibaran/newentry.html')


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
    return render(request, 'forms/pratibedan_bibaran/newentry.html')


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
    return render(request, 'forms/import-export/index.html')


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
    return render(request, 'forms/hotel-patrakar/index.html')


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
    return render(request, 'forms/report/summary.html')