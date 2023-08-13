from django import forms

from .models import TaskModel

class AddTaskForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = ['task_title', 'task_description']

        widgets = {
            'task_title': forms.TextInput(attrs={'placeholder': 'Task Title'}),
            'task_description': forms.Textarea(attrs={'placeholder': 'Task Description'}),
        }

class EditTaskForm(AddTaskForm):
    is_completed = forms.BooleanField(label="Is Completed", required=False)

    class Meta:
        model = TaskModel
        fields = ['task_title', 'task_description', 'is_completed']



