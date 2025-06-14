from django import forms
from django.forms import DateTimeInput

from todo_servise.models import Task, Tag


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
    )
    class Meta:
        model = Task
        fields = "__all__"
        widgets = {
            "ded_line": DateTimeInput(
                attrs={"type": "datetime-local"}
            ),
        }
