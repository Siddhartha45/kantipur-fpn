from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import CustomUser, Office
from .forms import CustomUserForm, OfficeForm, UserEditForm
from fpn import commons
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from fpn.email_normalization import normalize_email
from django.contrib.auth.views import PasswordResetView
from fpn.decorators import user_login_check, admin_required, current_user_check
from django.http import JsonResponse


#---------------------------------------------------------AUTHENTICATION PART---------------------------------------------------------------


@user_login_check
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


@admin_required
def user_create(request):
    """for creating new users"""
    
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


@login_required
def user_edit(request, id):
    """for updating users details"""
    
    # data = {
    #     'role': commons.ROLE_CHOICES,
    #     'department': commons.DEPARTMENT_CHOICES,
    #     'office_IE': Office.objects.filter(category='IE'),
    #     'office_DO': Office.objects.filter(category='DO'),
    #     'office_FO': Office.objects.filter(category='FO'),
    # }
    user_object = get_object_or_404(CustomUser, id=id)
    
    if request.user.id != user_object.id and request.user.role != 'A':  #allows users to update their own details only while allowing admin to update other users details too
        messages.error(request, 'Cannot Access!')
        return redirect('user-edit', id=request.user.id)
    
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=user_object)
        
        new_email = request.POST.get("email")
        normalized_email = normalize_email(new_email)
        
        new_username = request.POST.get('username')
        l_new_username = new_username.lower().strip().replace(" ", "")
            
        if CustomUser.objects.exclude(id=user_object.id).filter(username=l_new_username).first():
            messages.info(request, f'User with this username "{l_new_username}" already exists')
            return redirect('user-edit', id=id)
        
        if CustomUser.objects.exclude(id=user_object.id).filter(email=normalized_email).first():
            messages.info(request, f'User with this email "{normalized_email}" already exists')
            return redirect('user-edit', id=id)
        
        if form.is_valid():
            form.save()
            if request.user.role == 'A':
                messages.success(request, "User Details Updated Successfully")
                return redirect('user-list')
            else:
                messages.success(request, "Details Updated Successfully")
                return redirect('user-profile', user_id=request.user.id)
        else:
            messages.error(request, "Please fill the form with correct data")
    else:
        form = UserEditForm(instance=user_object)
    context = {'form': form, 'user_object': user_object}
    return render(request, 'user/useredit.html', context)


@login_required
def password_change(request, id):
    """for changing users password"""
    
    user_object = get_object_or_404(CustomUser, id=id)
    
    if request.user.id != user_object.id:       #cannot let one user change other users password
        messages.error(request, 'Cannot access!')
        return redirect('password-change', id=request.user.id)
    
    if request.method == 'POST':
        current_password = request.POST.get('current_password')
        new_password = request.POST.get('new_password')
        new_password_confirmation = request.POST.get('new_password_confirmation')
        
        if current_password == '' or new_password == '' or new_password_confirmation == '':
            messages.error(request, "Please fill all the fields")
            return redirect('password-change', id=id)
        
        if not user_object.check_password(current_password):
            messages.error(request, "Incorrect Current Password")
            return redirect('password-change', id=id)
            
        if new_password != new_password_confirmation:
            messages.error(request, "New Password and Confirm New Password didn't match")
            return redirect('password-change', id=id)
        
        if current_password == new_password:
            messages.error(request, "New Password should not be same as Current Password!")
            return redirect('password-change', id=id)
        
        user_object.set_password(new_password)
        user_object.save()
        #update_session_auth_hash(request, user_object) #user is not logged out after changing password
        messages.success(request, "Password Changed Successfully! Login with new password")
        return redirect('login')
    
    context = {'user_object': user_object}
    return render(request,'user/changepassword.html', context)


@admin_required
def user_list(request):
    """list of users"""
    
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


@admin_required
def user_delete(request, id):
    """for deleting users"""
    
    user_object = get_object_or_404(CustomUser, id=id)
    user_object.delete()
    messages.info(request, "User Deleted")
    return redirect('user-list')

#---------------------------------------------------------------OFFICE PART----------------------------------------------------------------


@admin_required
def create_office(request):
    """for adding new offices"""
    
    data = {
        'office': commons.OFFICE_CHOICES,
    }
    if request.method == 'POST':
        form = OfficeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'New Office Created')
            return redirect('office-list')
        else:
            messages.error(request, "Please fill all the fields")
    else:
        form = OfficeForm()
    context = {'form': form, 'data': data}
    return render(request, 'office/office.html', context)


@admin_required
def office_list(request):
    """for viewing offices lists"""
    
    offices = Office.objects.all()
    context = {'offices': offices}
    return render(request, 'office/officetable.html', context)


@admin_required
def office_edit(request, id):
    """for editing office details"""
    
    data = {
        'office': commons.OFFICE_CHOICES,
    }
    office_object = get_object_or_404(Office, id=id)
    if request.method == 'POST':
        form = OfficeForm(request.POST, instance=office_object)
        print(form.data)
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


@admin_required
def office_delete(request, id):
    """for deleting office"""
    
    office_object = get_object_or_404(Office, id=id)
    office_object.delete()
    messages.info(request, "Office Deleted")
    return redirect('office-list')


#-----------------------------------------------------FOR RESETING USERS PASSWORD-------------------------------------------------------

#customizing the django default passwordresetview to check if users email exist in database before sending mail
class CustomPasswordResetView(PasswordResetView):
    def form_valid(self, form):
        email = form.cleaned_data['email']
        # Check if the email exists in the database
        if not CustomUser.objects.filter(email=email).exists():
            # Display an error message
            messages.error(self.request, 'Email does not exist.')
            return self.form_invalid(form)
        return super().form_valid(form) 

