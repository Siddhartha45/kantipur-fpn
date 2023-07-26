from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .forms import (BarsikLakshyaForm, UjuriGunasoForm, BittiyaBibaranForm, NamunaBibaranForm, PatraJariForm, PatraNabikaranForm,
                    UdyogSifarisForm, AnugamanBibaranForm, NamunaBisleysanForm, AayatNiryatForm, PrayogsalaBisleysanForm,
                    LogobitaranForm, KhadyaPrasodhanForm,UdyogSifarisEditForm, DetailAnugamanForm, DetailHotelForm, DetailRegistrationForm, DetailRenewForm,
                    DetailUdyogForm,PatraNabikaranEditForm,PatraJariEditForm, DetailGunasoForm,KhadyaPrasodhanEditForm, DetailMudhaForm, DetailRbpaForm, MasikPragatiForm,
                    AnugamanEditForm,BittiyaBibaranEditForm,PragatiBibaranEditForm, KhadyaactEditForm,UjuriGunasoEditForm, HotelEditForm, KhadyaEditForm, PrayogsalaEditForm,RbpaEditForm,AayatNiryatEditForm)
from .models import (BarsikLakshya, AnugamanBibaran, NamunaBisleysan, AayatNiryat, PrayogsalaBisleysan, Logobitaran, BittiyaBibaran, UjuriGunaso,
                    NamunaBibaran, PragatiBibaran, DetailRbpa, UdyogSifaris, PatraNabikaran, PatraJari, KhadyaPrasodhan,
                    DetailAnugaman, DetailGunaso, DetailHotel, DetailMudha, DetailRegistration, DetailRenew, DetailUdyog)
from fpn import commons
from django.contrib.auth.decorators import login_required
import nepali_datetime
from django.contrib import messages
from fpn.decorators import (fo_and_do_and_ffsqrd_required, fo_and_ffsqrd_required, fo_required, fo_and_nffrl_required, ie_required, ie_and_fo_required)
from account.models import CustomUser, Office
from django.db.models import Sum

from .report_sum import (ayatniryat_sum, namunabibaran_sum, anugamanbibaran_sum, logobitaran_sum, namunabisleysan_sum, prayogsala_sum, 
                        patrajari_sum, patranabikaran_sum,udyogsifaris_sum, ujurigunaso_sum, rbpa_sum, khadyaprasodhan_sum, bittiyabibaran_sum,
                        
                        namunabibaran_monthly_sum, anugamanbibaran_monthly_sum, logobitaran_monthly_sum, namunabisleysan_monthly_sum,
                        prayogsala_monthly_sum, patrajari_monthly_sum, patranabikaran_monthly_sum, udyogsifaris_monthly_sum, ayatniryat_monthly_sum,
                        ujurigunaso_monthly_sum, rbpa_monthly_sum, 
                        
                        office_namunabibaran_monthly_sum, office_anugamanbibaran_monthly_sum, office_logobitaran_monthly_sum, office_namunabisleysan_monthly_sum,
                        office_patrajari_monthly_sum, office_patranabikaran_monthly_sum, office_prayogsala_monthly_sum, office_rbpa_monthly_sum,
                        office_udyogsifaris_monthly_sum, office_ujurigunaso_monthly_sum, office_ayatniryat_monthly_sum)
from fpn.exceptions import RecordAlreadyExists
#----------------------------------------------------------------------------------------------------------------------------------


@login_required
def home(request):
    """view for dashboard"""
    return render(request, 'index.html')


def report(request):
    offices = Office.objects.all()
    selected_month = request.GET.get('month')
    
    for office in offices:
        office_namunabibaran_monthly = office_namunabibaran_monthly_sum(request, office.id, selected_month)
        office.office_namunabibaran_monthly = office_namunabibaran_monthly
        
        office_anugamanbibaran_monthly = office_anugamanbibaran_monthly_sum(request, office.id, selected_month)
        office.office_anugamanbibaran_monthly = office_anugamanbibaran_monthly
        
        office_logobitaran_monthly = office_logobitaran_monthly_sum(request, office.id, selected_month)
        office.office_logobitaran_monthly = office_logobitaran_monthly
        
        office_namunabisleysan_monthly = office_namunabisleysan_monthly_sum(request, office.id, selected_month)
        office.office_namunabisleysan_monthly = office_namunabisleysan_monthly
        
        office_prayogsala_monthly = office_prayogsala_monthly_sum(request, office.id, selected_month)
        office.office_prayogsala_monthly = office_prayogsala_monthly
        
        office_patrajari_monthly = office_patrajari_monthly_sum(request, office.id, selected_month)
        office.office_patrajari_monthly = office_patrajari_monthly
        
        office_patranabikaran_monthly = office_patranabikaran_monthly_sum(request, office.id, selected_month)
        office.office_patranabikaran_monthly = office_patranabikaran_monthly
        
        office_udyogsifaris_monthly = office_udyogsifaris_monthly_sum(request, office.id, selected_month)
        office.office_udyogsifaris_monthly = office_udyogsifaris_monthly
        
        office_ayatniryat_monthly = office_ayatniryat_monthly_sum(request, office.id, selected_month)
        office.office_ayatniryat_monthly = office_ayatniryat_monthly
        
        office_ujurigunaso_monthly = office_ujurigunaso_monthly_sum(request, office.id, selected_month)
        office.office_ujurigunaso_monthly = office_ujurigunaso_monthly
        
        office_rbpa_monthly = office_rbpa_monthly_sum(request, office.id, selected_month)
        office.office_rbpa_monthly = office_rbpa_monthly
        
    context = {
        'offices': offices,
        'selected_month': selected_month,
    }
    
    return render(request, 'report.html', context)


def progress_count(request):
    
    #variables for storing sum of models
    aayat_niryat_sum = ayatniryat_sum(request)
    namuna_bibaran_sum = namunabibaran_sum(request)
    anugaman_bibaran_sum = anugamanbibaran_sum(request)
    logo_bitaran_sum = logobitaran_sum(request)
    namuna_bisleysan_sum = namunabisleysan_sum(request)
    prayog_sala_sum = prayogsala_sum(request)
    patra_jari_sum = patrajari_sum(request)
    patra_nabikaran_sum = patranabikaran_sum(request)
    udyog_sifaris_sum = udyogsifaris_sum(request)
    ujuri_gunaso_sum = ujurigunaso_sum(request)
    rbpa_analysis_sum = rbpa_sum(request)
    
    month = request.GET.get('month')    #gets the value of months from frontend
    
    #vvariables for storing sum of models for specific month
    namuna_bibaran_monthly_sum = namunabibaran_monthly_sum(request, month)
    anugaman_bibaran_monthly_sum = anugamanbibaran_monthly_sum(request, month)
    logo_bitaran_monthly_sum = logobitaran_monthly_sum(request, month)
    namuna_bisleysan_monthly_sum = namunabisleysan_monthly_sum(request, month)
    prayog_sala_monthly_sum = prayogsala_monthly_sum(request, month)
    patra_jari_monthly_sum = patrajari_monthly_sum(request, month)
    patra_nabikaran_monthly_sum = patranabikaran_monthly_sum(request, month)
    udyog_sifaris_monthly_sum = udyogsifaris_monthly_sum(request, month)
    ayat_niryat_monthly_sum = ayatniryat_monthly_sum(request, month)
    ujuri_gunaso_monthly_sum = ujurigunaso_monthly_sum(request, month)
    rbpa_analysis_monthly_sum = rbpa_monthly_sum(request, month)
    
    # sum_values = NamunaBibaran.objects.filter(
    #     is_verified = True, created_on_np_date__startswith=f'2080-{month}'
    # ).aggregate(
    #     total = Sum('milk') + Sum('oil') + Sum('fruits') + Sum('spice') + 
    #             Sum('tea') + Sum('salt') + Sum('khadanna') + Sum('water') + 
    #             Sum('sweets') + Sum('confectionery') + Sum('meat') + Sum('grain') +
    #             Sum('others')
    # )
    
    if request.user.role == 'A':
        try:
            obj = BarsikLakshya.objects.filter(created_by__role='A').latest('created_on')
        except:
            obj = None
    elif request.user.role == 'DE':
        try:
            obj = BarsikLakshya.objects.filter(created_by__office=request.user.office).latest('created_on')
        except:
            obj = None
    else:
        obj = None
        
    context = {
        'obj': obj,
        'aayat_niryat_sum': aayat_niryat_sum,
        'namuna_bibaran_sum': namuna_bibaran_sum,
        'anugaman_bibaran_sum': anugaman_bibaran_sum,
        'logo_bitaran_sum': logo_bitaran_sum,
        'namuna_bisleysan_sum': namuna_bisleysan_sum,
        'prayog_sala_sum': prayog_sala_sum,
        'patra_jari_sum': patra_jari_sum,
        'patra_nabikaran_sum': patra_nabikaran_sum,
        'udyog_sifaris_sum': udyog_sifaris_sum,
        'ujuri_gunaso_sum': ujuri_gunaso_sum,
        'rbpa_analysis_sum': rbpa_analysis_sum,
        
        'namuna_bibaran_monthly_sum': namuna_bibaran_monthly_sum,
        'anugaman_bibaran_monthly_sum': anugaman_bibaran_monthly_sum,
        'logo_bitaran_monthly_sum': logo_bitaran_monthly_sum,
        'namuna_bisleysan_monthly_sum': namuna_bisleysan_monthly_sum,
        'prayog_sala_monthly_sum': prayog_sala_monthly_sum,
        'patra_jari_monthly_sum': patra_jari_monthly_sum,
        'patra_nabikaran_monthly_sum': patra_nabikaran_monthly_sum,
        'udyog_sifaris_monthly_sum': udyog_sifaris_monthly_sum,
        'ayat_niryat_monthly_sum': ayat_niryat_monthly_sum,
        'ujuri_gunaso_monthly_sum': ujuri_gunaso_monthly_sum,
        'rbpa_analysis_monthly_sum': rbpa_analysis_monthly_sum,
    }
    return render(request, 'count.html', context)


