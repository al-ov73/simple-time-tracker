from django import forms

from time_tracker.models import Task


class TaskForm(forms.ModelForm):

    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control bg-secondary text-white border-0',
            }
        )
    )

    class Meta:
        model = Task
        fields = ['name']
