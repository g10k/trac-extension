
from django.contrib import admin

import models

admin.site.register(models.Ticket)
admin.site.register(models.Project)
admin.site.register(models.UserProject)
admin.site.register(models.ProjectComponent)
admin.site.register(models.ProjectMilestone)
admin.site.register(models.NotificationHistory)
admin.site.register(models.TargetUser)
admin.site.register(models.TargetGroup)
admin.site.register(models.ProjectTestServer)



