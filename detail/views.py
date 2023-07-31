from django.shortcuts import render, redirect
from account.models import CustomUser
from main.models import (DetailAnugaman, DetailGunaso, DetailHotel, DetailMudha, DetailRegistration, 
                        DetailRenew, DetailUdyog)
from .forms import SiteSettingsModelForm
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from detail.models import SiteSettings
from datetime import datetime


def site_settings(request):
    """for setting open and close dates of forms submission"""
    
    try:
        obj = SiteSettings.objects.order_by('-id').first()
        open_date = obj.open_date
        close_date = obj.close_date
    except ObjectDoesNotExist:
        # Handle the case where obj does not exists
        obj = None
    except AttributeError:
        # Handle the case where obj exists, but open_date or close_date is not available
        open_date = None
        close_date = None
    
    current_date = datetime.now().date()
    
    if request.method == 'POST':
        form = SiteSettingsModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Dates Added")
            return redirect('settings')
        else:
            messages.error(request, 'Please add valid date and time!')
    else:
        form = SiteSettingsModelForm()
    context = {'form': form, 'open_date': open_date, 'close_date': close_date, 'current_date': current_date}
    return render(request, 'settings.html', context)


def detail_hotel_report(request):
    user_office = CustomUser.objects.filter(office=request.user.office)
    if request.user.role == 'A':
        data = DetailHotel.objects.filter(is_verified=True)
    elif request.user.role == 'V':
        data = DetailHotel.objects.all()
    else:
        data = DetailHotel.objects.filter(created_by__in=user_office)
    context = {'data': data}
    return render(request, 'report/details/hotel.html', context)


def detail_anugaman_report(request):
    user_office = CustomUser.objects.filter(office=request.user.office)
    if request.user.role == 'A':
        data = DetailAnugaman.objects.filter(is_verified=True)
    elif request.user.role == 'V':
        data = DetailAnugaman.objects.all()
    else:
        data = DetailAnugaman.objects.filter(created_by__in=user_office)
    context = {'data': data}
    return render(request, 'report/details/anugaman.html', context)


def detail_gunaso_report(request):
    user_office = CustomUser.objects.filter(office=request.user.office)
    if request.user.role == 'A':
        data = DetailGunaso.objects.filter(is_verified=True)
    elif request.user.role == 'V':
        data = DetailGunaso.objects.all()
    else:
        data = DetailGunaso.objects.filter(created_by__in=user_office)
    context = {'data': data}
    return render(request, 'report/details/gunaso.html', context)


def detail_mudha_report(request):
    user_office = CustomUser.objects.filter(office=request.user.office)
    if request.user.role == 'A':
        data = DetailMudha.objects.filter(is_verified=True)
    elif request.user.role == 'V':
        data = DetailMudha.objects.all()
    else:
        data = DetailMudha.objects.filter(created_by__in=user_office)
    context = {'data': data}
    return render(request, 'report/details/mudha.html', context)


def detail_registration_report(request):
    user_office = CustomUser.objects.filter(office=request.user.office)
    if request.user.role == 'A':
        data = DetailRegistration.objects.filter(is_verified=True)
    elif request.user.role == 'V':
        data = DetailRegistration.objects.all()
    else:
        data = DetailRegistration.objects.filter(created_by__in=user_office)
    context = {'data': data}
    return render(request, 'report/details/registration.html', context)


def detail_renew_report(request):
    user_office = CustomUser.objects.filter(office=request.user.office)
    if request.user.role == 'A':
        data = DetailRenew.objects.filter(is_verified=True)
    elif request.user.role == 'V':
        data = DetailRenew.objects.all()
    else:
        data = DetailRenew.objects.filter(created_by__in=user_office)
    context = {'data': data}
    return render(request, 'report/details/renew.html', context)


def detail_udyog_report(request):
    user_office = CustomUser.objects.filter(office=request.user.office)
    if request.user.role == 'A':
        data = DetailUdyog.objects.filter(is_verified=True)
    elif request.user.role == 'V':
        data = DetailUdyog.objects.all()
    else:
        data = DetailUdyog.objects.filter(created_by__in=user_office)
    context = {'data': data}
    return render(request, 'report/details/udyog.html', context)
