# -*- encoding: utf-8 -*-
import datetime

from django import template
register = template.Library()


@register.filter
def to_datetime(t):
    """

    :param t: время в микросекундах
    :return:
    """
    return datetime.datetime.fromtimestamp(int(t*0.000001))