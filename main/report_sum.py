from .models import (AayatNiryat, NamunaBibaran, AnugamanBibaran, Logobitaran,
                    NamunaBisleysan, PrayogsalaBisleysan, PatraJari, PatraNabikaran,
                    UdyogSifaris, UjuriGunaso, DetailRbpa, KhadyaPrasodhan, BittiyaBibaran)

from django.db.models import Sum
import nepali_datetime

def ayatniryat_sum(request):
    """calculates total sum of all instances of AayatNiryat model"""
    if request.user.role == 'DE':
        sum_values = AayatNiryat.objects.filter(
            created_by__office = request.user.office
        ).aggregate(
            total = Sum('b_lakshya') + Sum('c_lakshya') + Sum('c_pragati') +
                    Sum('m_pragati') + Sum('pratikul_n') + Sum('pratikul_p') +
                    Sum('h_pragati') + Sum('h_pratisat')
        )
    elif request.user.role == 'A':
        sum_values = AayatNiryat.objects.filter(
            is_verified = True
            ).aggregate(
            total = Sum('b_lakshya') + Sum('c_lakshya') + Sum('c_pragati') +
                    Sum('m_pragati') + Sum('pratikul_n') + Sum('pratikul_p') +
                    Sum('h_pragati') + Sum('h_pratisat')
        )
    else:
        sum_values = AayatNiryat.objects.aggregate(
            total = Sum('b_lakshya') + Sum('c_lakshya') + Sum('c_pragati') +
                    Sum('m_pragati') + Sum('pratikul_n') + Sum('pratikul_p') +
                    Sum('h_pragati') + Sum('h_pratisat')
        )
    total_sum = sum_values['total'] if 'total' in sum_values else 0
    return total_sum


def ayatniryat_monthly_sum(request, month):
    """calculates total sum of all instances of AayatNiryat model"""
    if request.user.role == 'DE':
        sum_values = AayatNiryat.objects.filter(
            created_by__office = request.user.office
        ).aggregate(
            total = Sum('b_lakshya') + Sum('c_lakshya') + Sum('c_pragati') +
                    Sum('m_pragati') + Sum('pratikul_n') + Sum('pratikul_p') +
                    Sum('h_pragati') + Sum('h_pratisat')
        )
    elif request.user.role == 'A':
        sum_values = AayatNiryat.objects.filter(
            is_verified = True, created_on_np_date__startswith=f'2080-{month}'
            ).aggregate(
            total = Sum('b_lakshya') + Sum('c_lakshya') + Sum('c_pragati') +
                    Sum('m_pragati') + Sum('pratikul_n') + Sum('pratikul_p') +
                    Sum('h_pragati') + Sum('h_pratisat')
        )
    else:
        sum_values = AayatNiryat.objects.aggregate(
            total = Sum('b_lakshya') + Sum('c_lakshya') + Sum('c_pragati') +
                    Sum('m_pragati') + Sum('pratikul_n') + Sum('pratikul_p') +
                    Sum('h_pragati') + Sum('h_pratisat')
        )
    total_sum = sum_values['total'] if 'total' in sum_values else 0
    return total_sum


def namunabibaran_sum(request):
    """calculates total sum of all instances of NamunaBibaran model"""
    if request.user.role == 'DE':
        sum_values = NamunaBibaran.objects.filter(
            created_by__office = request.user.office
        ).aggregate(
            total = Sum('milk') + Sum('oil') + Sum('fruits') + Sum('spice') + 
                    Sum('tea') + Sum('salt') + Sum('khadanna') + Sum('water') + 
                    Sum('sweets') + Sum('confectionery') + Sum('meat') + Sum('grain') +
                    Sum('others')
        )
    elif request.user.role == 'A':
        sum_values = NamunaBibaran.objects.filter(
            is_verified = True
        ).aggregate(
            total = Sum('milk') + Sum('oil') + Sum('fruits') + Sum('spice') + 
                    Sum('tea') + Sum('salt') + Sum('khadanna') + Sum('water') + 
                    Sum('sweets') + Sum('confectionery') + Sum('meat') + Sum('grain') +
                    Sum('others')
        )
    else:
        sum_values = NamunaBibaran.objects.aggregate(
            total = Sum('milk') + Sum('oil') + Sum('fruits') + Sum('spice') + 
                    Sum('tea') + Sum('salt') + Sum('khadanna') + Sum('water') + 
                    Sum('sweets') + Sum('confectionery') + Sum('meat') + Sum('grain') +
                    Sum('others')
        )
    total_sum = sum_values['total'] if 'total' in sum_values else 0
    return total_sum


