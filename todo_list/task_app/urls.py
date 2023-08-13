from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-task/', views.add_task, name='add-task'),
    path('show-tasks/', views.show_tasks, name='show-tasks'),
    path('task/<int:id>', views.show_task_details, name='task'),
    path('edit-task/<int:id>', views.edit_task, name='edit-task'),
    path('completed-tasks/', views.completed_tasks, name='completed-tasks'),
    path('complete-task/<int:id>', views.complete_task, name='complete-task'),
    path('mark-as-pending/<int:id>', views.mark_as_pending, name='mark-as-pending'),
    path('delete-task/<int:id>/', views.delete_task, name='delete-task'),
]