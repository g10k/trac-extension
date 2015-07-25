# -*- encoding: utf-8 -*-
from django import forms
from djtrac.models import Milestone


class DatePicker(forms.TextInput):
    class Media:
        css = {'all':('datetimepicker-master/jquery.datetimepicker.css',)}
        js = ('datetimepicker-master/jquery.datetimepicker.js',)


class ReportForm(forms.Form):
    milestone = forms.ChoiceField(
        label=u"Период",
        choices=[('', '-----')] + list(Milestone.objects.values_list('name', 'name')),
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=False
    )
    number = forms.IntegerField(
        label=u"Номер тикета",
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        help_text=u"Если указан номер, то остальные фильтры не действуют"
    )
    keyword = forms.CharField(
        label=u"Ключевое слово",
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    dt_from = forms.DateField(
        label=u"С",
        required=False,
        widget=DatePicker(attrs={'class': 'form-control'})
    )
    dt_to = forms.DateField(
        label=u"По",
        widget=DatePicker(attrs={'class': 'form-control'}),
        required=False
    )
