# -*- encoding: utf-8 -*-

from django.test import TestCase, Client, runner
# from django.test
from django.contrib.auth.models import User

from django.core.urlresolvers import reverse
from django.conf import settings

from djtrac.models import Milestone


import pprint

class TestMain(TestCase):

    def setUp(self):

        test_user = User(
            username='test',
            password='123',
            email='test@mail.ru',
        )
        test_user.save()
        print User.objects.all()
        self.client = Client()


    def test_main(self):
        response = self.client.get(reverse('djtrac.views.main.main'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.redirect_chain[0], ('http://testserver/login/?next=/',302))
        self.client.login(username='test', password='123')
        # client.is
        response = self.client.get(reverse('djtrac.views.main.main'),follow=True)
        self.assertEqual(response.status_code, 200)
        print response.redirect_chain[0]

    def test_login(self):
        login_url = reverse('custom_login')
        response = self.client.get(login_url)
        self.assertEqual(response.status_code, 200)
        response = self.client.post(login_url,{'username':'test','password':'123'})
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse('djtrac.views.main.main'))
        self.assertEqual(response.status_code, 200)




