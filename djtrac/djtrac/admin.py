
from django.contrib import admin

from .models import Attachment, AuthCookie, Cache, Component, DjangoMigrations, Enum, Milestone, NodeChange,\
    Permission, Report, Repository, Revision, Session, SessionAttribute, System, Ticket, TicketChange, TicketCustom,\
    Version, Wiki, Project, ProjectComponent, ProjectMilestone



admin.site.register(Milestone)
admin.site.register(Ticket)
admin.site.register(Component)
admin.site.register(Project)
admin.site.register(ProjectComponent)
admin.site.register(ProjectMilestone)



