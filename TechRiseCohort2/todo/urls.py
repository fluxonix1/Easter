from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.task_list, name = 'task_list'),
    path('toggle/<int:task_id>/', views.task_list, name = 'toggle_task'),
    path('delete/<int:task_id>/', views.delete_task, name ='delete_task'),
]
