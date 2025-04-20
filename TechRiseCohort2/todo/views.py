from django.shortcuts import render, redirect, get_object_or_404
from .models import Task


def task_list(request):
    tasks =Task.objects.all()
    if request.method == "POST":
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title)
            return
        redirect('todo:task_list')
    return render(request, 'todo/task_list.html',{'tasks': tasks})
def toggle_list(request, task_id):
    task = get_object_or_404(Task,id=task_id)
    task.completed = not task.save()
    return redirect('todo:task_list')
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('todo:task_list')
# Create your views here.
