
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User as DjangoUser

from .models import Attachment, AuthCookie, Cache, Component, DjangoMigrations, Enum, Milestone, NodeChange,\
    Permission, Report, Repository, Revision, Session, SessionAttribute, System, Ticket, TicketChange, TicketCustom,\
    Version, Wiki, PermissionReport

class PermissionReportAdmin(admin.ModelAdmin):
    model = PermissionReport
    list_filter = ('user', 'component')


admin.site.register(Milestone)
admin.site.register(Ticket)
admin.site.register(Component)
admin.site.register(PermissionReport, PermissionReportAdmin)




class PermissionReportAdminTabular(admin.TabularInline):
    model = PermissionReport

class CustomUserAdmin(UserAdmin):
    inlines = [
        PermissionReportAdminTabular,
    ]
admin.site.unregister(DjangoUser)
admin.site.register(DjangoUser, CustomUserAdmin)