def progress_amount(request):
    return render(request, 'amount.html')


def barsik_lakshya(request):
    """for adding barsik lakshya to meet to check progress(used in मासिक प्रगति विवरण)"""
    if request.method == 'POST':
        form = BarsikLakshyaForm(request.POST)
        if form.is_valid():
            BarsikLakshya.objects.create(created_by=request.user, **form.cleaned_data)
            messages.success(request, "Barsik Lakshya Added")
            return redirect('barsik-lakshya')
        else:
            messages.error(request, "Barsik Lakshya was not added. Please fill the form again")
    else:
        form = BarsikLakshyaForm()
    context = {'form': form}
    return render(request, 'forms/barsik_lakshya/barsik_lakshya.html', context)


#------------------------------------------------------------FORMS PART BELOW -----------------------------------------------------------


@fo_and_do_and_ffsqrd_required
def namuna_bibaran(request):
    """views for खाद्य ऐन/नियम बमोजिम संकलित नमुना विवरण"""
    
    if request.method == 'POST':
        form = NamunaBibaranForm(request.POST)
        if form.is_valid():
            try:
                NamunaBibaran.objects.create(created_by=request.user, **form.cleaned_data)
                messages.success(request, "Form submitted successfully")
                return redirect('khadya-act-report')
            except RecordAlreadyExists as e:
                messages.error(request, e.message)
                return redirect('namuna')
        else:
            messages.error(request, "Please fill the form with correct data")
    else:
        form = NamunaBibaranForm()
    context = {'form': form}
    return render(request, 'forms/namuna_bibaran/newentry.html', context)


@fo_and_do_and_ffsqrd_required
def anugaman(request):
    """views for निरीक्षण अनुगमन विवरण"""
    if request.method == 'POST':
        form = AnugamanBibaranForm(request.POST)
        if form.is_valid():
            types = {
                'udyog': ['u_patak', 'u_sankhya', 'u_pragati', 'u_kaifiyat'],
                'pasal': ['p_patak', 'p_sankhya', 'p_pragati', 'p_kaifiyat'],
                'supermarket': ['s_patak', 's_sankhya', 's_pragati', 's_kaifiyat'],
                'godam': ['g_patak', 'g_sankhya', 'g_pragati', 'g_kaifiyat'],
                'hotel': ['h_patak', 'h_sankhya', 'h_pragati', 'h_kaifiyat'],
                'dana': ['d_patak', 'd_sankhya', 'd_pragati', 'd_kaifiyat'],
                'anya': ['a_patak', 'a_sankhya', 'a_pragati', 'a_kaifiyat'],
            }

            objects_to_create = []  # Creating an empty list to store different data

            for type_key, form_fields in types.items():
                data = {
                    'type': type_key,
                }
                for field in form_fields:
                    data[field.split("_")[-1]] = form.cleaned_data.get(field)
                objects_to_create.append(AnugamanBibaran(created_by=request.user, **data))

            try:
                AnugamanBibaran.objects.bulk_create(objects_to_create)
                messages.success(request, "Form submitted successfully")
                return redirect('anugaman-report')
            except RecordAlreadyExists as e:
                messages.error(request, e.message)
                return redirect('anugaman')
        else:
            messages.error(request, "Please fill the form with correct data")
    else:
        form = AnugamanBibaranForm()
    context = {'form': form}
    return render(request, 'forms/anugaman_bibaran/newentry.html', context)


@fo_and_ffsqrd_required
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
            objects_to_create.append(Logobitaran(created_by=request.user, **g_data))
            #Logobitaran.objects.create(created_by=request.user, **g_data)
            
            y1_data = {
                'type': 'yellow1',
                'c_pragati': form.cleaned_data.get('y1_c_pragati'),
                'h_pragati1': form.cleaned_data.get('y1_h_pragati1'),
                'h_pragati2': form.cleaned_data.get('y1_h_pragati2'),
                'kaifiyat': form.cleaned_data.get('y1_kaifiyat'),
            }
            objects_to_create.append(Logobitaran(created_by=request.user, **y1_data))
            #Logobitaran.objects.create(created_by=request.user, **y1_data)
            
            y2_data = {
                'type': 'yellow2',
                'c_pragati': form.cleaned_data.get('y2_c_pragati'),
                'h_pragati1': form.cleaned_data.get('y2_h_pragati1'),
                'h_pragati2': form.cleaned_data.get('y2_h_pragati2'),
                'kaifiyat': form.cleaned_data.get('y2_kaifiyat'),
            }
            objects_to_create.append(Logobitaran(created_by=request.user, **y2_data))
            #Logobitaran.objects.create(created_by=request.user, **y2_data)
            
            r_data = {
                'type': 'red',
                'c_pragati': form.cleaned_data.get('r_c_pragati'),
                'h_pragati1': form.cleaned_data.get('r_h_pragati1'),
                'h_pragati2': form.cleaned_data.get('r_h_pragati2'),
                'kaifiyat': form.cleaned_data.get('r_kaifiyat'),
            }
            objects_to_create.append(Logobitaran(created_by=request.user, **r_data))
            #Logobitaran.objects.create(created_by=request.user, **r_data)
            try:
                Logobitaran.objects.bulk_create(objects_to_create)
                messages.success(request, "Form submitted successfully")
                return redirect('hotel-report')
            except RecordAlreadyExists as e:
                messages.error(request, e.message)
                return redirect('logobitaran')
        else:
            messages.error(request, "Please fill the form with correct data")
    else:
        form = LogobitaranForm()
    context = {'form': form}
    return render(request, 'forms/logobitaran_bibaran/newentry.html', context)


