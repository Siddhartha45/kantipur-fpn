from django.shortcuts import redirect


def importexport_required(view_func):
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.department_category == 'IE':
            return view_func(request, *args, **kwargs)
        else:
            return redirect('home')
    return wrap