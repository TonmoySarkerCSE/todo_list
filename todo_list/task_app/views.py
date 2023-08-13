from django.shortcuts import redirect, render
from .models import TaskModel
from .forms import AddTaskForm, EditTaskForm

# Create your views here.
def home(request):
    tasks = TaskModel.objects.all()
    return render(request, "task_app/home.html", {'tasks': tasks})

def add_task(request):
    if request.method == "POST":
        form = AddTaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show-tasks")
    else:
        form = AddTaskForm()
    return render(request, "task_app/add_task.html", {"form": form})

def show_tasks(request):
    tasks = TaskModel.objects.all()
    return render(request, "task_app/show_tasks.html", {"tasks": tasks})

def show_task_details(request, id):
    task = TaskModel.objects.get(pk=id)
    return render(request, "task_app/task_details.html", {"task": task})

def edit_task(request, id):
    task = TaskModel.objects.get(pk=id)

    if request.method == "POST":
        form = EditTaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.is_completed = form.cleaned_data["is_completed"]
            task.save()
            return redirect("show-tasks")
    else:
        form = EditTaskForm(instance=task)

    return render(request, "task_app/edit.html", {"form": form})

def completed_tasks(request):
    completed_tasks = TaskModel.objects.filter(is_completed=True)
    return render(
        request, "task_app/completed_task.html", {"completed_tasks": completed_tasks}
    )

def complete_task(request, id):
    task = TaskModel.objects.get(pk=id)
    if not task.is_completed:
        task.is_completed = True
        task.save()
    return redirect("completed-tasks")

def mark_as_pending(request, id):
    task = TaskModel.objects.get(pk=id)

    if task.is_completed:
        task.is_completed = False
        task.save()
    return redirect("show-tasks")

def delete_task(request, id):
    task = TaskModel.objects.get(pk=id)
    if request.method == "POST":
        task.delete()
        return redirect("show-tasks")

    return render(request, "task_app/confirmation.html", {"task": task})