@fo_and_nffrl_required
def namuna_bisleysan(request):
    """views for खाद्य तथा दाना नमुना विश्लेषण विवरण"""
    
    data = {
        'ekai': commons.EKAI_CHOICES,
    }
    
    if request.method == 'POST':
        form = NamunaBisleysanForm(request.POST)
        if form.is_valid():
            types = {
                'milk': ['m_ekai', 'm_lakshya', 'm_pragati1', 'm_mahina_pragati', 'm_sankhya', 'm_parameter', 'm_pragati2', 'm_pratisat', 'm_kaifiyat'],
                'oil': ['o_ekai', 'o_lakshya', 'o_pragati1', 'o_mahina_pragati', 'o_sankhya', 'o_parameter', 'o_pragati2', 'o_pratisat', 'o_kaifiyat'],
                'fruits': ['f_ekai', 'f_lakshya', 'f_pragati1', 'f_mahina_pragati', 'f_sankhya', 'f_parameter', 'f_pragati2', 'f_pratisat', 'f_kaifiyat'],
                'spice': ['s_ekai', 's_lakshya', 's_pragati1', 's_mahina_pragati', 's_sankhya', 's_parameter', 's_pragati2', 's_pratisat', 's_kaifiyat'],
                'tea': ['t_ekai', 't_lakshya', 't_pragati1', 't_mahina_pragati', 't_sankhya', 't_parameter', 't_pragati2', 't_pratisat', 't_kaifiyat'],
                'salt': ['sa_ekai', 'sa_lakshya', 'sa_pragati1', 'sa_mahina_pragati', 'sa_sankhya', 'sa_parameter', 'sa_pragati2', 'sa_pratisat', 'sa_kaifiyat'],
                'khadanna': ['k_ekai', 'k_lakshya', 'k_pragati1', 'k_mahina_pragati', 'k_sankhya', 'k_parameter', 'k_pragati2', 'k_pratisat', 'k_kaifiyat'],
                'water': ['w_ekai', 'w_lakshya', 'w_pragati1', 'w_mahina_pragati', 'w_sankhya', 'w_parameter', 'w_pragati2', 'w_pratisat', 'w_kaifiyat'],
                'sweets': ['sw_ekai', 'sw_lakshya', 'sw_pragati1', 'sw_mahina_pragati', 'sw_sankhya', 'sw_parameter', 'sw_pragati2', 'sw_pratisat', 'sw_kaifiyat'],
                'confectionery': ['c_ekai', 'c_lakshya', 'c_pragati1', 'c_mahina_pragati', 'c_sankhya', 'c_parameter', 'c_pragati2', 'c_pratisat', 'c_kaifiyat'],
                'meat': ['me_ekai', 'me_lakshya', 'me_pragati1', 'me_mahina_pragati', 'me_sankhya', 'me_parameter', 'me_pragati2', 'me_pratisat', 'me_kaifiyat'],
                'others': ['ot_ekai', 'ot_lakshya', 'ot_pragati1', 'ot_mahina_pragati', 'ot_sankhya', 'ot_parameter', 'ot_pragati2', 'ot_pratisat', 'ot_kaifiyat'],
                'grain': ['g_ekai', 'g_lakshya', 'g_pragati1', 'g_mahina_pragati', 'g_sankhya', 'g_parameter', 'g_pragati2', 'g_pratisat', 'g_kaifiyat'],
            }
            
            objects_to_create = []
            
            for type_key, form_fields in types.items():
                data = {
                    'type': type_key,
                }
                for field in form_fields:
                    if field.endswith('_mahina_pragati'):
                        data['mahina_pragati'] = form.cleaned_data.get(field)
                    else:
                        data[field.split("_")[-1]] = form.cleaned_data.get(field)
                objects_to_create.append(NamunaBisleysan(created_by=request.user, **data))

            try:
                NamunaBisleysan.objects.bulk_create(objects_to_create)
                messages.success(request, "Form submitted successfully")
                return redirect('khadya-report')
            except RecordAlreadyExists as e:
                messages.error(request, e.message)
                return redirect('namuna-bisleysan')
        else:
            messages.error(request, "Please fill the form with correct data")
    else:
        form = NamunaBisleysanForm()
    context = {'form': form, 'data': data}
    return render(request, 'forms/bisleysan_bibaran/newentry.html', context)


@fo_and_nffrl_required
def prayogsala_bisleysan(request):
    """for data entry of प्रयोगशाला विश्लेषण प्रतिवेदन सारांश"""
    
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
            objects_to_create.append(PrayogsalaBisleysan(created_by=request.user, **m_data))
            
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
            objects_to_create.append(PrayogsalaBisleysan(created_by=request.user, **o_data))
            
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
            objects_to_create.append(PrayogsalaBisleysan(created_by=request.user, **f_data))
            
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
            objects_to_create.append(PrayogsalaBisleysan(created_by=request.user, **s_data))
            
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
            objects_to_create.append(PrayogsalaBisleysan(created_by=request.user, **t_data))
            
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
            objects_to_create.append(PrayogsalaBisleysan(created_by=request.user, **sa_data))
            
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
            objects_to_create.append(PrayogsalaBisleysan(created_by=request.user, **k_data))
            
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
            objects_to_create.append(PrayogsalaBisleysan(created_by=request.user, **w_data))
            
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
            objects_to_create.append(PrayogsalaBisleysan(created_by=request.user, **sw_data))
            
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
            objects_to_create.append(PrayogsalaBisleysan(created_by=request.user, **c_data))
            
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
            objects_to_create.append(PrayogsalaBisleysan(created_by=request.user, **me_data))
            
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
            objects_to_create.append(PrayogsalaBisleysan(created_by=request.user, **g_data))
            
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
            objects_to_create.append(PrayogsalaBisleysan(created_by=request.user, **ot_data))
            
            try:
                PrayogsalaBisleysan.objects.bulk_create(objects_to_create)
                messages.success(request, "Form submitted successfully")
                return redirect('prayogsala-report')
            except RecordAlreadyExists as e:
                messages.error(request, e.message)
                return redirect('prayogsala-bisleysan')
        else:
            messages.error(request, "Please fill the form with correct data")
    else:
        form = PrayogsalaBisleysanForm()
    context = {'form': form}
    return render(request, 'forms/pratibedan_bibaran/newentry.html', context)


@fo_and_ffsqrd_required
def khadya1(request):
    """views for खाद्य तथा दाना अनुज्ञा पत्र जारी"""
    
    if request.method == 'POST':
        form = PatraJariForm(request.POST)
        if form.is_valid():
            try:
                PatraJari.objects.create(created_by=request.user, **form.cleaned_data)
                messages.success(request, "Form submitted successfully")
                return redirect('patrajari-report')
            except RecordAlreadyExists as e:
                messages.error(request, e.message)
                return redirect('khadya1')
        else:
            messages.error(request, "Please fill the form with correct data")
    else:
        form = PatraJariForm()
    context = {'form': form}
    return render(request, 'forms/registration/new.html', context)


@fo_and_ffsqrd_required
def khadya2(request):
    """views for खाद्य तथा दाना अनुज्ञा पत्र नविकरण"""
    
    if request.method == 'POST':
        form = PatraNabikaranForm(request.POST)
        if form.is_valid():
            try:
                PatraNabikaran.objects.create(created_by=request.user, **form.cleaned_data)
                messages.success(request, "Form submitted successfully")
                return redirect('renew-report')
            except RecordAlreadyExists as e:
                messages.error(request, e.message)
                return redirect('khadya2')
        else:
            messages.error(request, "Please fill the form with correct data")
    else:
        form = PatraNabikaranForm()
    context = {'form': form}
    return render(request, 'forms/registration/renew.html', context)


@fo_and_ffsqrd_required
def udyog(request):
    """views for उद्योग सिफारिस"""
    
    if request.method == 'POST':
        form = UdyogSifarisForm(request.POST)
        if form.is_valid():
            try:
                UdyogSifaris.objects.create(created_by=request.user, **form.cleaned_data)
                messages.success(request, "Form submitted successfully")
                return redirect('udyog-report')
            except RecordAlreadyExists as e:
                messages.error(request, e.message)
                return redirect('udyog')
        else:
            messages.error(request, "Please fill the form with correct data")
    else:
        form = UdyogSifarisForm()
    context = {'form': form}
    return render(request, 'forms/registration/udyog.html', context)


@ie_required
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
            objects_to_create.append(AayatNiryat(created_by=request.user, **m_data))
            
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
            objects_to_create.append(AayatNiryat(created_by=request.user, **o_data))
            
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
            objects_to_create.append(AayatNiryat(created_by=request.user, **f_data))
            
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
            objects_to_create.append(AayatNiryat(created_by=request.user, **s_data))
            
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
            objects_to_create.append(AayatNiryat(created_by=request.user, **t_data))
            
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
            objects_to_create.append(AayatNiryat(created_by=request.user, **sa_data))
            
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
            objects_to_create.append(AayatNiryat(created_by=request.user, **k_data))
            
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
            objects_to_create.append(AayatNiryat(created_by=request.user, **w_data))
            
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
            objects_to_create.append(AayatNiryat(created_by=request.user, **sw_data))
            
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
            objects_to_create.append(AayatNiryat(created_by=request.user, **c_data))
            
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
            objects_to_create.append(AayatNiryat(created_by=request.user, **me_data))
            
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
            objects_to_create.append(AayatNiryat(created_by=request.user, **ot_data))
            
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
            objects_to_create.append(AayatNiryat(created_by=request.user, **g_data))
            
            try:
                AayatNiryat.objects.bulk_create(objects_to_create)
                messages.success(request, "Form submitted successfully")
                return redirect('import-export-report')
            except RecordAlreadyExists as e:
                messages.error(request, e.message)
                return redirect('aayat')
        else:
            messages.error(request, "Please fill the form with correct data")
    else:
        form = AayatNiryatForm()
    context = {
        'form': form,
        'data': data,
    }
    return render(request, 'forms/import-export/index.html', context)


