from django.shortcuts import render
from account.models import CustomUser
from main.models import (DetailAnugaman, DetailGunaso, DetailHotel, DetailMudha, DetailRegistration, 
                        DetailRenew, DetailUdyog)


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
