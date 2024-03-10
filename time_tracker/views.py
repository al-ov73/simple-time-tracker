import json
from django.core import serializers
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import CreateView

from time_tracker.forms import TaskForm
from time_tracker.models import Task


class TaskView(CreateView):

    def get(self, request, *args, **kwargs):
        # tasks = Task.objects.all()
        tasks = serializers.serialize("json", Task.objects.all())
        form = TaskForm()
        return render(
            request,
            'index.html',
            {'form': form, 'tasks': tasks,}
        )

    def post(self, request, *args, **kwargs):
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        messages.add_message(
            request,
            messages.SUCCESS,
            'Введите корректное название задачи'
        )
        return render(
            request,
            'index.html',
            {'form': form}
        )