#not fixed
@login_required
def ujuri(request):
    """views for उजुरी/गुनासो ब्येवस्थापन"""
    
    if request.method == 'POST':
        form = UjuriGunasoForm(request.POST)
        if form.is_valid():
            try:
                UjuriGunaso.objects.create(created_by=request.user, **form.cleaned_data)
                messages.success(request, "Form submitted successfully")
                return redirect('gunasho-report')
            except RecordAlreadyExists as e:
                messages.error(request, e.message)
                return redirect('ujuri')
        else:
            messages.error(request, "Please fill the form with correct data")
    else:
        form = UjuriGunasoForm()
    context = {'form': form}
    return render(request, 'forms/gunasho/index.html', context)


#not fixed
@login_required
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

        objects_to_create = []

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
                # khadya_object = form.save(commit=False)
                # khadya_object.save()
                objects_to_create.append(KhadyaPrasodhan(created_by=request.user, **form.cleaned_data))
            else:
                messages.error(request, "Please fill the form with correct data")
                return redirect('khadya-prasodhan')
        
        try:
            KhadyaPrasodhan.objects.bulk_create(objects_to_create)
            messages.success(request, "Form submitted successfully")
            return redirect('patrakar-report')
        except RecordAlreadyExists as e:
            messages.error(request, e.message)
            return redirect('khadya-prasodhan')
    else:
        form = KhadyaPrasodhanForm()
    context = {'form': form}
    return render(request, 'forms/hotel-patrakar/index.html', context)


#not fixed
@login_required
def masik_bittiya(request):
    """views for मासिक वित्तिय विवरण"""
    
    if request.method == 'POST':
        form = BittiyaBibaranForm(request.POST)
        if form.is_valid():
            try:
                BittiyaBibaran.objects.create(created_by=request.user, **form.cleaned_data)
                messages.success(request, "Form submitted successfully")
                return redirect('finance-report')
            except RecordAlreadyExists as e:
                messages.error(request, e.message)
                return redirect('masik-bittiya')
        else:
            messages.error(request, "Please fill the form with correct data")
        print(form.errors)
    else:
        form = BittiyaBibaranForm()
    context = {'form': form}
    return render(request, 'forms/account/summary.html', context)


@login_required
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
        
        objects_to_create = []
        
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
                objects_to_create.append(PragatiBibaran(created_by=request.user, **form.cleaned_data))
            else:
                messages.error(request, "Please fill the form with correct data")
                return redirect('masik-pragati')
        try:
            PragatiBibaran.objects.bulk_create(objects_to_create)
            messages.success(request, "Form submitted successfully")
            return redirect('monthly-report')
        except RecordAlreadyExists as e:
            messages.error(request, e.message)
            return redirect('masik-pragati')
    else:
        form = MasikPragatiForm()
    context = {'form': form, 'data': data}
    return render(request, 'forms/report/summary.html', context)


#----------------------------------------------- DETAILS FORM BELOW ----------------------------------------------------------------


@login_required
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
        
        objects_to_create = []
        
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
                objects_to_create.append(DetailHotel(created_by=request.user, **form.cleaned_data))
            else:
                messages.error(request, "Please fill the form with correct data")
                return redirect('d-hotel')
        try:
            DetailHotel.objects.bulk_create(objects_to_create)
            messages.success(request, "Form submitted successfully")
            return redirect('detail-hotel')
        except RecordAlreadyExists as e:
            messages.error(request, e.message)
            return redirect('d-hotel')
    else:
        form = DetailHotelForm()
    context = {'form': form, 'data': data}
    return render(request, 'forms/details/hotel.html', context)


@login_required
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
        
        objects_to_create = []
        
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
                objects_to_create.append(DetailRegistration(created_by=request.user, **form.cleaned_data))
            else:
                messages.error(request, "Please fill the form with correct data")
                return redirect('d-registration')
        try:
            DetailRegistration.objects.bulk_create(objects_to_create)
            messages.success(request, "Form submitted successfully")
            return redirect('detail-registration')
        except RecordAlreadyExists as e:
            messages.error(request, e.message)
            return redirect('d-registration')
    else:
        form = DetailRegistrationForm()
    context = {'form': form, 'data': data}
    return render(request, 'forms/details/registration.html', context)


@login_required
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
        
        objects_to_create = []
        
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
                objects_to_create.append(DetailRenew(created_by=request.user, **form.cleaned_data))
            else:
                messages.error(request, "Please fill the form with correct data")
                return redirect('d-renew')
        try:
            DetailRenew.objects.bulk_create(objects_to_create)
            messages.success(request, "Form submitted successfully")
            return redirect('detail-renew')
        except RecordAlreadyExists as e:
            messages.error(request, e.message)
            return redirect('d-renew')
    else:
        form = DetailRenewForm()
    context = {'form': form, 'data': data}
    return render(request, 'forms/details/renew.html', context)\


@login_required
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
        
        objects_to_create = []
        
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
                objects_to_create.append(DetailUdyog(created_by=request.user, **form.cleaned_data))
            else:
                messages.error(request, "Please fill the form with correct data")
                return redirect('d-udyog')
        try:
            DetailUdyog.objects.bulk_create(objects_to_create)
            messages.success(request, "Form submitted successfully")
            return redirect('detail-udyog')
        except RecordAlreadyExists as e:
            messages.error(request, e.message)
            return redirect('d-udyog')
    else:
        form = DetailUdyogForm()
    context = {'form': form, 'data': data}
    return render(request, 'forms/details/udyog.html', context)


@login_required
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
        
        objects_to_create = []
        
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
                objects_to_create.append(DetailAnugaman(created_by=request.user, **form.cleaned_data))
            else:
                messages.error(request, "Please fill the form with correct data")
                return redirect('d-anugaman')
        try:
            DetailAnugaman.objects.bulk_create()
            messages.success(request, "Form submitted successfully")
            return redirect('detail-anugaman')
        except RecordAlreadyExists as e:
            messages.error(request, e.message)
            return redirect('d-anugaman')
    else:
        form = DetailAnugamanForm()
    context = {'form': form, 'data': data}
    return render(request, 'forms/details/anugaman.html', context)


@login_required
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
        
        objects_to_create = []
        
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
                objects_to_create.append(DetailMudha(created_by=request.user, **form.cleaned_data))
            else:
                messages.error(request, "Please fill the form with correct data")
                return redirect('d-mudha')
        try:
            DetailMudha.objects.bulk_create(objects_to_create)    
            messages.success(request, "Form submitted successfully")
            return redirect('detail-mudha')
        except RecordAlreadyExists as e:
            messages.error(request, e.message)
            return redirect('d-mudha')
    else:
        form = DetailMudhaForm()
    context = {'form': form}
    return render(request, 'forms/details/mudha.html', context)


@ie_and_fo_required
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
        
        objects_to_create = []
        
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
                objects_to_create.append(DetailRbpa(created_by=request.user, **form.cleaned_data))
            else:
                messages.error(request, "Please fill the form with correct data")
                return redirect('d-rbpa')
        try:
            DetailRbpa.objects.bulk_create(objects_to_create)    
            messages.success(request, "Form submitted successfully")
            return redirect('rbpa-report')
        except RecordAlreadyExists as e:
            messages.error(request, e.message)
            return redirect('d-rbpa')
    else:
        form = DetailRbpaForm()
    context = {'form': form}
    return render(request, 'forms/details/rbpa.html', context)


@login_required
def detail_gunasho(request):
    """views for detail उजुरी गुनासो"""
    
    data = {
        'srot': commons.DETAIL_SROT_CHOICES,
    }
    if request.method == 'POST':
        d_p_miti = request.POST.getlist('p_miti[]')
        d_srot = request.POST.getlist('srot[]')
        d_s_miti = request.POST.getlist('s_miti[]')
        d_bibaran = request.POST.getlist('bibaran[]')
        
        objects_to_create = []
        
        for p_miti, srot, s_miti, bibaran in zip (d_p_miti, d_srot, d_s_miti, d_bibaran):
            form_data = {
                'p_miti': p_miti,
                'srot': srot,
                's_miti': s_miti,
                'bibaran': bibaran,
            }
            form = DetailGunasoForm(form_data)
            if form.is_valid():
                objects_to_create.append(DetailGunaso(created_by=request.user, **form.cleaned_data))
            else:
                messages.error(request, "Please fill the form with correct data")
                return redirect('d-gunasho')
        try:
            DetailGunaso.objects.bulk_create(objects_to_create)    
            messages.success(request, "Form submitted successfully")
            return redirect('detail-gunaso')
        except RecordAlreadyExists as e:
            messages.error(request, e.message)
            return redirect('d-gunasho')
    else:
        form = DetailGunasoForm()
    context = {'form': form, 'data': data}
    return render(request, 'forms/details/gunasho.html', context)



