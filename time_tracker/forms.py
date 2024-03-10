from django import forms

from time_tracker.models import Task


class TaskForm(forms.ModelForm):

    name = forms.CharField(
        label='Название задачи',
        widget=forms.TextInput(attrs={'class': 'form-input'})
    )

    class Meta:
        model = Task
        fields = ['name']
