from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import CustomUser, Office
from .forms import CustomUserForm, OfficeForm
from fpn import commons
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from fpn.email_normalization import normalize_email


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
            return redirect('office-list')
    else:
        form = OfficeForm()
    context = {'form': form, 'data': data}
    return render(request, 'office.html', context)


@login_required
def office_list(request):
    offices = Office.objects.all()
    context = {'offices': offices}
    return render(request, 'officetable.html', context)


def progress_count(request):
    return render(request, 'count.html')


def progress_amount(request):
    return render(request, 'amount.html')






import pandas as pd
from .forms import UploadFileForm

# def import_file(request):
#     if request.method == 'POST':
#         form = UploadFileForm(request.POST)
#         if form.is_valid():
#             file = request.FILES['file']
            
#             # file_path = file#os.path.join(settings.MEDIA_ROOT, 'files', file.name)
#             # with open(file_path, 'wb+') as f:
#             #     for chunk in file.chunks():
#             #         f.write(chunk)
#             #     f.seek(0)
            
#             df = pd.read_excel(file)
            
#             for _, row in df.iterrows():
                
#                 industry_data = {}
                
#                 if 'department_name' in df.columns:
#                     industry_data['name'] = row['industry_name']
#                 if 'industry_reg_no' in df.columns:
#                     industry_data['industry_reg_no'] = row['industry_reg_no']
#                 # if 'reg_date' in df.columns:
#                 #     industry_data['reg_date'] = row['reg_date']
#                 if 'owner_name' in df.columns:
#                     industry_data['owner_name'] = row['owner_name']
#                 if 'address' in df.columns:
#                     industry_data['address'] = row['address']
#                 if 'telephone_number' in df.columns:
#                     industry_data['telephone_number'] = row['telephone_number']
#                 if 'contact_person' in df.columns:
#                     industry_data['contact_person'] = row['contact_person']
#                 if 'mobile_number' in df.columns:
#                     industry_data['mobile_number'] = row['mobile_number']
#                 if 'district' in df.columns:
#                     industry_data['district'] = row['district']
#                 if 'local_body' in df.columns:
#                     industry_data['local_body'] = row['local_body']
#                 if 'latitude' in df.columns:
#                     industry_data['latitude'] = row['latitude']
#                 if 'longitude' in df.columns:
#                     industry_data['longitude'] = row['longitude']
#                 if 'product_description' in df.columns:
#                     industry_data['product_description'] = row['product_description']
                
#                 #for assigning investment
#                 if 'investment' in df.columns:
#                     investment_choice = row['investment']
#                     if investment_choice == "साना" or investment_choice == "साना प्रा.फ.":
#                         investment = "SMALL"
#                     elif investment_choice == "लघु" or investment_choice == "लघु प्रा.फ":
#                         investment = "MINIATURE"
#                     elif investment_choice == "घरेलु" or investment_choice == "घरेलु  प्रा.फ.":
#                         investment = "DOMESTIC"
#                     elif investment_choice == "मझौला":
#                         investment = "MEDIUM"
#                     elif investment_choice == "ठुलो":
#                         investment = "LARGE"
#                     else:
#                         investment = None
#                 else:
#                     investment = None
#                 if investment is not None:
#                     industry_data['investment'] = investment
                
#                 #for assigning product
#                 if 'industry_acc_product' in df.columns:
#                     industry_acc_product_choice = row['industry_acc_product']
#                     if industry_acc_product_choice == "कृषि मूलक" or industry_acc_product_choice == "कृषि":
#                         industry_acc_product = "AF"
#                     elif industry_acc_product_choice == "उत्पादन मूलक" or industry_acc_product_choice == "उत्पादन":
#                         industry_acc_product = "MF"
#                     elif industry_acc_product_choice == "सेवा मूलक" or industry_acc_product_choice == "सेवा":
#                         industry_acc_product = "S"
#                     elif industry_acc_product_choice == "निर्माण":
#                         industry_acc_product = "I"
#                     else:
#                         industry_acc_product = None
#                 else:
#                     industry_acc_product = None
#                 if industry_acc_product is not None:
#                     industry_data['industry_acc_product'] = industry_acc_product
                
#                 #for assigning status   
#                 if 'current_status' in df.columns:
#                     current_status_choice = row['current_status']
#                     if current_status_choice == "सकृय" or current_status_choice == "चालु":
#                         current_status = "A"
#                     elif current_status_choice == "निष्कृय":
#                         current_status = "I"
#                     else:
#                         current_status = None
#                 else:
#                     current_status = None
#                 if current_status is not None:
#                     industry_data['current_status'] = current_status
            
#                 if 'product_service_name' in df.columns:
#                     industry_data['product_service_name'] = row['product_service_name']
                
#                 if 'male' in df.columns:
#                     male_value = row['male'] if pd.notnull(row['male']) else 0
#                     try:
#                         male_value = int(male_value)
#                     except ValueError:
#                         male_value = 0
#                     industry_data['male'] = male_value
#                 total_manpower = 0
#                 if 'female' in df.columns:
#                     female_value = row['female'] if pd.notnull(row['female']) else 0
#                     try:
#                         female_value = int(female_value)
#                     except ValueError:
#                         female_value = 0
#                     industry_data['female'] = female_value
                
#                     total_manpower = female_value + male_value
                    
#                 if 'yearly_capacity' in df.columns:
#                     yearly_capacity_value = row['yearly_capacity'] if pd.notnull(row['yearly_capacity']) else 0
#                     yearly_capacity_value = str(yearly_capacity_value).replace(',', '')  # Remove commas from the number
#                     try:
#                         industry_data['yearly_capacity'] = float(yearly_capacity_value)
#                     except ValueError:
#                         industry_data['yearly_capacity'] = 0
                
#                 if 'fixed_capital' in df.columns:
#                     fixed_capital_value = row['fixed_capital'] if pd.notnull(row['fixed_capital']) else 0
#                     fixed_capital_value = str(fixed_capital_value).replace(',', '')  # Remove commas from the number
#                     try:
#                         industry_data['fixed_capital'] = float(fixed_capital_value)
#                     except ValueError:
#                         industry_data['fixed_capital'] = 0
                
#                 if 'current_capital' in df.columns:
#                     current_capital_value = row['current_capital'] if pd.notnull(row['current_capital']) else 0
#                     current_capital_value = str(current_capital_value).replace(',', '')  # Remove commas from the number
#                     try:
#                         industry_data['current_capital'] = float(current_capital_value)   
#                     except ValueError:
#                         industry_data['current_capital'] = 0
                    
#                 if 'total_capital' in df.columns:
#                     total_capital_value = row['total_capital'] if pd.notnull(row['total_capital']) else 0
#                     total_capital_value = str(total_capital_value).replace(',', '')  # Remove commas from the number
#                     try:
#                         industry_data['total_capital'] = float(total_capital_value)
#                     except ValueError:
#                         industry_data['total_capital'] = 0
                
#                 industry = Industry(**industry_data)
#                 if hasattr(industry, 'total_manpower'):
#                     industry.total_manpower = total_manpower
                
#                 industry.save() 
#             messages.success(request, "The excel data is saved to database.")
#     else:
#         form = UploadFileForm()
            
#     return render(request, 'report/fileupload.html', {'form': form})