#------------------------------------------------------------REPORT PART-----------------------------------------------------------------


#----------------------------------------खाद्य ऐन/नियम बमोजिम संकलित नमुना विवरण(list, edit, delete)-----------------------------------------


@login_required
def khadyaact_report(request):
    """table list for खाद्य ऐन/नियम बमोजिम संकलित नमुना विवरण"""
    current_date = nepali_datetime.date.today().strftime("%Y-%m")
    total_sum = namunabibaran_sum(request)
    #obj = NamunaBibaran.objects.filter(is_verified=True).aggregate(total_milk=Sum('milk'))['total_milk']
    user_office = CustomUser.objects.filter(office=request.user.office)
    if request.user.role == 'A':
        data = NamunaBibaran.objects.filter(is_verified=True)
    elif request.user.role == 'V':
        data = NamunaBibaran.objects.all()
    else:
        data = NamunaBibaran.objects.filter(created_by__in=user_office)
    
    context = {'data': data, 'total_sum': total_sum}
    return render(request, 'report/khadyaact.html', context)


def khadyaact_view(request, id):
    obj = get_object_or_404(NamunaBibaran, id=id)
    context = {'obj': obj}
    return render(request, 'detail/khadyaact_detail.html', context)


def khadyaact_edit(request, id):
    khadya_object = get_object_or_404(NamunaBibaran, id=id)
    if request.method == 'POST':
        form = KhadyaactEditForm(request.POST, instance=khadya_object)
        if form.is_valid():
            form.save()
            messages.success(request, "Report Updated")
            return redirect('khadya-act-report')
        else:
            messages.error(request, 'Please fill the form with correct data')
    else:
        form = KhadyaactEditForm(instance=khadya_object)
    context = {'form': form, 'khadya_object': khadya_object}
    return render(request, 'edit_forms/namunabibaran_edit.html', context)


def khadyaact_report_delete(request, id):
    """for deleting निरीक्षण अनुगमन विवरण"""
    object = get_object_or_404(NamunaBibaran, id=id)
    object.delete()
    messages.success(request, "Report deleted")
    return redirect('khadya-act-report')


def khadyaact_remarks(request, id):
    obj = get_object_or_404(NamunaBibaran, id=id)
    if request.method == 'POST':
        updated_remarks = request.POST.get('remarks')
        if 'reject' in request.POST:
            obj.remarks = updated_remarks
            obj.is_rejected = True
            obj.save()
            messages.success(request,  "Remarks Sent (Rejected)")
        elif 'verify' in request.POST:
            obj.is_verified = True
            obj.save()
            messages.success(request, "Verified")
        return redirect('khadya-act-report')
    else:
        messages.error(request, "Bad Request")

#----------------------------------------------निरीक्षण अनुगमन विवरण(list, edit, delete)----------------------------------------------------


@login_required
def anugaman_report(request):
    """table list for निरीक्षण अनुगमन विवरण"""
    total_sum = anugamanbibaran_sum(request)
    user_office = CustomUser.objects.filter(office=request.user.office)
    if request.user.role == 'A':
        data = AnugamanBibaran.objects.filter(is_verified=True)
    elif request.user.role == 'V':
        data = AnugamanBibaran.objects.all()
    else:
        data = AnugamanBibaran.objects.filter(created_by__in=user_office)
    # month = request.query_params.get("month", "")
    # if month:
    #     data = data.filter(created_on_np_date__regex=r"[\d]*-{month}-[\d]*".format(month=month))
    context = {'data': data, 'total_sum': total_sum}
    return render(request, 'report/anugaman.html', context)


def anugaman_view(request, id):
    obj = get_object_or_404(AnugamanBibaran, id=id)
    context = {'obj': obj}
    return render(request, 'detail/anugaman_detail.html', context)


def anugaman_edit(request, id):
    """for editing निरीक्षण अनुगमन विवरण"""
    anugaman_object = get_object_or_404(AnugamanBibaran, id=id)
    if request.method == 'POST':
        form = AnugamanEditForm(request.POST, instance=anugaman_object)
        if form.is_valid():
            form.save()
            messages.success(request, "Report Updated")
            return redirect('anugaman-report')
        else:
            messages.error(request, 'Please fill the form with correct data')
    else:
        form = AnugamanEditForm(instance=anugaman_object)
    context = {'form': form, 'anugaman_object': anugaman_object}
    return render(request, 'edit_forms/anugaman_edit.html', context)


def anugaman_report_delete(request, id):
    """for deleting निरीक्षण अनुगमन विवरण"""
    object = get_object_or_404(AnugamanBibaran, id=id)
    object.delete()
    messages.success(request, "Report deleted")
    return redirect('anugaman-report')


def anugaman_remarks(request, id):
    obj = get_object_or_404(AnugamanBibaran, id=id)
    if request.method == 'POST':
        updated_remarks = request.POST.get('remarks')
        if 'reject' in request.POST:
            obj.remarks = updated_remarks
            obj.is_rejected = True
            obj.save()
            messages.success(request, "Remarks Sent (Rejected)")
        elif 'verify' in request.POST:
            obj.is_verified = True
            obj.save()
            messages.success(request, "Verified")
        return redirect('anugaman-report')
    else:
        messages.error(request, "Bad Request")


#--------------------------------------होटल स्तरीकरण लोगो वितरण सम्बन्धि विवरण(list, edit, delete)----------------------------------------


@login_required
def hotel_report(request):
    """table list for होटल स्तरीकरण लोगो वितरण सम्बन्धि विवरण"""
    total_sum = logobitaran_sum(request)
    user_office = CustomUser.objects.filter(office=request.user.office)
    if request.user.role == 'A':
        data = Logobitaran.objects.filter(is_verified=True)
    elif request.user.role == 'V':
        data = Logobitaran.objects.all()
    else:
        data = Logobitaran.objects.filter(created_by__in=user_office)
    
    context = {'data': data, 'total_sum': total_sum}
    return render(request, 'report/hotel.html', context)


def hotel_view(request, id):
    obj = get_object_or_404(Logobitaran, id=id)
    context = {'obj': obj}
    return render(request, 'detail/hotel_detail.html', context)


def hotel_edit(request, id):
    hotel_object = get_object_or_404(Logobitaran, id=id)
    if request.method == 'POST':
        form = HotelEditForm(request.POST, instance=hotel_object)
        if form.is_valid():
            form.save()
            messages.success(request, "Report Updated")
            return redirect('hotel-edit')
        else:
            messages.error(request, "Please fill the form with correct data")
    else:
        form = HotelEditForm(instance=hotel_object)
    context = {'form': form, 'hotel_object': hotel_object}
    return render(request, 'edit_forms/logobitaran_edit.html', context)


def hotel_report_delete(request, id):
    """table list for होटल स्तरीकरण लोगो वितरण सम्बन्धि विवरण"""

    object = get_object_or_404(Logobitaran, id=id)
    object.delete()
    messages.success(request, "Report deleted")
    return redirect('hotel-report')


def hotel_remarks(request, id):
    obj = get_object_or_404(Logobitaran, id=id)
    if request.method == 'POST':
        updated_remarks = request.POST.get('remarks')
        if 'reject' in request.POST:
            obj.remarks = updated_remarks
            obj.is_rejected = True
            obj.save()
            messages.success(request, "Remarks Sent (Rejected)")
        elif 'verify' in request.POST:
            obj.is_verified = True
            obj.save()
            messages.success(request, "Verified")
        return redirect('hotel-report')
    else:
        messages.error(request, "Bad Request")


#----------------------------------------खाद्य तथा दाना नमुना विश्लेषण विवरण(list, edit, delete)----------------------------------------------


