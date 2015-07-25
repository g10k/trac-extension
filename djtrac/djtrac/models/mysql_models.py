# -*- encoding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models


class PermissionReport(models.Model):
    user = models.ForeignKey(User)
    component = models.ForeignKey('ComponentInMysql', verbose_name=u"Компонент")

    def __unicode__(self):
        return u"%s: %s" % (self.user, self.component)

    class Meta:
        verbose_name = u"Право на компонент"
        verbose_name_plural = u"Права на компоненты"


class ComponentInMysql(models.Model):
    """Компоненты хранящиеся в mysql
    Данные должны соответствовать sqlite_models.Component
    """
    name = models.TextField(blank=True)
    owner = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return u"%s" % (self.name,)