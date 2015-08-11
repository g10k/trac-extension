# -*- encoding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext, ugettext_lazy as _


from djtrac.models import Milestone, Ticket
from djtrac.datatools import components_for_user,milestones_for_user
EMPTY_CHOICE = ('', '-----')


class DatePicker(forms.TextInput):
    class Media:
        css = {'all':('datetimepicker-master/jquery.datetimepicker.css',)}
        js = ('datetimepicker-master/jquery.datetimepicker.js',)

class AutoComplete(forms.TextInput):
    class Media:
        css = {'all':('css/jquery-ui.min.css',)}
        js = ('js/jquery-ui.min.js',)

class ReportForm(forms.Form):
    component = forms.ChoiceField(
        label=u"Направление",
        choices=list(Ticket.objects.values_list('component', 'component').distinct()),
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=False
    )
    milestone = forms.ChoiceField(
        label=u"Этап",
        choices=[EMPTY_CHOICE] + list(Milestone.objects.values_list('name', 'name')),
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
        widget=AutoComplete(attrs={'class': 'form-control'}),

    )
    dt_from = forms.DateField(
        label=u"Время работы. С",
        required=False,
        widget=DatePicker(attrs={'class': 'form-control'})
    )
    dt_to = forms.DateField(
        label=u"Время работы. По",
        widget=DatePicker(attrs={'class': 'form-control'}),
        required=False
    )
    group_by_components = forms.BooleanField(
        label=u"Группировать по направлению",
        # widget=forms.CheckboxInput(attrs={'class': 'form-control'}),
        required=False
    )
    group_by_milestone = forms.BooleanField(
        label=u"Группировать по этапу",
        # widget=forms.CheckboxInput(attrs={'class': 'form-control'}),
        required=False
    )
    show_description = forms.BooleanField(
        label=u"Отображать подробно",
        # widget=forms.CheckboxInput(attrs={'class': 'form-control'}),
        required=False
    )

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        form = super(ReportForm, self).__init__(*args,**kwargs)
        if user == None:
            pass
        else:
            self.fields['component'].choices = list([EMPTY_CHOICE]) + [(component_name, component_name) for component_name in components_for_user(user)]
            self.fields['milestone'].choices = list([EMPTY_CHOICE]) + [(milestone_name, milestone_name) for milestone_name in milestones_for_user(user)]


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        exclude = ()


class CustomAuthenticationForm(AuthenticationForm):
    """
    Переопределяю класс чтобы добавить в input класс form-control
    """
    username = forms.CharField(
        max_length=254,
        widget = forms.TextInput(attrs={'class': 'form-control'})
    )

    password = forms.CharField(
        label=_("Password"),
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )