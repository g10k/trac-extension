# -*- coding: utf-8 -*-
import sys

from django.core.management.base import BaseCommand, CommandError
from djtrac.models import Component, Ticket, ComponentInMysql

class Command(BaseCommand):
    help = 'Сверяет наличие направлений (компонент) в ComponentInMySQL'

    def add_arguments(self, parser):
        parser.add_argument('--fake',
            action='store_true',
            dest='fake',
            default=False,
            help=u'Не делать изменений в БД')

    def handle(self, *args, **options):
        fake = options['fake']
        sqlite_components = list(Component.objects.values_list('name', flat=True).distinct())
        from_tickets_components = list(Ticket.objects.values_list('component', flat=True).distinct())
        all_components_name = set(sqlite_components)|set(from_tickets_components)
        if fake:
            not_in_mysql = all_components_name - set(ComponentInMysql.objects.values_list('name', flat=True))
            for name in not_in_mysql:
                sys.stdout.write(name + "\r\n")
        else:
            for component_name in all_components_name:
                component, created = ComponentInMysql.objects.get_or_create(name=component_name)
                if created:
                    component.save()
                    sys.stdout.write(u'Создан: %s\r\n' % component_name)