@login_required
def khadya_report(request):
    """table list for खाद्य तथा दाना नमुना विश्लेषण विवरण"""
    total_sum = namunabisleysan_sum(request)
    user_office = CustomUser.objects.filter(office=request.user.office)
    if request.user.role == 'A':
        data = NamunaBisleysan.objects.filter(is_verified=True)
    elif request.user.role == 'V':
        data = NamunaBisleysan.objects.all()
    else:
        data = NamunaBisleysan.objects.filter(created_by__in=user_office)
    context = {'data': data, 'total_sum': total_sum}
    return render(request, 'report/khadyanamuna.html', context)


def khadya_view(request, id):
    obj = get_object_or_404(NamunaBisleysan, id=id)
    context = {'obj': obj}
    return render(request, 'detail/khadya_detail.html', context)


def khadya_edit(request, id):
    data = {
        'ekai': commons.EKAI_CHOICES,
    }
    k_object = get_object_or_404(NamunaBisleysan, id=id)
    if request.method == 'POST':
        form = KhadyaEditForm(request.POST, instance=k_object)
        if form.is_valid():
            form.save()
            messages.success(request, "Report Updated")
            return redirect('khadya-report')
        else:
            messages.error(request, "Please fill the form with correct data")
    else:
        form = KhadyaEditForm(instance=k_object)
    context = {'form': form, 'k_object': k_object, 'data': data}
    return render(request, 'edit_forms/khadya_edit.html', context)


def khadya_report_delete(request, id):
    """table list for होटल स्तरीकरण लोगो वितरण सम्बन्धि विवरण"""

    object = get_object_or_404(NamunaBisleysan, id=id)
    object.delete()
    messages.success(request, "Report deleted")
    return redirect('khadya-report')


def khadya_remarks(request, id):
    obj = get_object_or_404(NamunaBisleysan, id=id)
    if request.method == 'POST':
        updated_remarks = request.POST.get('remarks')
        if 'reject' in request.POST:
            obj.remarks = updated_remarks
            obj.is_rejected = True
            obj.save()
            messages.success(request, "Remarks Sent (Rejected)")
        elif 'verify' in request.POST:
            obj.is_verified = True
            obj.save()
            messages.success(request, "Verified")
        return redirect('khadya-report')
    else:
        messages.error(request, "Bad Request")


#------------------------------------------प्रयोगशाला विश्लेषण प्रतिवेदन सारांश(list, edit, delete)------------------------------------------


@login_required
def prayogsala_report(request):
    """table list for प्रयोगशाला विश्लेषण प्रतिवेदन सारांश"""
    total_sum = prayogsala_sum(request)
    user_office = CustomUser.objects.filter(office=request.user.office)
    if request.user.role == 'A':
        data = PrayogsalaBisleysan.objects.filter(is_verified=True)
    elif request.user.role == 'V':
        data = PrayogsalaBisleysan.objects.all()
    else:
        data = PrayogsalaBisleysan.objects.filter(created_by__in=user_office)
    context = {'data': data, 'total_sum': total_sum}
    return render(request, 'report/prayogsala.html', context)


def prayogsala_view(request, id):
    obj = get_object_or_404(PrayogsalaBisleysan, id=id)
    context = {'obj': obj}
    return render(request, 'detail/prayogsala_detail.html', context)


def prayogsala_edit(request, id):
    prayogsala_object = get_object_or_404(PrayogsalaBisleysan, id=id)
    if request.method == 'POST':
        form = PrayogsalaEditForm(request.POST, instance=prayogsala_object)
        if form.is_valid():
            form.save()
            messages.success(request, "Report Updated")
            return redirect('prayogsala-report')
        else:
            messages.error(request, "Please fill the form with correct data")
    else:
        form = PrayogsalaEditForm(instance=prayogsala_object)
    context = {'form': form, 'prayogsala_object': prayogsala_object}
    return render(request, 'edit_forms/prayogsala_edit.html', context)


def prayogsala_report_delete(request, id):
    """table list for होटल स्तरीकरण लोगो वितरण सम्बन्धि विवरण"""

    object = get_object_or_404(PrayogsalaBisleysan, id=id)
    object.delete()
    messages.success(request, "Report deleted")
    return redirect('prayogsala-report')


def prayogsala_remarks(request, id):
    obj = get_object_or_404(PrayogsalaBisleysan, id=id)
    if request.method == 'POST':
        updated_remarks = request.POST.get('remarks')
        if 'reject' in request.POST:
            obj.remarks = updated_remarks
            obj.is_rejected = True
            obj.save()
            messages.success(request, "Remarks Sent (Rejected)")
        elif 'verify' in request.POST:
            obj.is_verified = True
            obj.save()
            messages.success(request, "Verified")
        return redirect('prayogsala-report')
    else:
        messages.error(request, "Bad Request")


#------------------------------------------------RBPR Analysis Report(list, edit, delete)-------------------------------------------


@login_required
def rbpa_report(request):
    """table list for RBPA Analysis Report"""
    total_sum = rbpa_sum(request)
    user_office = CustomUser.objects.filter(office=request.user.office)
    if request.user.role == 'A':
        data = DetailRbpa.objects.filter(is_verified=True)
    elif request.user.role == 'V':
        data = DetailRbpa.objects.all()
    else:
        data = DetailRbpa.objects.filter(created_by__in=user_office)
    context = {'data': data, 'total_sum': total_sum}
    return render(request, 'report/rbpa.html', context)


def rbpa_view(request, id):
    obj = get_object_or_404(DetailRbpa, id=id)
    context = {'obj': obj}
    return render(request, 'detail/rbpa_detail.html', context)


def rbpa_edit(request, id):
    rbpa_object = get_object_or_404(DetailRbpa, id=id)
    if request.method == 'POST':
        form=RbpaEditForm(request.POST,instance=rbpa_object)
        if form.is_valid():
            form.save()
            messages.success(request, "Report Updated")
            return redirect('rbpa-report')
        else:
            messages.error(request, "Please fill the form with correct data")
    else:
        form=RbpaEditForm(instance=rbpa_object)
    context={'form':form,'rbpa_object':rbpa_object}
    return render(request,'edit_forms/rbpa_edit.html',context)


def rbpa_report_delete(request, id):
    """table list for होटल स्तरीकरण लोगो वितरण सम्बन्धि विवरण"""

    object = get_object_or_404(DetailRbpa, id=id)
    object.delete()
    messages.success(request, "Report deleted")
    return redirect('rbpa-report')


def rbpa_remarks(request, id):
    obj = get_object_or_404(DetailRbpa, id=id)
    if request.method == 'POST':
        updated_remarks = request.POST.get('remarks')
        if 'reject' in request.POST:
            obj.remarks = updated_remarks
            obj.is_rejected = True
            obj.save()
            messages.success(request, "Remarks Sent (Rejected)")
        elif 'verify' in request.POST:
            obj.is_verified = True
            obj.save()
            messages.success(request, "Verified")
        return redirect('rbpa-report')
    else:
        messages.error(request, "Bad Request")


#-------------------------------------------------उजुरी/गुनासो ब्येवस्थापन(list, edit, delete)---------------------------------------


@login_required
def importexport_report(request):
    """table list for आयात निर्यात गुण प्रमाणिकरण"""
    total_sum = ayatniryat_sum(request)
    user_office = CustomUser.objects.filter(office=request.user.office)
    if request.user.role == 'A':
        data = AayatNiryat.objects.filter(is_verified=True)
    elif request.user.role == 'V':
        data = AayatNiryat.objects.all()
    else:
        data = AayatNiryat.objects.filter(created_by__in=user_office)
    context = {'data': data, 'total_sum': total_sum}
    return render(request, 'report/importexport.html', context)


def importexport_view(request, id):
    obj = get_object_or_404(AayatNiryat, id=id)
    context = {'obj': obj}
    return render(request, 'detail/importexport_detail.html', context)


def importexport_edit(request, id):
    data = {
        'ekai': commons.EKAI_CHOICES,
    }
    ie_object = get_object_or_404(AayatNiryat, id=id)
    if request.method == 'POST':
        form=AayatNiryatEditForm(request.POST,instance=ie_object)
        if form.is_valid():
            form.save()
            messages.success(request, "Report Updated")
            return redirect('import-export-report')
        else:
            messages.error(request, "Please fill the form with correct data")
    else:
        form=AayatNiryatEditForm(instance=ie_object)
    context={'form':form,'ie_object': ie_object, 'data': data}
    return render(request,'edit_forms/importexport_edit.html',context)


