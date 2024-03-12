import json
from django.contrib import messages
from django.shortcuts import render, redirect

from django.views import View

from time_tracker.forms import TaskForm
from time_tracker.models import Task
from django.core.serializers.json import DjangoJSONEncoder

class TaskView(View):

    def get(self, request, *args, **kwargs):
        tasks = Task.objects.order_by('id').values()
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
class TaskStatus(View):

    def get(self, request, *args, **kwargs):
        task_id = kwargs.get('pk')
        task = Task.objects.get(id=task_id)
        print(task.status)
        task.status = 'done'
        task.save()
        return redirect('index')
