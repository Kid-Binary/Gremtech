from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings


class MailerMixin():

    _email_from = settings.EMAIL_FROM
    _email_to = settings.EMAIL_TO

    def send_email(self, subject, template, context):
        html = render_to_string(template, context)

        message = EmailMessage(
            subject, html, self._email_from, [self._email_to]
        )

        message.content_subtype = 'html'
        message.send()
