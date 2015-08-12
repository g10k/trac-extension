# -*- encoding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from trac_models import Ticket
COMPONENT_CHOICES = (Ticket.objects.values_list('component', 'component').distinct())
MILESTONE_CHOICES = (Ticket.objects.values_list('milestone', 'milestone').distinct())


class Project(models.Model):
    name = models.TextField(blank=True)
    description = models.TextField(blank=True, null=True)
    users = models.ManyToManyField(User, related_name=u'allowed_projects')

    def __unicode__(self):
        return u"%s" % (self.name,)

    class Meta:
        verbose_name = u"Проект"
        verbose_name_plural = u"Проекты"


class ProjectComponent(models.Model):
    project = models.ForeignKey(Project, related_name='allowed_components')
    component_name = models.CharField(max_length=255, verbose_name=u"Название компонента", choices=COMPONENT_CHOICES)

    def __unicode__(self):
        return u"%s: %s" % (self.project, self.component_name,)

    class Meta:
        verbose_name = u"Компонент в проекте"
        verbose_name_plural = u"Компоненты в проекте"


class ProjectMilestone(models.Model):
    project = models.ForeignKey(Project, related_name='allowed_milestones')
    milestone_name = models.CharField(max_length=255, verbose_name=u"Название этапа", choices=MILESTONE_CHOICES)
    is_current = models.BooleanField(u"Текущий этап", default=False)

    def __unicode__(self):
        return u"%s: %s" % (self.project, self.milestone_name,)

    class Meta:
        verbose_name = u"Этап в проекте"
        verbose_name_plural = u"Этапы в проекте"