def namunabibaran_monthly_sum(request, month):
    """calculates total sum of all instances of NamunaBibaran model for specific month"""
    
    current_date = nepali_datetime.date.today().strftime("%Y-%m")
    
    if request.user.role == 'DE':
        sum_values = NamunaBibaran.objects.filter(
            created_by__office = request.user.office, 
        ).aggregate(
            total = Sum('milk') + Sum('oil') + Sum('fruits') + Sum('spice') + 
                    Sum('tea') + Sum('salt') + Sum('khadanna') + Sum('water') + 
                    Sum('sweets') + Sum('confectionery') + Sum('meat') + Sum('grain') +
                    Sum('others')
        )
    elif request.user.role == 'A':
        sum_values = NamunaBibaran.objects.filter(
            is_verified = True, created_on_np_date__startswith=f'2080-{month}'
        ).aggregate(
            total = Sum('milk') + Sum('oil') + Sum('fruits') + Sum('spice') + 
                    Sum('tea') + Sum('salt') + Sum('khadanna') + Sum('water') + 
                    Sum('sweets') + Sum('confectionery') + Sum('meat') + Sum('grain') +
                    Sum('others')
        )
    else:
        sum_values = NamunaBibaran.objects.aggregate(
            total = Sum('milk') + Sum('oil') + Sum('fruits') + Sum('spice') + 
                    Sum('tea') + Sum('salt') + Sum('khadanna') + Sum('water') + 
                    Sum('sweets') + Sum('confectionery') + Sum('meat') + Sum('grain') +
                    Sum('others')
        )
    total_sum = sum_values['total'] if 'total' in sum_values else 0
    return total_sum


def anugamanbibaran_sum(request):
    """calculates total sum of all instances of AnugamanBibaran model"""
    if request.user.role == 'DE':
        sum_values = AnugamanBibaran.objects.filter(
            created_by__office = request.user.office
        ).aggregate(
            total = Sum('patak') + Sum('sankhya') + Sum('pragati')
        )
    elif request.user.role == 'A':
        sum_values = AnugamanBibaran.objects.filter(
            is_verified = True
        ).aggregate(
            total = Sum('patak') + Sum('sankhya') + Sum('pragati')
        )
    else:
        sum_values = AnugamanBibaran.objects.aggregate(
            total = Sum('patak') + Sum('sankhya') + Sum('pragati')
        )
    total_sum = sum_values['total'] if 'total' in sum_values else 0
    return total_sum


def anugamanbibaran_monthly_sum(request, month):
    """calculates total sum of all instances of AnugamanBibaran model for specific month"""
    if request.user.role == 'DE':
        sum_values = AnugamanBibaran.objects.filter(
            created_by__office = request.user.office
        ).aggregate(
            total = Sum('patak') + Sum('sankhya') + Sum('pragati')
        )
    elif request.user.role == 'A':
        sum_values = AnugamanBibaran.objects.filter(
            is_verified = True, created_on_np_date__startswith=f'2080-{month}'
        ).aggregate(
            total = Sum('patak') + Sum('sankhya') + Sum('pragati')
        )
    else:
        sum_values = AnugamanBibaran.objects.aggregate(
            total = Sum('patak') + Sum('sankhya') + Sum('pragati')
        )
    total_sum = sum_values['total'] if 'total' in sum_values else 0
    return total_sum


def logobitaran_sum(request):
    """calculates total sum of all instances of Logobitaran model"""
    if request.user.role == 'DE':
        sum_values = Logobitaran.objects.filter(
            created_by__office = request.user.office
        ).aggregate(
            total = Sum('c_pragati') + Sum('h_pragati1') + Sum('h_pragati2')
        )
    elif request.user.role == 'A':
        sum_values = Logobitaran.objects.filter(
            is_verified = True
        ).aggregate(
            total = Sum('c_pragati') + Sum('h_pragati1') + Sum('h_pragati2')
        )
    else:
        sum_values = Logobitaran.objects.aggregate(
            total = Sum('c_pragati') + Sum('h_pragati1') + Sum('h_pragati2')
        )
    total_sum = sum_values['total'] if 'total' in sum_values else 0
    return total_sum


def logobitaran_monthly_sum(request, month):
    """calculates total sum of all instances of Logobitaran model for specific month"""
    if request.user.role == 'DE':
        sum_values = Logobitaran.objects.filter(
            created_by__office = request.user.office
        ).aggregate(
            total = Sum('c_pragati') + Sum('h_pragati1') + Sum('h_pragati2')
        )
    elif request.user.role == 'A':
        sum_values = Logobitaran.objects.filter(
            is_verified = True, created_on_np_date__startswith=f'2080-{month}'
        ).aggregate(
            total = Sum('c_pragati') + Sum('h_pragati1') + Sum('h_pragati2')
        )
    else:
        sum_values = Logobitaran.objects.aggregate(
            total = Sum('c_pragati') + Sum('h_pragati1') + Sum('h_pragati2')
        )
    total_sum = sum_values['total'] if 'total' in sum_values else 0
    return total_sum


