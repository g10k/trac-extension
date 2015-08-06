# -*- encoding: utf-8 -*-
from django.http import HttpResponse
from django.core import serializers
import json

from djtrac.models import Ticket

def keywords(request):
    """Ключевые слова в json формате"""

    if request.is_ajax:
        keyword = request.GET.get('term')
        keywords_db = list(Ticket.objects.filter(keywords__icontains=keyword).values_list('keywords', flat=True).distinct())
        #Некоторые keywords из БД нужно распарсить:  'blog, django'
        result_keywords = []
        for kw in keywords_db:
            result_keywords += kw.split(',')

        return HttpResponse(content=json.dumps(result_keywords), content_type='application/json')


# def json_org(request):
#     """Возвращаем mobil организации по имени org  в GET запросе """
#     if request.is_ajax:
#         org_name = request.GET.get('org')
#         orgs = mobil_models.Organization.objects.filter(name=org_name)
#     return HttpResponse(content=serializers.serialize('json', orgs), content_type='application/json')