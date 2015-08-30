
from django.contrib import admin

from .models import Ticket, Project, ProjectComponent, ProjectMilestone, UserProject, Notification

admin.site.register(Ticket)
admin.site.register(Project)
admin.site.register(UserProject)
admin.site.register(ProjectComponent)
admin.site.register(ProjectMilestone)
admin.site.register(Notification)



