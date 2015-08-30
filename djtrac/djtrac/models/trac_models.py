# -*- encoding: utf-8 -*-
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


# class Attachment(models.Model):
#     type = models.TextField(blank=True, null=True)
#     id = models.TextField(blank=True, primary_key=True)
#     filename = models.TextField(blank=True, null=True)
#     size = models.IntegerField(blank=True, null=True)
#     time = models.IntegerField(blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     author = models.TextField(blank=True, null=True)
#     ipnr = models.TextField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'attachment'
#         unique_together = (('type', 'id', 'filename'),)

#
# class AuthCookie(models.Model):
#     cookie = models.TextField(blank=True, null=True)
#     name = models.TextField(blank=True, null=True)
#     ipnr = models.TextField(blank=True, null=True)
#     time = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_cookie'
#         unique_together = (('cookie', 'ipnr', 'name'),)
#
#
# class Cache(models.Model):
#     id = models.IntegerField(primary_key=True, blank=True)  # AutoField?
#     generation = models.IntegerField(blank=True, null=True)
#     key = models.TextField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'cache'
#

class Component(models.Model):
    name = models.TextField(blank=True, primary_key=True)
    owner = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'component'

    def __unicode__(self):
        return u"%s, %s" % (self.name, self.owner)

#
#
# class DjangoMigrations(models.Model):
#     id = models.IntegerField(primary_key=True)  # AutoField?
#     app = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     applied = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'django_migrations'
#
#
# class Enum(models.Model):
#     type = models.TextField(blank=True, null=True)
#     name = models.TextField(blank=True, null=True)
#     value = models.TextField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'enum'
#         unique_together = (('type', 'name'),)
#
#
class Milestone(models.Model):
    name = models.TextField(primary_key=True, blank=True)
    due = models.IntegerField(blank=True, null=True)
    completed = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'milestone'

    def __unicode__(self):
        return "%s due: %s; completed: %s " % (self.name, self.due, self.completed)

#
# class NodeChange(models.Model):
#     repos = models.IntegerField(blank=True, null=True)
#     rev = models.TextField(blank=True, null=True)
#     path = models.TextField(blank=True, null=True)
#     node_type = models.TextField(blank=True, null=True)
#     change_type = models.TextField(blank=True, null=True)
#     base_path = models.TextField(blank=True, null=True)
#     base_rev = models.TextField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'node_change'
#         unique_together = (('repos', 'rev', 'path', 'change_type'),)
#
#
# class Permission(models.Model):
#     username = models.TextField(blank=True, null=True)
#     action = models.TextField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'permission'
#         unique_together = (('username', 'action'),)
#
#
# class Report(models.Model):
#     id = models.IntegerField(blank=True, primary_key=True)  # AutoField?
#     author = models.TextField(blank=True, null=True)
#     title = models.TextField(blank=True, null=True)
#     query = models.TextField(blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'report'
#
#
# class Repository(models.Model):
#     id = models.IntegerField(blank=True, primary_key=True)
#     name = models.TextField(blank=True, null=True)
#     value = models.TextField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'repository'
#         unique_together = (('id', 'name'),)
#
#
# class Revision(models.Model):
#     repos = models.IntegerField(blank=True, null=True)
#     rev = models.TextField(blank=True, null=True)
#     time = models.IntegerField(blank=True, null=True)
#     author = models.TextField(blank=True, null=True)
#     message = models.TextField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'revision'
#         unique_together = (('repos', 'rev'),)
#
#
# class Session(models.Model):
#     sid = models.TextField(blank=True, null=True)
#     authenticated = models.IntegerField(blank=True, null=True)
#     last_visit = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'session'
#         unique_together = (('sid', 'authenticated'),)
#
#
# class SessionAttribute(models.Model):
#     sid = models.TextField(blank=True, null=True)
#     authenticated = models.IntegerField(blank=True, null=True)
#     name = models.TextField(blank=True, null=True)
#     value = models.TextField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'session_attribute'
#         unique_together = (('sid', 'authenticated', 'name'),)
#
#
# class System(models.Model):
#     name = models.TextField(primary_key=True, blank=True)
#     value = models.TextField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'system'


class TicketsManager(models.Manager):
    def get_allowed(self, user):
        projects = user.allowed_projects.all()
        components = set()
        for project in projects:
            components.update(project.allowed_components.values_list('component_name', flat=True))
        return self.filter(component__in=components)


class Ticket(models.Model):
    id = models.IntegerField(primary_key=True, blank=True)  # AutoField?
    type = models.TextField(blank=True, null=True)
    # Измеряется как timestamp в микросекундах, для перевода в datetime использовать datetime.datetime.fromtimestamp(t*0.000001)
    time = models.IntegerField(blank=True, null=True)
    changetime = models.IntegerField(verbose_name=u"Время последнего изменения", blank=True, null=True,)
    component = models.TextField(blank=True, null=True)
    severity = models.TextField(blank=True, null=True)
    priority = models.TextField(blank=True, null=True)
    owner = models.TextField(blank=True, null=True)
    reporter = models.TextField(blank=True, null=True)
    cc = models.TextField(blank=True, null=True)
    version = models.TextField(blank=True, null=True)
    milestone = models.TextField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)
    resolution = models.TextField(blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    keywords = models.TextField(blank=True, null=True)
    objects = TicketsManager()

    def __unicode__(self):
        return "%s" % self.summary

    class Meta:
        managed = False
        db_table = 'ticket'


# class TicketChange(models.Model):
#     """ Нам нужны изменения:
#             field       oldvalue    newvalue
#             ____________________________
#             status      new         assigned  - создали тикет
#             owner       NULL        telminov  - Установили владельца
#             owner       telminov    g10k      - Сменили владельца
#             milestone   2015-08     2015-09   - Сменили milestone
#
#     """
#
#
#     ticket = models.IntegerField(blank=True, null=True)
#     time = models.IntegerField(blank=True, primary_key=True)
#     author = models.TextField(blank=True, null=True)
#     field = models.TextField(blank=True, null=True)
#     oldvalue = models.TextField(blank=True, null=True)
#     newvalue = models.TextField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'ticket_change'
#         unique_together = (('ticket', 'time', 'field'),)
#
#     def __unicode__(self):
#         return "%s" % self.ticket


# class TicketCustom(models.Model):
#     ticket = models.IntegerField(blank=True, null=True)
#     name = models.TextField(blank=True, null=True)
#     value = models.TextField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'ticket_custom'
#         unique_together = (('ticket', 'name'),)
#
#
# class Version(models.Model):
#     name = models.TextField(primary_key=True, blank=True)
#     time = models.IntegerField(blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'version'
#
#
# class Wiki(models.Model):
#     name = models.TextField(blank=True, null=True)
#     version = models.IntegerField(blank=True, null=True)
#     time = models.IntegerField(blank=True, null=True)
#     author = models.TextField(blank=True, null=True)
#     ipnr = models.TextField(blank=True, null=True)
#     text = models.TextField(blank=True, null=True)
#     comment = models.TextField(blank=True, null=True)
#     readonly = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'wiki'
#         unique_together = (('name', 'version'),)
#
#
