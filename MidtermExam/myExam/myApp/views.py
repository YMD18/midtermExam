from django.shortcuts import render, redirect
from datetime import date

from . models import Task

# Create your views here.

def viewTask(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks' : tasks})

def addTask(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        due_date = request.POST['due_date']
        status = 'Due Today'
        today = str(date.today())
        if due_date < today:
            status = 'Overdue'
        elif due_date == today:
            status = 'Due Today'
        elif due_date > today:
            status = 'Upcoming'

        newTask = Task(title = title, description = description, due_date = due_date, status = status)
        newTask.save()
        return redirect('/')
    return render(request, 'task_form.html')

def editTask(request, taskID):
    task = Task.objects.get(id=taskID)

    if request.method == 'POST':
        task.title = request.POST['title']
        task.description = request.POST['description']
        task.due_date = request.POST['due_date']
        today = str(date.today())
        if task.due_date < today:
            task.status = 'Overdue'
        elif task.due_date == today:
            task.status = 'Due Today'
        elif task.due_date > today:
            task.status = 'Upcoming'
        task.save()
        return redirect('/')
    return render(request, 'task_edit.html', {'task' : task})

def deleteTask(request, taskID):
    task = Task.objects.get(id=taskID)
    task.delete()
    return redirect('/')

def confirmDelete(request, taskID):
    task = Task.objects.get(id=taskID)
    return render(request, 'task_confirm_delete.html', {'task' : task})