# -*- encoding: utf-8 -*-
import json
from django.http import HttpResponse
from djtrac.models import Ticket
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')
def keywords(request):
    """Ключевые слова в json формате"""

    if request.is_ajax:
        keyword = request.GET.get('term')
        keywords_db = list(Ticket.objects.filter(keywords__icontains=keyword).values_list('keywords', flat=True).distinct())
        # Некоторые keywords из БД нужно распарсить:  'blog, django'
        result_keywords = []
        for kw in keywords_db:
            result_keywords += kw.split(',')
        return HttpResponse(content=json.dumps(result_keywords), content_type='application/json')
