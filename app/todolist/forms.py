import re
from todolist.models.statuses import Status
from todolist.models.types import Type
from todolist.models.tasks import Tasks
from django import forms
from django.core.exceptions import ValidationError


def sum_text_validator(string):
    if '@' in string:
        raise ValidationError("You can't use @ in summary!")
    return string

def first_symbol_validator(string):
    if re.match(r'#', string):
        raise ValidationError("You can't use the first symbol # in summary!")
    return string


class TaskForm(forms.ModelForm):
    status = forms.ModelChoiceField(queryset=Status.objects.all())
    type = forms.ModelMultipleChoiceField(
        queryset=Type.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    summary = forms.CharField(validators=[sum_text_validator, first_symbol_validator])

    class Meta:
        model = Tasks
        fields = ('summary', 'description', 'status', 'type')








