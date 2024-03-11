import json
from django.core import serializers
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.core.serializers.json import DjangoJSONEncoder

from time_tracker.forms import TaskForm
from time_tracker.models import Task

from rest_framework import generics, viewsets

from time_tracker.serializers import TaskSerializer
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

class TaskSerializerView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        tasks = Task.objects.all()
        serialized_tasks = TaskSerializer(tasks, many=True)
        form = TaskForm()
        return Response(
            {'form': form, 'tasks': tasks, 'serialized_tasks': serialized_tasks}
        )    


class TaskView(CreateView):

    def get(self, request, *args, **kwargs):
        tasks = Task.objects.all().values()
        tasks_json = json.dumps(list(tasks), cls=DjangoJSONEncoder)
        form = TaskForm()
        return render(
            request,
            'index.html',
            {'form': form, 'tasks': tasks, 'tasks_json': tasks_json}
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