def importexport_report_delete(request, id):
    """table list for होटल स्तरीकरण लोगो वितरण सम्बन्धि विवरण"""

    object = get_object_or_404(AayatNiryat, id=id)
    object.delete()
    messages.success(request, "Report deleted")
    return redirect('import-export-report')


def importexport_remarks(request, id):
    obj = get_object_or_404(AayatNiryat, id=id)
    if request.method == 'POST':
        updated_remarks = request.POST.get('remarks')
        if 'reject' in request.POST:
            obj.remarks = updated_remarks
            obj.is_rejected = True
            obj.save()
            messages.success(request, "Remarks Sent (Rejected)")
        elif 'verify' in request.POST:
            obj.is_verified = True
            obj.save()
            messages.success(request, "Verified")
        return redirect('import-export-report')
    else:
        messages.error(request, "Bad Request")
    

#------------------------------------------------working(list, edit, delete)-----------------------------------------------------


@login_required
def gunasho_report(request):
    """table list for उजुरी/गुनासो ब्येवस्थापन"""
    total_sum = ujurigunaso_sum(request)
    user_office = CustomUser.objects.filter(office=request.user.office)
    if request.user.role == 'A':
        data = UjuriGunaso.objects.filter(is_verified=True)
    elif request.user.role == 'V':
        data = UjuriGunaso.objects.all()
    else:
        data = UjuriGunaso.objects.filter(created_by__in=user_office)
    context = {'data': data, 'total_sum': total_sum}
    return render(request, 'report/gunasho.html', context)


def gunasho_view(request, id):
    obj = get_object_or_404(UjuriGunaso, id=id)
    context = {'obj': obj}
    return render(request, 'detail/gunasho_detail.html', context)


def gunasho_edit(request, id):
    gunasho_object = get_object_or_404(UjuriGunaso, id=id)
    if request.method == 'POST':
        form=UjuriGunasoEditForm(request.POST,instance=gunasho_object)
        if form.is_valid():
            form.save()
            messages.success(request, "Report Updated")
            return redirect('gunasho-report')
        else:
            messages.error(request, "Please fill the form with correct data")
    else:
        form=UjuriGunasoEditForm(instance=gunasho_object)
    context={'form':form,'gunasho_object':gunasho_object}
    return render(request,'edit_forms/gunasho_edit.html',context)


def gunasho_report_delete(request, id):
    """table list for होटल स्तरीकरण लोगो वितरण सम्बन्धि विवरण"""

    object = get_object_or_404(UjuriGunaso, id=id)
    object.delete()
    messages.success(request, "Report deleted")
    return redirect('gunasho-report')


def gunasho_remarks(request, id):
    obj = get_object_or_404(UjuriGunaso, id=id)
    if request.method == 'POST':
        updated_remarks = request.POST.get('remarks')
        if 'reject' in request.POST:
            obj.remarks = updated_remarks
            obj.is_rejected = True
            obj.save()
            messages.success(request, "Remarks Sent (Rejected)")
        elif 'verify' in request.POST:
            obj.is_verified = True
            obj.save()
            messages.success(request, "Verified")
        return redirect('gunasho-report')
    else:
        messages.error(request, "Bad Request")
    

#--------------------------------------------खाद्य प्रसोधन, खाद्य पोषण, उद्योग, होटेल, पत्रकार, कार्यशाला आदि-----------------------------------


@login_required
def patrakar_report(request):
    """table list for खाद्य प्रसोधन, खाद्य पोषण, उद्योग, होटेल, पत्रकार, कार्यशाला आदि"""
    total_sum = khadyaprasodhan_sum(request)
    user_office = CustomUser.objects.filter(office=request.user.office)
    if request.user.role == 'A':
        data = KhadyaPrasodhan.objects.filter(is_verified=True)
    elif request.user.role == 'V':
        data = KhadyaPrasodhan.objects.all()
    else:
        data = KhadyaPrasodhan.objects.filter(created_by__in=user_office)
    context = {'data': data, 'total_sum': total_sum}
    return render(request, 'report/patrakar.html', context)


def patrakar_view(request, id):
    obj = get_object_or_404(KhadyaPrasodhan, id=id)
    context = {'obj': obj}
    return render(request, 'detail/patrakar_detail.html', context)


def patrakar_edit(request, id):
    patrakar_object = get_object_or_404(KhadyaPrasodhan, id=id)
    if request.method == 'POST':
        form=KhadyaPrasodhanEditForm(request.POST,instance=patrakar_object)
        if form.is_valid():
            form.save()
            messages.success(request, "Report Updated")
            return redirect('patrakar-report')
        else:
            messages.error(request, "Please fill the form with correct data")
    else:
        form=KhadyaPrasodhanEditForm(instance=patrakar_object)
    context={'form':form,'patrakar_object':patrakar_object}
    return render(request,'edit_forms/patrakar_edit.html',context)


def patrakar_report_delete(request, id):
    """table list for होटल स्तरीकरण लोगो वितरण सम्बन्धि विवरण"""

    object = get_object_or_404(KhadyaPrasodhan, id=id)
    object.delete()
    messages.success(request, "Report deleted")
    return redirect('patrakar-report')


def patrakar_remarks(request, id):
    obj = get_object_or_404(KhadyaPrasodhan, id=id)
    if request.method == 'POST':
        updated_remarks = request.POST.get('remarks')
        if 'reject' in request.POST:
            obj.remarks = updated_remarks
            obj.is_rejected = True
            obj.save()
            messages.success(request, "Remarks Sent (Rejected)")
        elif 'verify' in request.POST:
            obj.is_verified = True
            obj.save()
            messages.success(request, "Verified")
        return redirect('patrakar-report')
    else:
        messages.error(request, "Bad Request")
    
    
#---------------------------------------------------------खाद्य तथा दाना अनुज्ञा पत्र जारी-------------------------------------------------


@login_required
def patrajari_report(request):
    """table list for खाद्य तथा दाना अनुज्ञा पत्र जारी"""
    total_sum = patrajari_sum(request)
    user_office = CustomUser.objects.filter(office=request.user.office)
    if request.user.role == 'A':
        data = PatraJari.objects.filter(is_verified=True)
    elif request.user.role == 'V':
        data = PatraJari.objects.all()
    else:
        data = PatraJari.objects.filter(created_by__in=user_office)
    context = {'data': data, 'total_sum': total_sum}
    return render(request, 'report/patrajari.html', context)


def patrajari_view(request, id):
    obj = get_object_or_404(PatraJari, id=id)
    context = {'obj': obj}
    return render(request, 'detail/patrajari_detail.html', context)


def patrajari_edit(request, id):
    patrajari_object = get_object_or_404(PatraJari, id=id)
    if request.method == 'POST':
        form=PatraJariEditForm(request.POST,instance=patrajari_object)
        if form.is_valid():
            form.save()
            messages.success(request, "Report Updated")
            return redirect('finance-report')
        else:
            messages.error(request, "Please fill the form with correct data")
    else:
        form=PatraJariEditForm(instance=patrajari_object)
    context={'form':form,'patrajari_object':patrajari_object}
    return render(request,'edit_forms/patrajari_edit.html',context)


def patrajari_report_delete(request, id):
    """table list for होटल स्तरीकरण लोगो वितरण सम्बन्धि विवरण"""

    object = get_object_or_404(PatraJari, id=id)
    object.delete()
    messages.success(request, "Report deleted")
    return redirect('patrajari-report')


def patrajari_remarks(request, id):
    obj = get_object_or_404(PatraJari, id=id)
    if request.method == 'POST':
        updated_remarks = request.POST.get('remarks')
        if 'reject' in request.POST:
            obj.remarks = updated_remarks
            obj.is_rejected = True
            obj.save()
            messages.success(request, "Remarks Sent (Rejected)")
        elif 'verify' in request.POST:
            obj.is_verified = True
            obj.save()
            messages.success(request, "Verified")
        return redirect('patrajari-report')
    else:
        messages.error(request, "Bad Request")
    
    
#----------------------------------------------------------खाद्य तथा दाना अनुज्ञा पत्र नविकरण


@login_required
def renew_report(request):
    """table list for खाद्य तथा दाना अनुज्ञा पत्र नविकरण"""
    total_sum = patranabikaran_sum(request)
    user_office = CustomUser.objects.filter(office=request.user.office)
    if request.user.role == 'A':
        data = PatraNabikaran.objects.filter(is_verified=True)
    elif request.user.role == 'V':
        data = PatraNabikaran.objects.all()
    else:
        data = PatraNabikaran.objects.filter(created_by__in=user_office)
    context = {'data': data, 'total_sum': total_sum}
    return render(request, 'report/renew.html', context)


