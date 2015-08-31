# -*- encoding: utf-8 -*-
import datetime
import os
from django import template
from django.template import Node, resolve_variable, TemplateSyntaxError
from django.conf import settings
from djtrac.datatools.reports import url_params
register = template.Library()

@register.filter
def to_datetime(t):
    """

    :param t: время в микросекундах
    :return:
    """
    if t:
        return datetime.datetime.fromtimestamp(int(t*0.000001))


@register.filter
def djtrac_ticket_url(ticket_id):
    return os.path.join(settings.HTTP_PATH_TO_TRAC, "neo/ticket/", str(ticket_id))


class AddParameter(Node):
  """https://djangosnippets.org/snippets/361/"""
  def __init__(self, varname, value):
    self.varname = varname
    self.value = value

  def render(self, context):
    req = resolve_variable('request', context)
    params = req.GET.copy()
    try:
        value = resolve_variable(self.value, context)
    except Exception:
        value = self.value
    params[self.varname] = value
    return '%s?%s' % (req.path, params.urlencode())


def addurlparameter(parser, token):
  from re import split
  bits = split(r'\s+', token.contents, 2)
  if len(bits) < 2:
    raise TemplateSyntaxError, "'%s' tag requires two arguments" % bits[0]
  return AddParameter(bits[1],bits[2])
register.tag('addurlparameter', addurlparameter)


@register.filter
def get_params(request):
    return url_params(request, as_is=True, use_urllib=True, except_params="page")
