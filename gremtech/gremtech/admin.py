from django.contrib import admin
from django.contrib.auth.models import Group, User
from django.contrib.auth.admin import GroupAdmin, UserAdmin


class ForbidDeleteMixin():
    def get_actions(self, request):
        actions = super(ForbidDeleteMixin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    def has_delete_permission(self, request, obj=None):
        return False


class ForbidAddMixin():
    def has_add_permission(self, request):
        return False


class GremtechAdminSite(admin.AdminSite):
    site_title = 'Gremtech'
    site_header = 'Deus Ex Machina'
    index_title = 'Gremtech Administration'

gremtech_admin_site = GremtechAdminSite(name='deus_ex_machina')


class DefaultOrderingModelAdmin(admin.ModelAdmin):
    ordering = ('id',)


@admin.register(Group, site=gremtech_admin_site)
class GroupAdmin(GroupAdmin):
    pass


@admin.register(User, site=gremtech_admin_site)
class UserAdmin(UserAdmin):
    pass
