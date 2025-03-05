from django.urls import path
from . import views

urlpatterns = [
    path('', views.viewTask),
    path('task_form/', views.addTask, name='task_form'),  
    path('task_edit/<int:taskID>/', views.editTask, name='task_edit') ,
    path('delete/<int:taskID>/', views.deleteTask, name='task_delete'),
    path('confirmDelete/<int:taskID>/', views.confirmDelete, name='task_confirm_delete'),
]