def namunabisleysan_sum(request):
    """calculates total sum of all instances of NamunaBisleysan model"""
    if request.user.role == 'DE':
        sum_values = NamunaBisleysan.objects.filter(
            created_by__office = request.user.office
        ).aggregate(
            total = Sum('lakshya') + Sum('pragati1') + Sum('mahina_pragati') + Sum('sankhya') + 
                    Sum('parameter') + Sum('pragati2') + Sum('pratisat')
        )
    elif request.user.role == 'A':
        sum_values = NamunaBisleysan.objects.filter(
            is_verified = True
        ).aggregate(
            total = Sum('lakshya') + Sum('pragati1') + Sum('mahina_pragati') + Sum('sankhya') + 
                    Sum('parameter') + Sum('pragati2') + Sum('pratisat')
        )
    else:
        sum_values = NamunaBisleysan.objects.aggregate(
            total = Sum('lakshya') + Sum('pragati1') + Sum('mahina_pragati') + Sum('sankhya') + 
                    Sum('parameter') + Sum('pragati2') + Sum('pratisat')
        )
    total_sum = sum_values['total'] if 'total' in sum_values else 0
    return total_sum


def namunabisleysan_monthly_sum(request, month):
    """calculates total sum of all instances of NamunaBisleysan model for specific month"""
    if request.user.role == 'DE':
        sum_values = NamunaBisleysan.objects.filter(
            created_by__office = request.user.office
        ).aggregate(
            total = Sum('lakshya') + Sum('pragati1') + Sum('mahina_pragati') + Sum('sankhya') + 
                    Sum('parameter') + Sum('pragati2') + Sum('pratisat')
        )
    elif request.user.role == 'A':
        sum_values = NamunaBisleysan.objects.filter(
            is_verified = True, created_on_np_date__startswith=f'2080-{month}'
        ).aggregate(
            total = Sum('lakshya') + Sum('pragati1') + Sum('mahina_pragati') + Sum('sankhya') + 
                    Sum('parameter') + Sum('pragati2') + Sum('pratisat')
        )
    else:
        sum_values = NamunaBisleysan.objects.aggregate(
            total = Sum('lakshya') + Sum('pragati1') + Sum('mahina_pragati') + Sum('sankhya') + 
                    Sum('parameter') + Sum('pragati2') + Sum('pratisat')
        )
    total_sum = sum_values['total'] if 'total' in sum_values else 0
    return total_sum


def prayogsala_sum(request):
    """calculates total sum of all instances of PrayogsalaBisleysan model"""
    if request.user.role == 'DE':
        sum_values = PrayogsalaBisleysan.objects.filter(
            created_by__office = request.user.office
        ).aggregate(
            total = Sum('b_sankhya') + Sum('b_pratikul') + Sum('u_sankhya') + Sum('u_pratikul') + 
                    Sum('ay_sankhya') + Sum('ay_pratikul') + Sum('v_sankhya') + Sum('v_pratikul') + 
                    Sum('k_sankhya') + Sum('k_pratikul') + Sum('a_sankhya') + Sum('a_pratikul') +
                    Sum('kul_sankhya')+ Sum('kul_pratikul')+ Sum('sample')
        )
    elif request.user.role == 'A':
        sum_values = PrayogsalaBisleysan.objects.filter(
            is_verified = True
        ).aggregate(
            total = Sum('b_sankhya') + Sum('b_pratikul') + Sum('u_sankhya') + Sum('u_pratikul') + 
                    Sum('ay_sankhya') + Sum('ay_pratikul') + Sum('v_sankhya') + Sum('v_pratikul') + 
                    Sum('k_sankhya') + Sum('k_pratikul') + Sum('a_sankhya') + Sum('a_pratikul') +
                    Sum('kul_sankhya')+ Sum('kul_pratikul')+ Sum('sample')
        )
    else:
        sum_values = PrayogsalaBisleysan.objects.aggregate(
            total = Sum('b_sankhya') + Sum('b_pratikul') + Sum('u_sankhya') + Sum('u_pratikul') + 
                    Sum('ay_sankhya') + Sum('ay_pratikul') + Sum('v_sankhya') + Sum('v_pratikul') + 
                    Sum('k_sankhya') + Sum('k_pratikul') + Sum('a_sankhya') + Sum('a_pratikul') +
                    Sum('kul_sankhya')+ Sum('kul_pratikul')+ Sum('sample')
        )
    total_sum = sum_values['total'] if 'total' in sum_values else 0
    return total_sum


def prayogsala_monthly_sum(request, month):
    """calculates total sum of all instances of PrayogsalaBisleysan model for specific month"""
    if request.user.role == 'DE':
        sum_values = PrayogsalaBisleysan.objects.filter(
            created_by__office = request.user.office
        ).aggregate(
            total = Sum('b_sankhya') + Sum('b_pratikul') + Sum('u_sankhya') + Sum('u_pratikul') + 
                    Sum('ay_sankhya') + Sum('ay_pratikul') + Sum('v_sankhya') + Sum('v_pratikul') + 
                    Sum('k_sankhya') + Sum('k_pratikul') + Sum('a_sankhya') + Sum('a_pratikul') +
                    Sum('kul_sankhya')+ Sum('kul_pratikul')+ Sum('sample')
        )
    elif request.user.role == 'A':
        sum_values = PrayogsalaBisleysan.objects.filter(
            is_verified = True, created_on_np_date__startswith=f'2080-{month}'
        ).aggregate(
            total = Sum('b_sankhya') + Sum('b_pratikul') + Sum('u_sankhya') + Sum('u_pratikul') + 
                    Sum('ay_sankhya') + Sum('ay_pratikul') + Sum('v_sankhya') + Sum('v_pratikul') + 
                    Sum('k_sankhya') + Sum('k_pratikul') + Sum('a_sankhya') + Sum('a_pratikul') +
                    Sum('kul_sankhya')+ Sum('kul_pratikul')+ Sum('sample')
        )
    else:
        sum_values = PrayogsalaBisleysan.objects.aggregate(
            total = Sum('b_sankhya') + Sum('b_pratikul') + Sum('u_sankhya') + Sum('u_pratikul') + 
                    Sum('ay_sankhya') + Sum('ay_pratikul') + Sum('v_sankhya') + Sum('v_pratikul') + 
                    Sum('k_sankhya') + Sum('k_pratikul') + Sum('a_sankhya') + Sum('a_pratikul') +
                    Sum('kul_sankhya')+ Sum('kul_pratikul')+ Sum('sample')
        )
    total_sum = sum_values['total'] if 'total' in sum_values else 0
    return total_sum


