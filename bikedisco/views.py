from django.shortcuts import render


def handling_404(request, exception):
    return render(request, 'main/404.html', {})
