from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('OK')


def handler400(request):
    return render(request, 'website/errors/400.html', {}, status=400)


def handler403(request):
    return render(request, 'website/errors/403.html', {}, status=403)


def handler404(request):
    return render(request, 'website/errors/404.html', {}, status=404)


def handler500(request):
    return render(request, 'website/errors/500.html', {}, status=500)
