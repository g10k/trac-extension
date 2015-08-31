# -*- encoding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
import trac_models
# COMPONENT_CHOICES = (trac_models.Component.objects.values_list('name', 'name').distinct())
# MILESTONE_CHOICES = (trac_models.Milestone.objects.values_list('name', 'name').distinct())
COMPONENT_CHOICES = []
MILESTONE_CHOICES = []


class Project(models.Model):
    name = models.TextField(blank=True)
    description = models.TextField(blank=True, null=True)
    user_projects = models.ManyToManyField(User, related_name='allowed_projects', through='UserProject')

    def __unicode__(self):
        return u"%s" % (self.name,)

    class Meta:
        verbose_name = u"Проект"
        verbose_name_plural = u"Проекты"


class UserProject(models.Model):
    user = models.ForeignKey(User, related_name='user_projects')
    project = models.ForeignKey(Project)
    notification = models.BooleanField(u"Оповещать по почте", default=False)

    def __unicode__(self):
        return u"%s: %s" % (self.user, self.project)

    class Meta:
        verbose_name = u"Проект пользователя"
        verbose_name_plural = u"Проекты пользователей"


class UserCurrentMilestoneTicket(models.Model):
    """
    Тикеты по пользвоателям относящиеся к текущему этапу
    """
    user = models.ForeignKey(User, related_name='last_notified_tickets')
    ticket = models.IntegerField(u"Номер тикета, по которому было выслано уведомление")


class UserNotification(models.Model):
    milestone = models.CharField(
        max_length=255, verbose_name=u"Название этапа, которому принадлежал тикет во время отправки.",
        choices=MILESTONE_CHOICES
    )
    ticket = models.IntegerField(u"Номер тикета по которому было оповещение")
    user = models.ForeignKey(User, related_name='notification_history')
    mail_dt = models.DateTimeField(u"Время, когда выслано оповещение (письмо)", auto_now_add=True)

    def __unicode__(self):
        return u"%s %s: %s" % (self.user, self.ticket, self.notificated_milestone)

    class Meta:
        verbose_name = u"Сообщение пользователю"
        verbose_name_plural = u"Сообщения пользователю"



class ProjectComponent(models.Model):
    project = models.ForeignKey(Project, related_name='allowed_components')
    component = models.CharField(max_length=255, verbose_name=u"Название компонента", choices=COMPONENT_CHOICES)

    def __unicode__(self):
        return u"%s: %s" % (self.project, self.component,)

    class Meta:
        verbose_name = u"Компонент в проекте"
        verbose_name_plural = u"Компоненты в проекте"


class ProjectMilestone(models.Model):
    project = models.ForeignKey(Project, related_name='allowed_milestones')
    milestone = models.CharField(max_length=255, verbose_name=u"Название этапа", choices=MILESTONE_CHOICES)
    is_current = models.BooleanField(u"Текущий этап", default=False)

    def __unicode__(self):
        return u"%s: %s" % (self.project, self.mileston,)

    class Meta:
        verbose_name = u"Этап в проекте"
        verbose_name_plural = u"Этапы в проекте"