def patrajari_sum(request):
    """calculates total sum of all instances of PatraJari model"""
    if request.user.role == 'DE':
        sum_values = PatraJari.objects.filter(
            created_by__office = request.user.office
        ).aggregate(
            total = Sum('milk') + Sum('oil') + Sum('fruits') + Sum('spice') + 
                    Sum('tea') + Sum('salt') + Sum('khadanna') + Sum('water') + 
                    Sum('sweets') + Sum('confectionery') + Sum('meat') + Sum('grain') +
                    Sum('others')
        )
    elif request.user.role == 'A':
        sum_values = PatraJari.objects.filter(
            is_verified = True
        ).aggregate(
            total = Sum('milk') + Sum('oil') + Sum('fruits') + Sum('spice') + 
                    Sum('tea') + Sum('salt') + Sum('khadanna') + Sum('water') + 
                    Sum('sweets') + Sum('confectionery') + Sum('meat') + Sum('grain') +
                    Sum('others')
        )
    else:
        sum_values = PatraJari.objects.aggregate(
            total = Sum('milk') + Sum('oil') + Sum('fruits') + Sum('spice') + 
                    Sum('tea') + Sum('salt') + Sum('khadanna') + Sum('water') + 
                    Sum('sweets') + Sum('confectionery') + Sum('meat') + Sum('grain') +
                    Sum('others')
        )
    total_sum = sum_values['total'] if 'total' in sum_values else 0
    return total_sum


def patrajari_monthly_sum(request, month):
    """calculates total sum of all instances of PatraJari model for specific month"""
    if request.user.role == 'DE':
        sum_values = PatraJari.objects.filter(
            created_by__office = request.user.office
        ).aggregate(
            total = Sum('milk') + Sum('oil') + Sum('fruits') + Sum('spice') + 
                    Sum('tea') + Sum('salt') + Sum('khadanna') + Sum('water') + 
                    Sum('sweets') + Sum('confectionery') + Sum('meat') + Sum('grain') +
                    Sum('others')
        )
    elif request.user.role == 'A':
        sum_values = PatraJari.objects.filter(
            is_verified = True, created_on_np_date__startswith=f'2080-{month}'
        ).aggregate(
            total = Sum('milk') + Sum('oil') + Sum('fruits') + Sum('spice') + 
                    Sum('tea') + Sum('salt') + Sum('khadanna') + Sum('water') + 
                    Sum('sweets') + Sum('confectionery') + Sum('meat') + Sum('grain') +
                    Sum('others')
        )
    else:
        sum_values = PatraJari.objects.aggregate(
            total = Sum('milk') + Sum('oil') + Sum('fruits') + Sum('spice') + 
                    Sum('tea') + Sum('salt') + Sum('khadanna') + Sum('water') + 
                    Sum('sweets') + Sum('confectionery') + Sum('meat') + Sum('grain') +
                    Sum('others')
        )
    total_sum = sum_values['total'] if 'total' in sum_values else 0
    return total_sum


def patranabikaran_sum(request):
    """calculates total sum of all instances of PatraNabikaran model"""
    if request.user.role == 'DE':
        sum_values = PatraNabikaran.objects.filter(
            created_by__office = request.user.office
        ).aggregate(
            total = Sum('milk') + Sum('oil') + Sum('fruits') + Sum('spice') + 
                    Sum('tea') + Sum('salt') + Sum('khadanna') + Sum('water') + 
                    Sum('sweets') + Sum('confectionery') + Sum('meat') + Sum('grain') +
                    Sum('others')
        )
    elif request.user.role == 'A':
        sum_values = PatraNabikaran.objects.filter(
            is_verified = True
        ).aggregate(
            total = Sum('milk') + Sum('oil') + Sum('fruits') + Sum('spice') + 
                    Sum('tea') + Sum('salt') + Sum('khadanna') + Sum('water') + 
                    Sum('sweets') + Sum('confectionery') + Sum('meat') + Sum('grain') +
                    Sum('others')
        )
    else:
        sum_values = PatraNabikaran.objects.aggregate(
            total = Sum('milk') + Sum('oil') + Sum('fruits') + Sum('spice') + 
                    Sum('tea') + Sum('salt') + Sum('khadanna') + Sum('water') + 
                    Sum('sweets') + Sum('confectionery') + Sum('meat') + Sum('grain') +
                    Sum('others')
        )
    total_sum = sum_values['total'] if 'total' in sum_values else 0
    return total_sum


