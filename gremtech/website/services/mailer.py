from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings


class MailerMixin():

    _email_from = settings.EMAIL_FROM
    _email_to = settings.EMAIL_TO

    def send_email(self, subject, template, context):
        email_html = render_to_string(template, context)
        email_from = 'GremTech Website <%s>' % self._email_from

        message = EmailMessage(
            subject, email_html, email_from, [self._email_to]
        )

        message.content_subtype = 'html'
        message.send()
