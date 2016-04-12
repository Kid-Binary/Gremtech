from django import forms
from django.contrib import admin

from transmeta import canonical_fieldname

from gremtech.admin import (
    gremtech_admin_site, DefaultOrderingModelAdmin
)

from .models import Metadata


# class MetadataForm(forms.ModelForm):
#     description = forms.CharField(widget=forms.Textarea)


@admin.register(Metadata, site=gremtech_admin_site)
class MetadataAdmin(DefaultOrderingModelAdmin):
    # form = MetadataForm
    readonly_fields = ('url_name',)
    fieldsets = (
        (None, {
            'fields': ('url_name', 'robots',)
        }),
        ('Русский', {
            'fields': ('title_ru', 'description_ru',)
        }),
        ('Украинский', {
            'fields': ('title_uk', 'description_uk',)
        }),
        ('Английский', {
            'fields': ('title_en', 'description_en',)
        }),
    )

    def formfield_for_dbfield(self, db_field, **kwargs):
        field = super(MetadataAdmin, self).formfield_for_dbfield(
            db_field, **kwargs
        )
        db_fieldname = canonical_fieldname(db_field)

        if db_fieldname == 'description':
            field.widget = forms.Textarea(attrs={'cols': '80', 'rows': '4'})

        return field