def patranabikaran_monthly_sum(request, month):
    """calculates total sum of all instances of PatraNabikaran model"""
    if request.user.role == 'DE':
        sum_values = PatraNabikaran.objects.filter(
            created_by__office = request.user.office
        ).aggregate(
            total = Sum('milk') + Sum('oil') + Sum('fruits') + Sum('spice') + 
                    Sum('tea') + Sum('salt') + Sum('khadanna') + Sum('water') + 
                    Sum('sweets') + Sum('confectionery') + Sum('meat') + Sum('grain') +
                    Sum('others')
        )
    elif request.user.role == 'A':
        sum_values = PatraNabikaran.objects.filter(
            is_verified = True, created_on_np_date__startswith=f'2080-{month}'
        ).aggregate(
            total = Sum('milk') + Sum('oil') + Sum('fruits') + Sum('spice') + 
                    Sum('tea') + Sum('salt') + Sum('khadanna') + Sum('water') + 
                    Sum('sweets') + Sum('confectionery') + Sum('meat') + Sum('grain') +
                    Sum('others')
        )
    else:
        sum_values = PatraNabikaran.objects.aggregate(
            total = Sum('milk') + Sum('oil') + Sum('fruits') + Sum('spice') + 
                    Sum('tea') + Sum('salt') + Sum('khadanna') + Sum('water') + 
                    Sum('sweets') + Sum('confectionery') + Sum('meat') + Sum('grain') +
                    Sum('others')
        )
    total_sum = sum_values['total'] if 'total' in sum_values else 0
    return total_sum


def udyogsifaris_sum(request):
    """calculates total sum of all instances of UdyogSifaris model"""
    if request.user.role == 'DE':
        sum_values = UdyogSifaris.objects.filter(
            created_by__office = request.user.office
        ).aggregate(
            total = Sum('milk') + Sum('oil') + Sum('fruits') + Sum('spice') + 
                    Sum('tea') + Sum('salt') + Sum('khadanna') + Sum('water') + 
                    Sum('sweets') + Sum('confectionery') + Sum('meat') + Sum('grain') +
                    Sum('others')
        )
    elif request.user.role == 'A':
        sum_values = UdyogSifaris.objects.filter(
            is_verified = True
        ).aggregate(
            total = Sum('milk') + Sum('oil') + Sum('fruits') + Sum('spice') + 
                    Sum('tea') + Sum('salt') + Sum('khadanna') + Sum('water') + 
                    Sum('sweets') + Sum('confectionery') + Sum('meat') + Sum('grain') +
                    Sum('others')
        )
    else:
        sum_values = UdyogSifaris.objects.aggregate(
            total = Sum('milk') + Sum('oil') + Sum('fruits') + Sum('spice') + 
                    Sum('tea') + Sum('salt') + Sum('khadanna') + Sum('water') + 
                    Sum('sweets') + Sum('confectionery') + Sum('meat') + Sum('grain') +
                    Sum('others')
        )
    total_sum = sum_values['total'] if 'total' in sum_values else 0
    return total_sum


def udyogsifaris_monthly_sum(request, month):
    """calculates total sum of all instances of UdyogSifaris model"""
    if request.user.role == 'DE':
        sum_values = UdyogSifaris.objects.filter(
            created_by__office = request.user.office
        ).aggregate(
            total = Sum('milk') + Sum('oil') + Sum('fruits') + Sum('spice') + 
                    Sum('tea') + Sum('salt') + Sum('khadanna') + Sum('water') + 
                    Sum('sweets') + Sum('confectionery') + Sum('meat') + Sum('grain') +
                    Sum('others')
        )
    elif request.user.role == 'A':
        sum_values = UdyogSifaris.objects.filter(
            is_verified = True, created_on_np_date__startswith=f'2080-{month}'
        ).aggregate(
            total = Sum('milk') + Sum('oil') + Sum('fruits') + Sum('spice') + 
                    Sum('tea') + Sum('salt') + Sum('khadanna') + Sum('water') + 
                    Sum('sweets') + Sum('confectionery') + Sum('meat') + Sum('grain') +
                    Sum('others')
        )
    else:
        sum_values = UdyogSifaris.objects.aggregate(
            total = Sum('milk') + Sum('oil') + Sum('fruits') + Sum('spice') + 
                    Sum('tea') + Sum('salt') + Sum('khadanna') + Sum('water') + 
                    Sum('sweets') + Sum('confectionery') + Sum('meat') + Sum('grain') +
                    Sum('others')
        )
    total_sum = sum_values['total'] if 'total' in sum_values else 0
    return total_sum


