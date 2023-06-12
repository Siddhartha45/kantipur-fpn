from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import CustomUser
from .forms import CustomUserForm
from fpn import commons
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash


def user_login(request):
    if request.method == 'POST':
        email_or_username = request.POST['email']
        password = request.POST['password']
        
        """authenticates users with both username or email"""
        user = authenticate(request, email_or_username=email_or_username, password=password)
        if user:
            login(request, user)
            return redirect('namuna')
    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect('login')


def user_create(request):
    data = {
        'role': commons.ROLE_CHOICES,
        'department_category': commons.DEPARTMENT_CHOICES,
    }
    if request.method == "POST":
        form = CustomUserForm(request.POST)
        if form.is_valid():
            user_data = {
                'username': form.cleaned_data.get('username'),
                'name': form.cleaned_data.get('name'),
                'email': form.cleaned_data.get('email'),
                'phone_number': form.cleaned_data.get('phone_number'),
                'role': form.cleaned_data.get('role'),
            }
            password = make_password(request.POST['password'])
            user = CustomUser.objects.create(password=password, **user_data)
            return HttpResponse("user created")
    else:
        form = CustomUserForm()
    context = {
        'form': form,
        'data': data,
    }
    return render(request, 'user/usercreate.html', context)


def user_list(request):
    users = CustomUser.objects.all()
    context = {'users': users}
    return render(request, 'user/userdisplay.html', context)


def user_profile(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    if request.user != user:
        return redirect('home')
    context = {'user': user}
    return render(request, 'user/userprofile.html', context)



