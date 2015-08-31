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
    send_milestone_changes = models.BooleanField(
        u"Оповещать об изменениях", default=False,
        help_text=u"оповещать об изменения состава текущих этапов по проектам пользователя")

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


class UserNotificationMilestoneChanges(models.Model):
    ACTION_ADD = 'add'
    ACTION_LEFT = 'left'
    ACTION_CHOICES = (
        (ACTION_ADD, ACTION_ADD),
        (ACTION_LEFT, ACTION_LEFT),
    )

    milestone = models.CharField(
        max_length=255, verbose_name=u"Название этапа, которому принадлежал тикет во время отправки.",
        choices=MILESTONE_CHOICES
    )
    ticket = models.IntegerField(u"Номер тикета по которому было оповещение")
    user = models.ForeignKey(User, related_name='notification_history')
    mail_dt = models.DateTimeField(u"Время, когда выслано оповещение (письмо)", auto_now_add=True)
    action = models.CharField(max_length=4, choices=ACTION_CHOICES)

    def __unicode__(self):
        return u"%s %s: %s" % (self.user, self.ticket, self.milestone)

    class Meta:
        verbose_name = u"Сообщение пользователю"
        verbose_name_plural = u"Сообщения пользователю"
        get_latest_by = 'mail_dt'



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


class MilestoneRelease(models.Model):
    milestone = models.CharField(max_length=255, verbose_name=u'Этап', unique=True)
    planned_date = models.DateField(verbose_name=u'Дата релиза', help_text=u'Планируемая дата релиза', null=True, blank=True)
    mail_dt = models.DateTimeField(verbose_name=u"Время рассылки уведомлений", null=True)

class ProjectTestServer(models.Model):
    project = models.ForeignKey(Project, verbose_name=u'Проект')
    name = models.CharField(max_length=255, verbose_name=u"Название", unique=True)
    url = models.URLField(verbose_name=u'http адрес')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u"Тестовый сервер"
        verbose_name_plural = u"Тестовые сервера"

