from django import forms
from django.utils.translation import ugettext_lazy as _

from .services.mailer import MailerMixin
from .models import Project


class InvestmentForm(MailerMixin, forms.Form):

    project = forms.ModelChoiceField(
        queryset=Project.objects.all(),
        empty_label=_(''),
        widget=forms.RadioSelect,
    )
    name = forms.CharField(
        min_length=2, max_length=250,
    )
    email = forms.EmailField(max_length=254,)
    phone = forms.CharField(
        max_length=19, required=False,
    )
    comment = forms.CharField(
        min_length=5, max_length=500, required=False, widget=forms.Textarea,
    )

    def __init__(self, *args, **kwargs):
        super(InvestmentForm, self).__init__(*args, **kwargs)

        # Project
        self.fields['project'].label = _('Проект')
        self.fields['project'].widget.attrs = {
            'data-rule-required': 'true',
            'data-msg-required': _('Пожалуйста, выберите проект'),
        }
        self.fields['project'].error_messages = {
            'required': _('Пожалуйста, выберите проект'),
            'invalid_choice': _('У нас нет такого проекта'),
        }

        # Name
        self.fields['name'].label = _('Имя')
        self.fields['name'].widget.attrs = {
            'placeholder': _(''),
            'data-rule-required': 'true',
            'data-msg-required': _('Пожалуйста, введите имя'),
            'data-rule-minlength': 2,
            'data-msg-minlength': _('Имя слишком короткое'),
            'data-rule-maxlength': 250,
            'data-msg-maxlength': _('Имя слишком длинное'),
        }
        self.fields['name'].error_messages = {
            'required': _('Пожалуйста, введите имя'),
            'min_length': _('Имя слишком короткое'),
            'max_length': _('Имя слишком длинное'),
        }

        # E-mail
        self.fields['email'].label = _('E-mail')
        self.fields['email'].widget.attrs = {
            'placeholder': _(''),
            'data-rule-required': 'true',
            'data-msg-required': _('Пожалуйста, укажите e-mail'),
            'data-rule-email': 'true',
            'data-msg-email': _('Это не похоже на валидный e-mail'),
            'data-rule-maxlength': 254,
            'data-msg-maxlength': _('Этот e-mail слишком длинный'),
        }
        self.fields['email'].error_messages = {
            'required': _('Пожалуйста, укажите e-mail'),
            'invalid': _('Это не похоже на валидный e-mail'),
            'max_length': _('Этот e-mail слишком длинный'),
        }

        # Phone
        self.fields['phone'].label = _('Телефон')
        self.fields['phone'].widget.attrs = {
            'placeholder': _(''),
            'data-rule-maxlength': 19,
            'data-msg-maxlength': _('Этот телефон слишком длинный'),
            'data-mask': '+380 (99) 999-9999',
        }
        self.fields['phone'].error_messages = {
            'max_length': _('Этот телефон слишком длинный'),
        }

        # Comment
        self.fields['comment'].label = _('Комментарий')
        self.fields['comment'].widget.attrs = {
            'placeholder': _(''),
            'data-rule-minlength': 5,
            'data-msg-minlength': _('Этот комментарий слишком короткий'),
            'data-rule-maxlength': 500,
            'data-msg-maxlength': _('Этот комментарий слишком длинный'),
        }
        self.fields['comment'].error_messages = {
            'min_length': _('Этот комментарий слишком короткий'),
            'max_length': _('Этот комментарий слишком длинный'),
        }

    def send_email(self):
        subject = _('')
        template = 'website/emails/investment.html'
        context = {
            'project': self.cleaned_data['project'],
            'name': self.cleaned_data['name'],
            'email': self.cleaned_data['email'],
            'phone': self.cleaned_data['phone'],
            'comment': self.cleaned_data['comment'],
        }

        super(InvestmentForm, self).send_email(subject, template, context)


class FeedbackForm(MailerMixin, forms.Form):

    name = forms.CharField(min_length=2, max_length=250,)
    email = forms.EmailField(max_length=254,)
    phone = forms.CharField(
        max_length=19, required=False,
    )
    message = forms.CharField(
        min_length=5, max_length=500, widget=forms.Textarea,
    )

    def __init__(self, *args, **kwargs):
        super(FeedbackForm, self).__init__(*args, **kwargs)

        # Name
        self.fields['name'].label = _('Имя')
        self.fields['name'].widget.attrs = {
            'placeholder': _(''),
            'data-rule-required': 'true',
            'data-msg-required': _('Пожалуйста, введите имя'),
            'data-rule-minlength': 2,
            'data-msg-minlength': _('Имя слишком короткое'),
            'data-rule-maxlength': 250,
            'data-msg-maxlength': _('Имя слишком длинное'),
        }
        self.fields['name'].error_messages = {
            'required': _('Пожалуйста, введите имя'),
            'min_length': _('Имя слишком короткое'),
            'max_length': _('Имя слишком длинное'),
        }

        # E-mail
        self.fields['email'].label = _('E-mail')
        self.fields['email'].widget.attrs = {
            'placeholder': _(''),
            'data-rule-required': 'true',
            'data-msg-required': _('Пожалуйста, укажите e-mail'),
            'data-rule-email': 'true',
            'data-msg-email': _('Это не похоже на валидный e-mail'),
            'data-rule-maxlength': 254,
            'data-msg-maxlength': _('Этот e-mail слишком длинный'),
        }
        self.fields['email'].error_messages = {
            'required': _('Пожалуйста, укажите e-mail'),
            'invalid': _('Это не похоже на валидный e-mail'),
            'max_length': _('Этот e-mail слишком длинный'),
        }

        # Phone
        self.fields['phone'].label = _('Телефон')
        self.fields['phone'].widget.attrs = {
            'placeholder': _(''),
            'data-rule-maxlength': 19,
            'data-msg-maxlength': _('Этот телефон слишком длинный'),
            'data-mask': '+380 (99) 999-9999',
        }
        self.fields['phone'].error_messages = {
            'max_length': _('Этот телефон слишком длинный'),
        }

        # Message
        self.fields['message'].label = _('Сообщение')
        self.fields['message'].widget.attrs = {
            'placeholder': _(''),
            'data-rule-required': 'true',
            'data-msg-required': _('Пожалуйста, оставьте сообщение'),
            'data-rule-minlength': 5,
            'data-msg-minlength': _('Это сообщение слишком короткое'),
            'data-rule-maxlength': 500,
            'data-msg-maxlength': _('Это сообщение слишком длинное'),
        }
        self.fields['message'].error_messages = {
            'min_length': _('Это сообщение слишком короткое'),
            'max_length': _('Это сообщение слишком длинное'),
        }

    def send_email(self):
        subject = _('')
        template = 'website/emails/feedback.html'
        context = {
            'name': self.cleaned_data['name'],
            'email': self.cleaned_data['email'],
            'phone': self.cleaned_data['phone'],
            'message': self.cleaned_data['message'],
        }

        super(FeedbackForm, self).send_email(subject, template, context)