def ujurigunaso_sum(request):
    """calculates total sum of all instances of UjuriGunaso model"""
    if request.user.role == 'DE':
        sum_values = UjuriGunaso.objects.filter(
            created_by__office = request.user.office
        ).aggregate(
            total = Sum('gunaso_petika') + Sum('gunaso_adhikari') + Sum('zilla') + Sum('banijya') + 
                    Sum('patra') + Sum('akhtiyar') + Sum('patrakar') + Sum('sarkar') + 
                    Sum('upavokta') + Sum('others') + Sum('jamma') + Sum('sambodhan')
        )
    elif request.user.role == 'A':
        sum_values = UjuriGunaso.objects.filter(
            is_verified = True
        ).aggregate(
            total = Sum('gunaso_petika') + Sum('gunaso_adhikari') + Sum('zilla') + Sum('banijya') + 
                    Sum('patra') + Sum('akhtiyar') + Sum('patrakar') + Sum('sarkar') + 
                    Sum('upavokta') + Sum('others') + Sum('jamma') + Sum('sambodhan')
        )
    else:
        sum_values = UjuriGunaso.objects.aggregate(
            total = Sum('gunaso_petika') + Sum('gunaso_adhikari') + Sum('zilla') + Sum('banijya') + 
                    Sum('patra') + Sum('akhtiyar') + Sum('patrakar') + Sum('sarkar') + 
                    Sum('upavokta') + Sum('others') + Sum('jamma') + Sum('sambodhan')
        )
    total_sum = sum_values['total'] if 'total' in sum_values else 0
    return total_sum


def ujurigunaso_monthly_sum(request, month):
    """calculates total sum of all instances of UjuriGunaso model"""
    if request.user.role == 'DE':
        sum_values = UjuriGunaso.objects.filter(
            created_by__office = request.user.office
        ).aggregate(
            total = Sum('gunaso_petika') + Sum('gunaso_adhikari') + Sum('zilla') + Sum('banijya') + 
                    Sum('patra') + Sum('akhtiyar') + Sum('patrakar') + Sum('sarkar') + 
                    Sum('upavokta') + Sum('others') + Sum('jamma') + Sum('sambodhan')
        )
    elif request.user.role == 'A':
        sum_values = UjuriGunaso.objects.filter(
            is_verified = True, created_on_np_date__startswith=f'2080-{month}'
        ).aggregate(
            total = Sum('gunaso_petika') + Sum('gunaso_adhikari') + Sum('zilla') + Sum('banijya') + 
                    Sum('patra') + Sum('akhtiyar') + Sum('patrakar') + Sum('sarkar') + 
                    Sum('upavokta') + Sum('others') + Sum('jamma') + Sum('sambodhan')
        )
    else:
        sum_values = UjuriGunaso.objects.aggregate(
            total = Sum('gunaso_petika') + Sum('gunaso_adhikari') + Sum('zilla') + Sum('banijya') + 
                    Sum('patra') + Sum('akhtiyar') + Sum('patrakar') + Sum('sarkar') + 
                    Sum('upavokta') + Sum('others') + Sum('jamma') + Sum('sambodhan')
        )
    total_sum = sum_values['total'] if 'total' in sum_values else 0
    return total_sum


def rbpa_sum(request):
    """calculates total sum of all instances of DetailRbpa model"""
    if request.user.role == 'DE':
        sum_values = DetailRbpa.objects.filter(
            created_by__office = request.user.office
        ).aggregate(
            total = Sum('sample1') + Sum('quantity1') + Sum('sample2') + 
                    Sum('quantity2') + Sum('sample3') + Sum('quantity3')
        )
    elif request.user.role == 'A':
        sum_values = DetailRbpa.objects.filter(
            is_verified = True
        ).aggregate(
            total = Sum('sample1') + Sum('quantity1') + Sum('sample2') + 
                    Sum('quantity2') + Sum('sample3') + Sum('quantity3')
        )
    else:
        sum_values = DetailRbpa.objects.aggregate(
            total = Sum('sample1') + Sum('quantity1') + Sum('sample2') + 
                    Sum('quantity2') + Sum('sample3') + Sum('quantity3')
        )
    total_sum = sum_values['total'] if 'total' in sum_values else 0
    return total_sum


def rbpa_monthly_sum(request, month):
    """calculates total sum of all instances of DetailRbpa model"""
    if request.user.role == 'DE':
        sum_values = DetailRbpa.objects.filter(
            created_by__office = request.user.office
        ).aggregate(
            total = Sum('sample1') + Sum('quantity1') + Sum('sample2') + 
                    Sum('quantity2') + Sum('sample3') + Sum('quantity3')
        )
    elif request.user.role == 'A':
        sum_values = DetailRbpa.objects.filter(
            is_verified = True, created_on_np_date__startswith=f'2080-{month}'
        ).aggregate(
            total = Sum('sample1') + Sum('quantity1') + Sum('sample2') + 
                    Sum('quantity2') + Sum('sample3') + Sum('quantity3')
        )
    else:
        sum_values = DetailRbpa.objects.aggregate(
            total = Sum('sample1') + Sum('quantity1') + Sum('sample2') + 
                    Sum('quantity2') + Sum('sample3') + Sum('quantity3')
        )
    total_sum = sum_values['total'] if 'total' in sum_values else 0
    return total_sum


