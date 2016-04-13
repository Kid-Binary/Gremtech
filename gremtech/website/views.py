from django.core.exceptions import PermissionDenied
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.utils.translation import ugettext as _
from django.utils.decorators import decorator_from_middleware

from gremtech.middleware.browser_checker import BrowserCheckerMiddleware

from .services.form_helpers import get_form_errors
from .forms import InvestmentForm, FeedbackForm


@decorator_from_middleware(BrowserCheckerMiddleware)
def index(request):
    return render(request, 'website/index.html')


@decorator_from_middleware(BrowserCheckerMiddleware)
def project(request):
    return render(request, 'website/project.html')


@decorator_from_middleware(BrowserCheckerMiddleware)
def investment(request):
    form = InvestmentForm

    return render(request, 'website/forms/investment.html', {
        'form': form
    })


def investment_send(request):
    # and request.is_ajax():
    if request.method == 'POST':
        form = InvestmentForm(request.POST)

        if form.is_valid():
            # form.send_email()
            response = {
                'data': {'message': _('Valid')},
                'code': 200,
            }
        else:
            errors = get_form_errors(form.errors.items())

            response = {
                'data': {'message': _('Invalid'), 'errors': errors},
                'code': 400,
            }
    else:
        raise PermissionDenied

    return JsonResponse(response['data'], status=response['code'])


@decorator_from_middleware(BrowserCheckerMiddleware)
def feedback(request):
    form = FeedbackForm

    return render(request, 'website/forms/feedback.html', {
        'form': form
    })


def feedback_send(request):
    # and request.is_ajax():
    if request.method == 'POST':
        form = FeedbackForm(request.POST)

        if form.is_valid():
            # form.send_email()
            response = {
                'data': {'message': _('Valid')},
                'code': 200,
            }
        else:
            errors = get_form_errors(form.errors.items())

            response = {
                'data': {'message': _('Invalid'), 'errors': errors},
                'code': 400,
            }
    else:
        raise PermissionDenied

    return JsonResponse(response['data'], status=response['code'])


def old_browser(request):
    return HttpResponse('Fuck')


@decorator_from_middleware(BrowserCheckerMiddleware)
def handler400(request):
    return render(request, 'website/errors/400.html', {}, status=400)


@decorator_from_middleware(BrowserCheckerMiddleware)
def handler403(request):
    return render(request, 'website/errors/403.html', {}, status=403)


@decorator_from_middleware(BrowserCheckerMiddleware)
def handler404(request):
    return render(request, 'website/errors/404.html', {}, status=404)


@decorator_from_middleware(BrowserCheckerMiddleware)
def handler500(request):
    return render(request, 'website/errors/500.html', {}, status=500)
