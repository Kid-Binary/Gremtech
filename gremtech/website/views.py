from django.core.exceptions import PermissionDenied
from django.http import JsonResponse, HttpResponse
from django.shortcuts import (
    render, get_object_or_404, get_list_or_404
)
from django.utils.translation import ugettext as _
from django.utils.decorators import decorator_from_middleware

from gremtech.middleware.browser_checker import BrowserCheckerMiddleware

from .models import (
    Intro, WeAre, WhatWeDo, GetInTouch, WorkWithUs,
    Service, Employee, Project, Contact,
)
from .forms import InvestmentForm, FeedbackForm
from .services.form_helpers import get_form_errors


@decorator_from_middleware(BrowserCheckerMiddleware)
def index(request):
    """
    Index
    """
    content = [
        Intro.objects.first(),
        WeAre.objects.prefetch_related('number_set').first(),
        WhatWeDo.objects.first(),
        GetInTouch.objects.first(),
    ]
    content_blocks = {
        block.get_template_block_name(): block
        for block in content
    }

    services = get_list_or_404(Service)
    projects = get_list_or_404(
        Project.objects.prefetch_related('stage')
    )
    employees = get_list_or_404(
        Employee.objects.prefetch_related('number_set')
    )
    contact = get_list_or_404(Contact)[0]

    return render(request, 'website/index.html', {
        'content_blocks': content_blocks,
        'projects': projects,
        'services': services,
        'employees': employees,
        'contact': contact,
    })


@decorator_from_middleware(BrowserCheckerMiddleware)
def project(request, id):
    """
    Project
    """
    content = [
        WorkWithUs.objects.first()
    ]
    content_blocks = {
        block.get_template_block_name(): block
        for block in content
    }

    project = get_object_or_404(
        Project.objects.prefetch_related(
            'stage', 'functionality_set', 'scope_set'
        ),
        pk=id,
    )
    projects = get_list_or_404(Project)
    contact = get_list_or_404(Contact)[0]

    return render(request, 'website/project.html', {
        'content_blocks': content_blocks,
        'project': project,
        'projects': projects,
        'contact': contact,
    })


@decorator_from_middleware(BrowserCheckerMiddleware)
def investment(request):
    """
    Investment
    """
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
    """
    Feedback
    """
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
