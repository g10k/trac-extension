# -*- encoding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
import trac_models
COMPONENT_CHOICES = (trac_models.Component.objects.values_list('name', 'name').distinct())
MILESTONE_CHOICES = (trac_models.Milestone.objects.values_list('name', 'name').distinct())


class Project(models.Model):
    name = models.TextField(blank=True)
    description = models.TextField(blank=True, null=True)
    user_projects = models.ManyToManyField(User, related_name='allowed_projects', through='UserProject')
    target_users = models.ManyToManyField('TargetUser', verbose_name='Пользователи проекта', blank=True)
    target_groups = models.ManyToManyField('TargetGroup', verbose_name='Группы пользователей проекта', blank=True)

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


class NotificationHistory(models.Model):
    notificated_milestone = models.CharField(max_length=255, verbose_name=u"Название этапа, которому принадлежал тикет во время отправки.", choices=MILESTONE_CHOICES)
    ticket = models.IntegerField(u"Номер тикета по которому было оповещение")
    user = models.ForeignKey(User, related_name='notification_history')
    dc = models.DateTimeField(u"Время, когда выслано оповещение(письмо)", auto_now_add=True)

    def __unicode__(self):
        return u"%s %s: %s" % (self.user, self.ticket, self.notificated_milestone)

    class Meta:
        verbose_name = u"История уведомлений (писем)"
        verbose_name_plural = u"История уведомлений (писем)"



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


class TargetUser(models.Model):
    name = models.CharField(max_length=255, verbose_name=u"Имя")
    email = models.EmailField(verbose_name=u"Почта")
    description = models.TextField(verbose_name=u"Описание", help_text=u"Должность и т.п.")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u"Пользователь продукта"
        verbose_name_plural = u"Пользователи продукта"

class TargetGroup(models.Model):
    name = models.CharField(max_length=255, verbose_name=u"Имя")
    users = models.ManyToManyField(TargetUser, verbose_name=u"Пользователи")

    class Meta:
        verbose_name = u"Группа пользователей продукта"
        verbose_name_plural = u"Группы пользователей продукта"

    def __unicode__(self):
        return self.name

    def get_user_emails(self):
        return self.users.values_list('email', flat=True)

class TicketReleaseNote(models.Model):
    ticket = models.IntegerField(verbose_name=u"Тикет")
    description = models.TextField(verbose_name=u"Описание", blank=True)
    target_users = models.ManyToManyField(TargetUser, verbose_name=u"Пользователи",
                                          help_text=u"к кому относятся результаты работы по тикету", blank=True)
    target_groups = models.ManyToManyField(TargetGroup, verbose_name=u"Группы пользователей",
                                           help_text=u"к кому относятся результаты работы по тикету", blank=True)
    mail_dt = models.DateTimeField(verbose_name=u"Время когда уведомление было отправлено пользвоателям", null=True)

    class Meta:
        verbose_name = u"Замечания к выпуску"
        verbose_name_plural = u"Замечания к выпуску"

    def __unicode__(self):
        return '#%s' % self.ticket

    def get_ticket(self):
        import djtrac.models.trac_models
        return djtrac.models.trac_models.Ticket.objects.get(id=self.ticket)

    def get_target_users(self):
        users = set()
        for user in self.target_users.all():
            users.add(user)
        for group in self.target_groups.all():
            users.update(group.users.all())
        return users










