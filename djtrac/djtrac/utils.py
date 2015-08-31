# -*- encoding: utf-8 -*-
import re
import urllib
import datetime
import time

from django.utils.safestring import mark_safe
from django.utils.http import urlquote
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def datetime_from_timestamp(t):
    """

    :param t: время в микросекундах
    :return:
    """
    return datetime.datetime.fromtimestamp(int(t*0.000001))

def timestamp_from_date(date):
    """

    :param date:  дата, которую нужно преобразовать в timestamp в микросекундах
    :return:
    """
    return int(time.mktime(date.timetuple())) * 1000000



def get_page(request, qs, objects_count=20):
    '''
    Функция для пагинации (разбиения списка по страницам).
    qs - query set объектов в списке;
    objects_count - число объектов на странице;
    Возвращается объект класса Page.
    '''

    per_page = request.GET.get('per_page', objects_count)
    if per_page == 'all':
        objects_count = len(qs)
    else:
        objects_count = int(per_page)
    paginator = Paginator(qs, objects_count)              # Количество объектов на странице
    page = request.GET.get('page', 1)                  # Если не передали GET -- показываем page=1

    try:
        return paginator.page(page)
    except PageNotAnInteger:
        # Если передали не целое число -- показываем первую страницу
        return paginator.page(1)
    except EmptyPage:
        # Если запросили страницу с номером около 100500 -- показываем последнюю страницу
        return paginator.page(paginator.num_pages)


def url_params(request, except_params=(), use_urllib=False, as_is=False):
    """
    функция создает строку с GET-параметрами запорса

    Пармметры:
        request -
        except_params -
        use_urllib - по-видимому, временный параметр. современем должен стать True. Эскейпит все специальные url-символы символы
        as_is - не добавляет преобразования символов имеющих особое значение в урлах.
                Может использоваться для формирования ссылок на основе текущей (например для сортировки с доп параметром),
                а не для передачи в качестве параметра в другом get-параметре (типа next)

    пример использвоания.
        во вьюхе:
            url = reverse('prof.views.search.administrator') + url_params(request)
            или
            c['sort_url'] = url_params(request, except_params=('sort',))
        затем в шаблоне:
            <a href="{{ sort_url }}&sort=lab_number">Лабораторный номер</a>
    """
    if not request.GET:
        return ''
    params = []
    for key, value in request.GET.items():
        if key not in except_params:
            for v in request.GET.getlist(key):
                params.append('%s=%s' % (key, urlquote(v)))

    if as_is:
        str_params = '?' + '&'.join(params)
    else:
        if use_urllib:
            str_params = '?' + '&'.join(params)
            str_params = urllib.pathname2url(str_params)
        else:
            str_params = '?' + '%26'.join(params)
    return mark_safe(str_params)

def url_path(request, base_url=None, *args, **kwargs):
    """
        функция формирует полный урл, позволяя исключать некоторые GET-параметры

        пример:

    """
    if not base_url:
        base_url = request.path
    params = url_params(request, *args, **kwargs)
    url = '%s%s' % (base_url, params)
    return url


def prepare_sort_params(params, request, sort_key='sort', revers_sort=None, except_params=None):
    """
        Prepare sort params. Add revers '-' if need.
        Params:
            params - list of sort parameters
            request
            sort_key
            revers_sort - list or set with keys that need reverse default sort direction
            except_params - GET-params that will be ignored
        Example:
            во вьюхе:
                c['sort_params'] = prepare_sort_params(
                    ('order__lab_number', 'order__client__lname', 'organization', 'city', 'street', ),
                    request,
                )
            в шаблоне:
                   <th><a href="{{ sort_params.order__lab_number.url }}">Лабораторный номер</a></th>
                   <th><a href="{{ sort_params.order__client__lname.url }}">ФИО</a></th>
                   <th><a href="{{ sort_params.organization.url }}">Организация</a></th>
                   <th><a href="{{ sort_params.city.url }}">Город</a></th>
                   <th><a href="{{ sort_params.street.url }}">Улица</a></th>

    """
    current_param, current_reversed = sort_key_process(request, sort_key)

    except_params = except_params or []
    except_params.append(sort_key)


    base_url = url_params(request, except_params=except_params, as_is=True)

    sort_params = {}
    revers_sort = revers_sort or set()
    url_connector = '?' if request.get_full_path() == request.path else "&"
    for p in params:
        sort_params[p] = {}
        if current_param and p == current_param:
            prefix = '' if current_reversed else '-'
            sort_params[p]['url'] = base_url + "%s%s=%s" % (url_connector, sort_key, prefix + current_param)
            sort_params[p]['is_reversed'] = current_reversed
            sort_params[p]['is_current'] = True
            arrow = 'down' if sort_params[p]['is_reversed'] else 'up'
            sort_params[p]['icon'] = '<span class="glyphicon glyphicon-arrow-%s"></span>' % (arrow,)

        else:
            default_direction = '-' if p in revers_sort else ''
            sort_params[p]['url'] = base_url + "%s%s=%s%s" % (url_connector, sort_key, default_direction, p)
            sort_params[p]['is_reversed'] = False
            sort_params[p]['is_current'] = False


    return sort_params

def sort_key_process(request, sort_key='sort'):
    """
        process sort-parameter value (for example, "-name")
        return:
            current_param - field for sorting ("name)
            current_reversed - revers flag (True)
    """
    current = request.GET.get(sort_key)
    current_reversed = False
    current_param = None
    if current:
        mo = re.match(r'^(-?)(\w+)$', current)    # exclude first "-" (if exist)
        if mo:
            current_reversed = mo.group(1) == '-'
            current_param = mo.group(2)

    return current_param, current_reversed