def khadyaprasodhan_sum(request):
    """calculates total sum of all instances of KhadyaPrasodhan model"""
    if request.user.role == 'DE':
        sum_values = KhadyaPrasodhan.objects.filter(
            created_by__office = request.user.office
        ).aggregate(
            total = Sum('m_sankhya') + Sum('p_sankhya')
        )
    elif request.user.role == 'A':
        sum_values = KhadyaPrasodhan.objects.filter(
            is_verified = True
        ).aggregate(
            total = Sum('m_sankhya') + Sum('p_sankhya')
        )
    else:
        sum_values = KhadyaPrasodhan.objects.aggregate(
            total = Sum('m_sankhya') + Sum('p_sankhya')
        )
    total_sum = sum_values['total'] if 'total' in sum_values else 0
    return total_sum


def bittiyabibaran_sum(request):
    """calculates total sum of all instances of BittiyaBibaran model"""
    if request.user.role == 'DE':
        sum_values = BittiyaBibaran.objects.filter(
            created_by__office = request.user.office
        ).aggregate(
            total = Sum('yearly_pujigat') + Sum('yearly_chalu') + Sum('monthly_pujigat') +
                    Sum('monthly_chalu') + Sum('monthly_rajaswo')
        )
    elif request.user.role == 'A':
        sum_values = BittiyaBibaran.objects.filter(
            is_verified = True
        ).aggregate(
            total = Sum('yearly_pujigat') + Sum('yearly_chalu') + Sum('monthly_pujigat') +
                    Sum('monthly_chalu') + Sum('monthly_rajaswo')
        )
    else:
        sum_values = BittiyaBibaran.objects.aggregate(
            total = Sum('yearly_pujigat') + Sum('yearly_chalu') + Sum('monthly_pujigat') +
                    Sum('monthly_chalu') + Sum('monthly_rajaswo')
        )
    total_sum = sum_values['total'] if 'total' in sum_values else 0
    return total_sum


#--------------------------------------MONTHLY PROGRESS REPORT OF EACH OFFICE-------------------------------------------------

def office_namunabibaran_monthly_sum(request, office_id, month):
    """calculates total sum of NamunaBibaran model for specific month of specific office"""
    if request.user.role == 'A' or request.user.role == 'V':
        sum_values = NamunaBibaran.objects.filter(
            is_verified = True, created_by__office=office_id, created_on_np_date__startswith=f'2080-{month}'
        ).aggregate(
            total = Sum('milk') + Sum('oil') + Sum('fruits') + Sum('spice') + 
                    Sum('tea') + Sum('salt') + Sum('khadanna') + Sum('water') + 
                    Sum('sweets') + Sum('confectionery') + Sum('meat') + Sum('grain') +
                    Sum('others')
        )
    else:
        None
    total_sum = sum_values['total'] if 'total' in sum_values else 0
    return total_sum


def office_anugamanbibaran_monthly_sum(request, office_id, month):
    """calculates total sum of AnugamanBibaran model for specific month of specific office"""
    if request.user.role == 'A' or request.user.role == 'V':
        sum_values = AnugamanBibaran.objects.filter(
            is_verified = True, created_by__office=office_id, created_on_np_date__startswith=f'2080-{month}'
        ).aggregate(
            total = Sum('patak') + Sum('sankhya') + Sum('pragati')
        )
    else:
        None
    total_sum = sum_values['total'] if 'total' in sum_values else 0
    return total_sum


def office_logobitaran_monthly_sum(request, office_id, month):
    """calculates total sum of Logobitaran model for specific month of specific office"""
    if request.user.role == 'A' or request.user.role == 'V':
        sum_values = Logobitaran.objects.filter(
            is_verified = True, created_by__office=office_id, created_on_np_date__startswith=f'2080-{month}'
        ).aggregate(
            total = Sum('c_pragati') + Sum('h_pragati1') + Sum('h_pragati2')
        )
    else:
        None
    total_sum = sum_values['total'] if 'total' in sum_values else 0
    return total_sum


def office_namunabisleysan_monthly_sum(request, office_id, month):
    """calculates total sum of NamunaBisleysan model for specific month of specific office"""
    if request.user.role == 'A' or request.user.role == 'V':
        sum_values = NamunaBisleysan.objects.filter(
            is_verified = True, created_by__office=office_id, created_on_np_date__startswith=f'2080-{month}'
        ).aggregate(
            total = Sum('lakshya') + Sum('pragati1') + Sum('mahina_pragati') + Sum('sankhya') + 
                    Sum('parameter') + Sum('pragati2') + Sum('pratisat')
        )
    else:
        None
    total_sum = sum_values['total'] if 'total' in sum_values else 0
    return total_sum


