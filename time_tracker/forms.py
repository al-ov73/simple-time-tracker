from django import forms

from time_tracker.models import Task


class TaskForm(forms.ModelForm):

    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control bg-dark text-white',
                'placeholder': 'Введите имя'
            }
        )
    )

    class Meta:
        model = Task
        fields = ['name']
