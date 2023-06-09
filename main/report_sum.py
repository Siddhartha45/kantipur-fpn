from .models import (AayatNiryat, NamunaBibaran, AnugamanBibaran, Logobitaran,
                    NamunaBisleysan, PrayogsalaBisleysan, PatraJari, PatraNabikaran,
                    UdyogSifaris, UjuriGunaso, DetailRbpa)

from django.db.models import Sum

def ayatniryat_sum(request):
    if request.user.role == 'DE':
        sum_values = AayatNiryat.objects.filter(
            created_by__office = request.user.office
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
    if request.user.role == 'DE':
        sum_values = NamunaBibaran.objects.filter(
            created_by__office = request.user.office
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
    if request.user.role == 'DE':
        sum_values = AnugamanBibaran.objects.filter(
            created_by__office = request.user.office
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
    if request.user.role == 'DE':
        sum_values = Logobitaran.objects.filter(
            created_by__office = request.user.office
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
    if request.user.role == 'DE':
        sum_values = NamunaBisleysan.objects.filter(
            created_by__office = request.user.office
        ).aggregate(
            total = Sum('lakshya') + Sum('pragati1') + Sum('mahina_pragati') + Sum('sankhya') + 
                    Sum('parameter') + Sum('pragati2')
        )
    else:
        sum_values = NamunaBisleysan.objects.aggregate(
            total = Sum('lakshya') + Sum('pragati1') + Sum('mahina_pragati') + Sum('sankhya') + 
                    Sum('parameter') + Sum('pragati2')
        )
    total_sum = sum_values['total'] if 'total' in sum_values else 0
    return total_sum


def prayogsala_sum(request):
    if request.user.role == 'DE':
        sum_values = PrayogsalaBisleysan.objects.filter(
            created_by__office = request.user.office
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
    if request.user.role == 'DE':
        sum_values = PatraJari.objects.filter(
            created_by__office = request.user.office
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
    if request.user.role == 'DE':
        sum_values = PatraNabikaran.objects.filter(
            created_by__office = request.user.office
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
    if request.user.role == 'DE':
        sum_values = UdyogSifaris.objects.filter(
            created_by__office = request.user.office
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
    if request.user.role == 'DE':
        sum_values = UjuriGunaso.objects.filter(
            created_by__office = request.user.office
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
    if request.user.role == 'DE':
        sum_values = DetailRbpa.objects.filter(
            created_by__office = request.user.office
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