def renew_view(request, id):
    obj = get_object_or_404(PatraNabikaran, id=id)
    context = {'obj': obj}
    return render(request, 'detail/renew_detail.html', context)


def renew_edit(request, id):
    renew_object = get_object_or_404(PatraNabikaran, id=id)
    if request.method == 'POST':
        form=PatraNabikaranEditForm(request.POST,instance=renew_object)
        if form.is_valid():
            form.save()
            messages.success(request, "Report Updated")
            return redirect('finance-report')
        else:
            messages.error(request, "Please fill the form with correct data")
    else:
        form=PatraNabikaranEditForm(instance=renew_object)
    context={'form':form,'renew_object':renew_object}
    return render(request,'edit_forms/renew_edit.html',context)


def renew_report_delete(request, id):
    """table list for होटल स्तरीकरण लोगो वितरण सम्बन्धि विवरण"""

    object = get_object_or_404(PatraNabikaran, id=id)
    object.delete()
    messages.success(request, "Report deleted")
    return redirect('renew-report')


def renew_remarks(request, id):
    obj = get_object_or_404(PatraNabikaran, id=id)
    if request.method == 'POST':
        updated_remarks = request.POST.get('remarks')
        if 'reject' in request.POST:
            obj.remarks = updated_remarks
            obj.is_rejected = True
            obj.save()
            messages.success(request, "Remarks Sent (Rejected)")
        elif 'verify' in request.POST:
            obj.is_verified = True
            obj.save()
            messages.success(request, "Verified")
        return redirect('renew-report')
    else:
        messages.error(request, "Bad Request")


#---------------------------------------------------------------उद्योग सिफारिस


@login_required
def udyog_report(request):
    """table list for उद्योग सिफारिस"""
    total_sum = udyogsifaris_sum(request)
    user_office = CustomUser.objects.filter(office=request.user.office)
    if request.user.role == 'A':
        data = UdyogSifaris.objects.filter(is_verified=True)
    elif request.user.role == 'V':
        data = UdyogSifaris.objects.all()
    else:
        data = UdyogSifaris.objects.filter(created_by__in=user_office)
    context = {'data': data, 'total_sum': total_sum}
    return render(request, 'report/udyog.html', context)


def udyog_view(request, id):
    obj = get_object_or_404(UdyogSifaris, id=id)
    context = {'obj': obj}
    return render(request, 'detail/udyog_detail.html', context)


def udyog_edit(request, id):
    udyog_object = get_object_or_404(UdyogSifaris, id=id)
    if request.method == 'POST':
        form=UdyogSifarisEditForm(request.POST,instance=udyog_object)
        if form.is_valid():
            form.save()
            messages.success(request, "Report Updated")
            return redirect('finance-report')
        else:
            messages.error(request, "Please fill the form with correct data")
    else:
        form=UdyogSifarisEditForm(instance=udyog_object)
    context={'form':form,'udyog_object':udyog_object}
    return render(request,'edit_forms/udyog_edit.html',context)


def udyog_report_delete(request, id):
    """table list for होटल स्तरीकरण लोगो वितरण सम्बन्धि विवरण"""

    object = get_object_or_404(UdyogSifaris, id=id)
    object.delete()
    messages.success(request, "Report deleted")
    return redirect('udyog-report')


def udyog_remarks(request, id):
    obj = get_object_or_404(UdyogSifaris, id=id)
    if request.method == 'POST':
        updated_remarks = request.POST.get('remarks')
        if 'reject' in request.POST:
            obj.remarks = updated_remarks
            obj.is_rejected = True
            obj.save()
            messages.success(request, "Remarks Sent (Rejected)")
        elif 'verify' in request.POST:
            obj.is_verified = True
            obj.save()
            messages.success(request, "Verified")
        return redirect('udyog-report')
    else:
        messages.error(request, "Bad Request")


#-------------------------------------------------------मासिक वित्तिय विवरण


@login_required
def finance_report(request):
    """table list for मासिक वित्तिय विवरण"""
    total_sum = bittiyabibaran_sum(request)
    user_office = CustomUser.objects.filter(office=request.user.office)
    if request.user.role == 'A':
        data = BittiyaBibaran.objects.filter(is_verified=True)
    elif request.user.role == 'V':
        data = BittiyaBibaran.objects.all()
    else:
        data = BittiyaBibaran.objects.filter(created_by__in=user_office)
    context = {'data': data, 'total_sum': total_sum}
    return render(request, 'report/finance.html', context)


def finance_view(request, id):
    obj = get_object_or_404(BittiyaBibaran, id=id)
    context = {'obj': obj}
    return render(request, 'detail/finance_detail.html', context)


def finance_edit(request, id):
    finance_object = get_object_or_404(BittiyaBibaran, id=id)
    if request.method == 'POST':
        form=BittiyaBibaranEditForm(request.POST,instance=finance_object)
        if form.is_valid():
            form.save()
            messages.success(request, "Report Updated")
            return redirect('finance-report')
        else:
            messages.error(request, "Please fill the form with correct data")
    else:
        form=BittiyaBibaranEditForm(instance=finance_object)
    context={'form':form,'finance_object':finance_object}
    return render(request,'edit_forms/finance_edit.html',context)


def finance_report_delete(request, id):
    """table list for होटल स्तरीकरण लोगो वितरण सम्बन्धि विवरण"""

    object = get_object_or_404(BittiyaBibaran, id=id)
    object.delete()
    messages.success(request, "Report deleted")
    return redirect('finance_report')


def finance_remarks(request, id):
    obj = get_object_or_404(BittiyaBibaran, id=id)
    if request.method == 'POST':
        updated_remarks = request.POST.get('remarks')
        if 'reject' in request.POST:
            obj.remarks = updated_remarks
            obj.is_rejected = True
            obj.save()
            messages.success(request, "Remarks Sent (Rejected)")
        elif 'verify' in request.POST:
            obj.is_verified = True
            obj.save()
            messages.success(request, "Verified")
        return redirect('finance-report')
    else:
        messages.error(request, "Bad Request")
        
        
#------------------------------------------------------मासिक प्रगति विवरण(list, edit, delete)-------------------------------------------------------


@login_required
def monthly_report(request):
    """table list for मासिक प्रगति विवरण"""
    user_office = CustomUser.objects.filter(office=request.user.office)
    if request.user.role == 'A':
        data = PragatiBibaran.objects.filter(is_verified=True)
    elif request.user.role == 'V':
        data = PragatiBibaran.objects.all()
    else:
        data = PragatiBibaran.objects.filter(created_by__in=user_office)
    context = {'data': data}
    return render(request, 'report/monthly.html', context)


def monthly_view(request, id):
    obj = get_object_or_404(PragatiBibaran, id=id)
    context = {'obj': obj}
    return render(request, 'detail/', context)


def monthly_edit(request):
    data = {
        'months': commons.MONTHS_CHOICES,
        'kharcha': commons.KHARCHA_CHOICES,
    }
    monthly_object = get_object_or_404(PragatiBibaran, id=id)
    if request.method == 'POST':
        form=PragatiBibaranEditForm(request.POST,instance=monthly_object)
        if form.is_valid():
            form.save()
            messages.success(request, "Report Updated")
            return redirect('monthly_report')
        else:
            messages.error(request, "Please fill the form with correct data")
    else:
        form=PragatiBibaranEditForm(instance=monthly_object)
    context={'form':form,'monthly_object':monthly_object, 'data': data}
    return render(request,'edit_forms/monthly_edit.html',context)


def monthly_report_delete(request, id):
    """table list for होटल स्तरीकरण लोगो वितरण सम्बन्धि विवरण"""

    object = get_object_or_404(PragatiBibaran, id=id)
    object.delete()
    messages.success(request, "Report deleted")
    return redirect('monthly-report')


def monthly_remarks(request, id):
    obj = get_object_or_404(PragatiBibaran, id=id)
    if request.method == 'POST':
        updated_remarks = request.POST.get('remarks')
        if 'reject' in request.POST:
            obj.remarks = updated_remarks
            obj.is_rejected = True
            obj.save()
            messages.success(request, "Remarks Sent (Rejected)")
        elif 'verify' in request.POST:
            obj.is_verified = True
            obj.save()
            messages.success(request, "Verified")
        return redirect('monthly-report')
    else:
        messages.error(request, "Bad Request")



