def office_prayogsala_monthly_sum(request, office_id, month):
    """calculates total sum of PrayogsalaBisleysan model for specific month of specific office"""
    if request.user.role == 'A' or request.user.role == 'V':
        sum_values = PrayogsalaBisleysan.objects.filter(
            is_verified = True, created_by__office=office_id, created_on_np_date__startswith=f'2080-{month}'
        ).aggregate(
            total = Sum('b_sankhya') + Sum('b_pratikul') + Sum('u_sankhya') + Sum('u_pratikul') + 
                    Sum('ay_sankhya') + Sum('ay_pratikul') + Sum('v_sankhya') + Sum('v_pratikul') + 
                    Sum('k_sankhya') + Sum('k_pratikul') + Sum('a_sankhya') + Sum('a_pratikul') +
                    Sum('kul_sankhya')+ Sum('kul_pratikul')+ Sum('sample')
        )
    else:
        None
    total_sum = sum_values['total'] if 'total' in sum_values else 0
    return total_sum


def office_patrajari_monthly_sum(request, office_id, month):
    """calculates total sum of PatraJari model for specific month of specific month"""
    if request.user.role == 'A' or request.user.role == 'V':
        sum_values = PatraJari.objects.filter(
            is_verified = True, created_by__office=office_id, created_on_np_date__startswith=f'2080-{month}'
        ).aggregate(
            total = Sum('milk') + Sum('oil') + Sum('fruits') + Sum('spice') + 
                    Sum('tea') + Sum('salt') + Sum('khadanna') + Sum('water') + 
                    Sum('sweets') + Sum('confectionery') + Sum('meat') + Sum('grain') +
                    Sum('others')
        )
    else:
        None
    total_sum = sum_values['total'] if 'total' in sum_values else 0
    return total_sum


def office_patranabikaran_monthly_sum(request, office_id, month):
    """calculates total sum of PatraNabikaran model for specific month"""
    if request.user.role == 'A' or request.user.role == 'V':
        sum_values = PatraNabikaran.objects.filter(
            is_verified = True, created_by__office=office_id, created_on_np_date__startswith=f'2080-{month}'
        ).aggregate(
            total = Sum('milk') + Sum('oil') + Sum('fruits') + Sum('spice') + 
                    Sum('tea') + Sum('salt') + Sum('khadanna') + Sum('water') + 
                    Sum('sweets') + Sum('confectionery') + Sum('meat') + Sum('grain') +
                    Sum('others')
        )
    else:
        None
    total_sum = sum_values['total'] if 'total' in sum_values else 0
    return total_sum


def office_udyogsifaris_monthly_sum(request, office_id, month):
    """calculates total sum of UdyogSifaris model of specific month"""
    if request.user.role == 'A' or request.user.role == 'V':
        sum_values = UdyogSifaris.objects.filter(
            is_verified = True, created_by__office=office_id, created_on_np_date__startswith=f'2080-{month}'
        ).aggregate(
            total = Sum('milk') + Sum('oil') + Sum('fruits') + Sum('spice') + 
                    Sum('tea') + Sum('salt') + Sum('khadanna') + Sum('water') + 
                    Sum('sweets') + Sum('confectionery') + Sum('meat') + Sum('grain') +
                    Sum('others')
        )
    else:
        None
    total_sum = sum_values['total'] if 'total' in sum_values else 0
    return total_sum


def office_ujurigunaso_monthly_sum(request, office_id, month):
    """calculates total sum of UjuriGunaso model of specific month of specific office"""
    if request.user.role == 'A' or request.user.role == 'V':
        sum_values = UjuriGunaso.objects.filter(
            is_verified = True, created_by__office=office_id, created_on_np_date__startswith=f'2080-{month}'
        ).aggregate(
            total = Sum('gunaso_petika') + Sum('gunaso_adhikari') + Sum('zilla') + Sum('banijya') + 
                    Sum('patra') + Sum('akhtiyar') + Sum('patrakar') + Sum('sarkar') + 
                    Sum('upavokta') + Sum('others') + Sum('jamma') + Sum('sambodhan')
        )
    else:
        None
    total_sum = sum_values['total'] if 'total' in sum_values else 0
    return total_sum


def office_rbpa_monthly_sum(request, office_id, month):
    """calculates total sum of DetailRbpa model of specific month of specific office"""
    if request.user.role == 'A' or request.user.role == 'V':
        sum_values = DetailRbpa.objects.filter(
            is_verified = True, created_by__office=office_id, created_on_np_date__startswith=f'2080-{month}'
        ).aggregate(
            total = Sum('sample1') + Sum('quantity1') + Sum('sample2') + 
                    Sum('quantity2') + Sum('sample3') + Sum('quantity3')
        )
    else:
        None
    total_sum = sum_values['total'] if 'total' in sum_values else 0
    return total_sum


def office_ayatniryat_monthly_sum(request, office_id, month):
    """calculates total sum of AayatNiryat model of specific month and office"""
    if request.user.role == 'A' or request.user.role == 'V':
        sum_values = AayatNiryat.objects.filter(
            is_verified = True, created_by__office=office_id, created_on_np_date__startswith=f'2080-{month}'
            ).aggregate(
            total = Sum('b_lakshya') + Sum('c_lakshya') + Sum('c_pragati') +
                    Sum('m_pragati') + Sum('pratikul_n') + Sum('pratikul_p') +
                    Sum('h_pragati') + Sum('h_pratisat')
        )
    else:
        None
    total_sum = sum_values['total'] if 'total' in sum_values else 0
    return total_sum