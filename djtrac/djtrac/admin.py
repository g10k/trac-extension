
from django.contrib import admin

from .models import Ticket, Project, ProjectComponent, ProjectMilestone

admin.site.register(Ticket)
admin.site.register(Project)
admin.site.register(ProjectComponent)
admin.site.register(ProjectMilestone)



