# -*- encoding: utf-8 -*-

# def
import datetime
import time

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

