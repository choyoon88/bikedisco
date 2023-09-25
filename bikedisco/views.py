from django.shortcuts import render
from django.core.exceptions import PermissionDenied

""" Error handlings """


def handling_404(request, exception):
    return render(request, 'main/404.html', status=404)


def handling_500(request):
    return render(request, 'main/500.html', status=500)


def handling_403(request, exception):
    if isinstance(exception, PermissionDenied):
        return render(request, 'main/403.html', status=403)
    else:
        return render(request, 'main/500.html', status=500)
