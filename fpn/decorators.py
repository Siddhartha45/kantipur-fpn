from django.shortcuts import redirect


# def all_required(view_func):
#     def wrap(request, *args, **kwargs):
#         if (
#             request.user.is_authenticated and 
#             request.user.department_category == 'IE' or 
#             request.user.department_category == 'DO' or 
#             request.user.department_category == 'FO' or
#             request.user.department_category == 'FFSQRD' or
#             request.user.department_category == 'FTDND' or
#             request.user.department_category == 'NFFRL' or
#             request.user.department_category == 'A'
#             ):
#             return view_func(request, *args, **kwargs)
#         else:
#             return redirect('home')
#     return wrap


def fo_and_do_and_ffsqrd_required(view_func):
    """only allows users with certain department category to access views"""
    def wrap(request, *args, **kwargs):
        if (
            request.user.is_authenticated and 
            request.user.department_category == 'FO' or
            request.user.department_category == 'DO' or
            request.user.department_category == 'FFSQRD' or
            request.user.role == 'A'
            ):
            return view_func(request, *args, **kwargs)
        else:
            return redirect('home')
    return wrap


def fo_and_ffsqrd_required(view_func):
    """only allows users with certain department category to access views"""
    def wrap(request, *args, **kwargs):
        if (
            request.user.is_authenticated and 
            request.user.department_category == 'FO' or
            request.user.department_category == 'FFSQRD' or
            request.user.role == 'A'
            ):
            return view_func(request, *args, **kwargs)
        else:
            return redirect('home')
    return wrap


def fo_and_nffrl_required(view_func):
    """only allows users with certain department category to access views"""
    def wrap(request, *args, **kwargs):
        if (
            request.user.is_authenticated and 
            request.user.department_category == 'FO' or
            request.user.department_category == 'NFFRL' or
            request.user.role == 'A'
            ):
            return view_func(request, *args, **kwargs)
        else:
            return redirect('home')
    return wrap


def ie_required(view_func):
    """only allows users with certain department category to access views"""
    def wrap(request, *args, **kwargs):
        if (
            request.user.is_authenticated and 
            request.user.department_category == 'IE' or
            request.user.role == 'A'
            ):
            return view_func(request, *args, **kwargs)
        else:
            return redirect('home')
    return wrap


def ie_and_fo_required(view_func):
    """only allows users with certain department category to access views"""
    def wrap(request, *args, **kwargs):
        if (
            request.user.is_authenticated and 
            request.user.department_category == 'IE' or
            request.user.department_category == 'FO' or
            request.user.role == 'A'
            ):
            return view_func(request, *args, **kwargs)
        else:
            return redirect('home')
    return wrap


def ie_and_fo_and_do_and_account_required(view_func):
    """only allows users with certain department category to access views"""
    def wrap(request, *args, **kwargs):
        if (
            request.user.is_authenticated and 
            request.user.department_category == 'IE' or
            request.user.department_category == 'FO' or
            request.user.department_category == 'DO' or
            request.user.department_category == 'A' or
            request.user.role == 'A'
            ):
            return view_func(request, *args, **kwargs)
        else:
            return redirect('home')
    return wrap


def user_login_check(view_func):
    """restricts authenticated user from visiting the login page"""
    def wrap(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('home')
    return wrap
