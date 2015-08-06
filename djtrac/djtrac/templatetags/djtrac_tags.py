# -*- encoding: utf-8 -*-
import datetime
from django import template
from django.template import Library, Node, resolve_variable, TemplateSyntaxError
from djtrac.datatools.reports import url_params
register = template.Library()

@register.filter
def to_datetime(t):
    """

    :param t: время в микросекундах
    :return:
    """
    if not t: return "no time"
    return datetime.datetime.fromtimestamp(int(t*0.000001))


class AddParameter(Node):
  """https://djangosnippets.org/snippets/361/"""
  def __init__(self, varname, value):
    self.varname = varname
    self.value = value

  def render(self, context):
    req = resolve_variable('request', context)
    params = req.GET.copy()
    try:
        # Нужно понять, можно ли использовать второй аргумент, как переменную контекста, из которой взять значение
        value = resolve_variable(self.value, context)
    except Exception:
        # Значит используем как значение
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

from trac.test import EnvironmentStub, Mock, MockPerm
from trac.mimeview import Context
from trac.wiki.formatter import HtmlFormatter, LinkFormatter
from trac.web.href import Href

from django.utils.safestring import mark_safe
from django import template
# register = template.Library()

env = EnvironmentStub(enable=['trac.*', 'tracopt.ticket.commit_updater.*'])
req = Mock(href=Href('/'), abs_href=Href('http://www.example.com/'),
           authname='anonymous', perm=MockPerm(), args={})
context = Context.from_request(req, 'wiki')

@register.filter
def tracwiki(s):
    return mark_safe(HtmlFormatter(env, context, s).generate())