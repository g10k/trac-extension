# -*- encoding: utf-8 -*-
import random
from django.core.management import call_command

from django.core import mail
from django.test import TestCase, Client
from django.contrib.auth.models import User

from djtrac.models import extra_models
from djtrac.models import trac_models
from djtrac.management.commands.check_notifications import get_mailing_info, get_user_tickets, NEW_TICKETS, LEFT_TICKETS
from djtrac.datatools.users import get_user_milestones

MOBIL_MED_PRO = u"Мобил МЕД"
SOFT_WAY_PRO = u"Софт-вей"

MILESTONE_08 = u'МИС ММ 2015-08'
MILESTONE_09 = u'МИС ММ 2015-09'
SW_MILESTONE_TESTING = u'Тестирование'
COMPONENTS = [u"лаба", u"МИС ММ", u"Выезды", u"ПРОФ", u"ЛМК", u"CRM"]
KEYWORDS = [u'Менеджеры', u'Лаборатория', u'Регистратура', u'Отдел качества']
DEVELOPERS = ['g10k', 'telminov', 'dyus']


class TestMain(TestCase):
    _ticket_number = 0

    @classmethod
    def get_ticket_number(self):
        self._ticket_number += 1
        return self._ticket_number

    def setUp(self):

        test_user = User(
            username='test',
            password='123',
            email='test@mail.ru',
        )
        test_user.save()
        self.client = Client()


    @classmethod
    def setUpTestData(self):
        # Сделаем Project Mis_mm  к нему 1 milestone 08 месяца, 2 milestone 09 месяца - текущий. по 20 тикетов в каждом, закрытых и нет.
        # создадим тикет changes.
        # Создадим для тикетов оповещение объекты
        #
        # Пользователи.  leha, telminov,g10k
        g10k = User.objects.create_user('g10k', 'g10k@mail.com', '1')
        telminov = User.objects.create_user('telminov', 'telminov@mail.com', '2')
        leha = User.objects.create_user('leha', 'leha@mail.com', '3')
        self.users = [g10k, telminov, leha]

        mobil_med = extra_models.Project.objects.create(name=MOBIL_MED_PRO,description=u'Проект Мобилмед')
        soft_way = extra_models.Project.objects.create(name=SOFT_WAY_PRO,description=u'Проект Софт Вей')

        extra_models.UserProject.objects.create(user=g10k, project=mobil_med, notification=True)
        extra_models.UserProject.objects.create(user=leha, project=mobil_med, notification=True)
        extra_models.UserProject.objects.create(user=telminov, project=mobil_med, notification=False)

        extra_models.UserProject.objects.create(user=g10k, project=soft_way, notification=True)
        extra_models.UserProject.objects.create(user=telminov, project=soft_way, notification=True)

        extra_models.ProjectMilestone.objects.create(project=mobil_med, milestone_name=MILESTONE_08)
        extra_models.ProjectMilestone.objects.create(project=mobil_med, milestone_name=MILESTONE_09, is_current=True)
        extra_models.ProjectMilestone.objects.create(project=soft_way, milestone_name=SW_MILESTONE_TESTING, is_current=True)

        for component in COMPONENTS:
            extra_models.ProjectComponent.objects.create(project=mobil_med, component_name=component)

        self.projects = [mobil_med, soft_way]
        for project in self.projects:
            milestones = list(project.allowed_milestones.values_list('milestone_name', flat=True))
            for rate, milestone in enumerate(milestones, start=1):
                for i in range(self._ticket_number + 1, self._ticket_number + 21):
                    ticket_number = self.get_ticket_number()
                    self._generate_ticket(milestone, ticket_number)


    @classmethod
    def _generate_ticket(self, milestone, number):
        """
        Создаем тикет и ticketChange
        """

        ticket = trac_models.Ticket.objects.create(
                    id=number,
                    summary=u"Ticket number %s" % number,
                    changetime=number*10,
                    component=random.choice(COMPONENTS),
                    milestone=milestone,
                    owner=random.choice(DEVELOPERS),
                    status='new',
                    keywords=random.choice(KEYWORDS),
                )
        return ticket


    def test_new_tickets_in_not_notificated(self):
        nn = get_mailing_info()
        for user in self.users:
            new_tickets_count = nn[user.username][NEW_TICKETS]
            user_project_tickets = len(get_user_tickets(user, only_notification=True))
            self.assertEqual(
                len(new_tickets_count),
                user_project_tickets
            )

    def test_check_notifications_mailing(self):
        mailing_info = get_mailing_info()
        call_command('check_notifications')
        self.assertEqual(len(mail.outbox), len(mailing_info))
        mailing_info = get_mailing_info()
        for user in self.users:
            self.assertEqual(mailing_info[user.username][NEW_TICKETS], set([]))
            self.assertEqual(mailing_info[user.username][LEFT_TICKETS], set([]))


    def test_new_tickets(self):
        call_command('check_notifications')
        new_tickets_count = random.randint(1, 10)
        for i in range(new_tickets_count):
            self._generate_ticket(MILESTONE_09, self.get_ticket_number())
        mailing_info = get_mailing_info()
        milestone_09_users = [user for user in self.users if user in get_user_milestones(user,only_notification=True)]

        for user in milestone_09_users:
            self.assertEqual(len(mailing_info[user.username].get(NEW_TICKETS)), new_tickets_count)

    def test_left_tickets(self):
        mailing_info = get_mailing_info()
        call_command('check_notifications')
        changed_tickets = {}
        for user in self.users:
            random_ticket = random.choice(list(mailing_info[user.username][NEW_TICKETS]))
            changed_tickets[user.username] = random_ticket
            ticket = trac_models.Ticket.objects.get(id=random_ticket)
            ticket.milestone = MILESTONE_08
            ticket.save()
        mailing_info = get_mailing_info()
        for user in self.users:
            self.assertTrue(mailing_info[user.username][LEFT_TICKETS])

    def test_close_ticket(self):
        pass

    def test_reopen_ticket(self):
        pass


