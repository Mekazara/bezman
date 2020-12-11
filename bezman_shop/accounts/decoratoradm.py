from django.shortcuts import redirect

def admin_only(func):
        def wrap(request, *args, **kwargs):
            if request.user.is_staff:
                return func(request, *args, **kwargs)
            else:
                return redirect('products')
        return wrap
