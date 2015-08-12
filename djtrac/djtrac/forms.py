# -*- encoding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _


from djtrac.datatools import components_for_user,milestones_for_user
from djtrac.models import ProjectMilestone
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
        choices=[], # переопределяется в __init__ методе
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=False,
    )
    milestone = forms.ChoiceField(
        label=u"Этап",
        choices=[], # переопределяется в __init__ методе
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
        required=False
    )
    group_by_milestone = forms.BooleanField(
        label=u"Группировать по этапу",
        required=False
    )
    show_description = forms.BooleanField(
        label=u"Отображать подробно",
        required=False
    )

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(ReportForm, self).__init__(*args,**kwargs)
        if user:
            self.fields['component'].choices = list([EMPTY_CHOICE]) + [(component_name, component_name) for component_name in components_for_user(user)]
            self.fields['milestone'].choices = list([EMPTY_CHOICE]) + [(milestone_name, milestone_name) for milestone_name in milestones_for_user(user)]
        current_milestone = ProjectMilestone.objects.filter(is_current=True).first()
        self.fields['milestone'].initial = current_milestone.milestone_name if current_milestone else False



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