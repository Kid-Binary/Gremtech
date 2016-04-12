from django import forms
from django.contrib import admin

from transmeta import canonical_fieldname

from .models import (
    Number, Stage, Scope, Functionality,
    Intro, WeAre, WhatWeDo, GetInTouch,
    Service, Employee, Project, Contact
)

from gremtech.admin import (
    ForbidAddMixin, ForbidDeleteMixin,
    gremtech_admin_site, DefaultOrderingModelAdmin
)


class ContentBlockMixin(ForbidDeleteMixin, ForbidAddMixin):
    exclude = ('name',)


class NumberInline(ForbidDeleteMixin, admin.StackedInline):
    model = Number
    max_num = 3
    extra = 1
    fields = (
        'quantity',
        'extra',
        'description_ru',
        'description_uk',
        'description_en',
    )


class FunctionalityInline(admin.StackedInline):
    model = Functionality
    extra = 1
    fields = ('title_ru', 'title_uk', 'title_en',)

    def formfield_for_dbfield(self, db_field, **kwargs):
        field = super(FunctionalityInline, self).formfield_for_dbfield(
            db_field, **kwargs
        )
        db_fieldname = canonical_fieldname(db_field)

        if db_fieldname == 'title':
            field.widget = forms.Textarea(attrs={'cols': '80', 'rows': '2'})

        return field


class ScopeInline(admin.StackedInline):
    model = Scope
    extra = 1
    fields = ('title_ru', 'title_uk', 'title_en',)


@admin.register(Intro, site=gremtech_admin_site)
class IntroAdmin(ContentBlockMixin, DefaultOrderingModelAdmin):
    fieldsets = (
        ('Русский', {
            'fields': ('headline_ru', 'title_ru', 'bottomline_ru',)
        }),
        ('Украинский', {
            'classes': ('collapse',),
            'fields': ('headline_uk', 'title_uk', 'bottomline_uk',)
        }),
        ('Английский', {
            'classes': ('collapse',),
            'fields': ('headline_en', 'title_en', 'bottomline_en',)
        }),
    )


@admin.register(WeAre, site=gremtech_admin_site)
class WeAreAdmin(ContentBlockMixin, DefaultOrderingModelAdmin):
    inlines = [
        NumberInline,
    ]
    fieldsets = (
        ('Русский', {
            'fields': ('headline_ru', 'title_ru', 'text_ru',)
        }),
        ('Украинский', {
            'classes': ('collapse',),
            'fields': ('headline_uk', 'title_uk', 'text_uk',)
        }),
        ('Английский', {
            'classes': ('collapse',),
            'fields': ('headline_en', 'title_en', 'text_en',)
        }),
    )


@admin.register(WhatWeDo, site=gremtech_admin_site)
class WhatWeDoAdmin(ContentBlockMixin, DefaultOrderingModelAdmin):
    fieldsets = (
        ('Русский', {
            'fields': ('text_ru',)
        }),
        ('Украинский', {
            'classes': ('collapse',),
            'fields': ('text_uk',)
        }),
        ('Английский', {
            'classes': ('collapse',),
            'fields': ('text_en',)
        }),
    )


@admin.register(GetInTouch, site=gremtech_admin_site)
class GetInTouchAdmin(ContentBlockMixin, DefaultOrderingModelAdmin):
    fieldsets = (
        ('Русский', {
            'fields': ('title_ru', 'text_ru',)
        }),
        ('Украинский', {
            'classes': ('collapse',),
            'fields': ('title_uk', 'text_uk',)
        }),
        ('Английский', {
            'classes': ('collapse',),
            'fields': ('title_en', 'text_en',)
        }),
    )


@admin.register(Service, site=gremtech_admin_site)
class ServiceAdmin(DefaultOrderingModelAdmin):
    fieldsets = (
        ('Русский', {
            'fields': ('action_ru', 'subject_ru',)
        }),
        ('Украинский', {
            'classes': ('collapse',),
            'fields': ('action_uk', 'subject_uk',)
        }),
        ('Английский', {
            'classes': ('collapse',),
            'fields': ('action_en', 'subject_en',)
        }),
    )


@admin.register(Employee, site=gremtech_admin_site)
class EmployeeAdmin(DefaultOrderingModelAdmin):
    inlines = [
        NumberInline,
    ]
    fieldsets = (
        (None, {
            'fields': ('image_thumb', 'photo',)
        }),
        ('Русский', {
            'fields': (
                'position_ru', 'name_ru', 'surname_ru', 'description_ru',
            )
        }),
        ('Украинский', {
            'classes': ('collapse',),
            'fields': (
                'position_uk', 'name_uk', 'surname_uk', 'description_uk',
            )
        }),
        ('Английский', {
            'classes': ('collapse',),
            'fields': (
                'position_en', 'name_en', 'surname_en', 'description_en',
            )
        }),
    )
    readonly_fields = ('image_thumb',)


@admin.register(Stage, site=gremtech_admin_site)
class StageAdmin(DefaultOrderingModelAdmin):
    fields = ('title_ru', 'title_uk', 'title_en',)


@admin.register(Project, site=gremtech_admin_site)
class ProjectAdmin(
    ForbidDeleteMixin, ForbidAddMixin, DefaultOrderingModelAdmin
):
    inlines = [
        FunctionalityInline,
        ScopeInline,
    ]
    fieldsets = (
        (None, {
            'fields': ('stage', 'completion',)
        }),
        ('Русский', {
            'fields': (
                'title_ru',
                'description_short_ru',
                'description_full_ru',
                'additional_ru',
            )
        }),
        ('Украинский', {
            'classes': ('collapse',),
            'fields': (
                'title_uk',
                'description_short_uk',
                'description_full_uk',
                'additional_uk',
            )
        }),
        ('Английский', {
            'classes': ('collapse',),
            'fields': (
                'title_en',
                'description_short_en',
                'description_full_en',
                'additional_en',
            )
        }),
    )

    def formfield_for_dbfield(self, db_field, **kwargs):
        field = super(ProjectAdmin, self).formfield_for_dbfield(
            db_field, **kwargs
        )
        db_fieldname = canonical_fieldname(db_field)

        if db_fieldname == 'description_short':
            field.widget = forms.Textarea(attrs={'cols': '80', 'rows': '5'})

        return field


@admin.register(Contact, site=gremtech_admin_site)
class ContactAdmin(
    ForbidDeleteMixin, ForbidAddMixin, DefaultOrderingModelAdmin
):
    pass
