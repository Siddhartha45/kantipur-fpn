from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import CustomUser, Office
from .forms import CustomUserForm, OfficeForm, UserEditForm
from fpn import commons
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from fpn.email_normalization import normalize_email


#---------------------------------------------------------AUTHENTICATION PART---------------------------------------------------------------


def user_login(request):
    if request.method == 'POST':
        email_or_username = request.POST['email']
        password = request.POST['password']
        
        #authenticates users with both username or email(in authentication file)
        user = authenticate(request, email_or_username=email_or_username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Please enter correct credentials')
    return render(request, 'login.html')


@login_required
def user_logout(request):
    logout(request)
    return redirect('login')


#--------------------------------------------------------------USER PART---------------------------------------------------------


@login_required
def user_create(request):
    data = {
        'role': commons.ROLE_CHOICES,
        'department_category': commons.DEPARTMENT_CHOICES,
        'office_IE': Office.objects.filter(category='IE'),
        'office_DO': Office.objects.filter(category='DO'),
        'office_FO': Office.objects.filter(category='FO'),
    }
    if request.method == "POST":
        form = CustomUserForm(request.POST)
        if form.is_valid():
            
            email = form.cleaned_data.get('email')
            normalized_email = normalize_email(email)
            username = form.cleaned_data.get('username')
            normalized_username = username.lower().strip().replace(" ", "")
            
            user_data = {
                'username': normalized_username,
                'name': form.cleaned_data.get('name'),
                'email': normalized_email,
                'phone_number': form.cleaned_data.get('phone_number'),
                'role': form.cleaned_data.get('role'),
                'department_category': form.cleaned_data.get('department_category'),
                'office_id': form.cleaned_data.get('office'),
            }
            password = make_password(request.POST['password'])
            
            #checks existing same email
            if CustomUser.objects.filter(email=user_data['email']).first():
                messages.info(request, f'User with this email "{user_data["email"]}" already exists')
                return redirect('user-create')
            
            #checks existing same username
            if CustomUser.objects.filter(username=user_data['username']).first():
                messages.info(request, f'User with this username "{user_data["username"]}" already exists')
                return redirect('user-create')
            
            user = CustomUser.objects.create(password=password, **user_data)
            messages.success(request, 'User Created')
            return redirect('user-list')
        else:
            messages.error(request, 'User not created! Please fill the form with correct data!')
    else:
        form = CustomUserForm()
    context = {
        'form': form,
        'data': data,
    }
    return render(request, 'user/usercreate.html', context)


#left to do
def user_edit(request, id):
    data = {
        'role': commons.ROLE_CHOICES,
        'department': commons.DEPARTMENT_CHOICES,
        'office_IE': Office.objects.filter(category='IE'),
        'office_DO': Office.objects.filter(category='DO'),
        'office_FO': Office.objects.filter(category='FO'),
    }
    user_object = get_object_or_404(CustomUser, id=id)
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=user_object)
        if form.is_valid():
            form.save()
            messages.success(request, "User Details Updated Successfully")
            return redirect('user-list')
        else:
            messages.error(request, "Please fill the form with correct data")
    else:
        form = UserEditForm(instance=user_object)
    context = {'form': form, 'user_object': user_object, 'data': data}
    return render(request, 'user/user_edit.html', context)


@login_required
def user_list(request):
    users = CustomUser.objects.all()
    context = {'users': users}
    return render(request, 'user/userdisplay.html', context)


@login_required
def user_profile(request, user_id):
    """for viewing users profile"""
    
    user = get_object_or_404(CustomUser, id=user_id)
    if request.user != user:
        return redirect('home')
    context = {'user': user}
    return render(request, 'user/userprofile.html', context)


def user_delete(request, id):
    user_object = get_object_or_404(CustomUser, id=id)
    user_object.delete()
    messages.info(request, "User Deleted")
    return redirect('user-list')

#---------------------------------------------------------------OFFICE PART----------------------------------------------------------------


@login_required
def create_office(request):
    data = {
        'office': commons.OFFICE_CHOICES,
    }
    if request.method == 'POST':
        form = OfficeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'New Office Created')
            return redirect('office/office-list')
    else:
        form = OfficeForm()
    context = {'form': form, 'data': data}
    return render(request, 'office/office.html', context)


@login_required
def office_list(request):
    offices = Office.objects.all()
    context = {'offices': offices}
    return render(request, 'office/officetable.html', context)


def office_edit(request, id):
    data = {
        'office': commons.OFFICE_CHOICES,
    }
    office_object = get_object_or_404(Office, id=id)
    if request.method == 'POST':
        form = OfficeForm(request.POST, instance=office_object)
        if form.is_valid():
            form.save()
            messages.success(request, "Office Details Updated")
            return redirect('office-list')
        else:
            messages.error(request, "Please fill the correct data")
    else:
        form = OfficeForm(instance=office_object)
    context = {'form': form, 'office_object': office_object, 'data': data}
    return render(request, 'office/office_edit.html', context)


def office_delete(request, id):
    office_object = get_object_or_404(Office, id=id)
    office_object.delete()
    messages.info(request, "Office Deleted")
    return redirect('office-list')


#--------------------------------------------------------------------------------------------------------------------------------------------

def progress_count(request):
    return render(request, 'count.html')


def progress_amount(request):
    return render(request, 'amount.html')


