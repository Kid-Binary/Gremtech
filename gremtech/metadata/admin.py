from django import forms
from django.contrib import admin

from gremtech.admin import (
    gremtech_admin_site, DefaultOrderingModelAdmin
)

from .models import Metadata


class MetadataForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea)


@admin.register(Metadata, site=gremtech_admin_site)
class MetadataAdmin(DefaultOrderingModelAdmin):
    form = MetadataForm
    readonly_fields = ('url_name',)
