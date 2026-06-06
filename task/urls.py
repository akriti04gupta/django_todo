from django.urls import path
from . import views

app_name='task'

urlpatterns = [
    path('', views.task_list,name='task_list'),
    path('add/',views.task_add,name='task_add'),
    path('edit/<int:id>/',views.task_edit,name='task_edit'),
    path('delete/<int:id>/',views.task_delete,name='task_delete'),
    path('priority/',views.task_priority,name='task_priority'),
    path('toggle/<int:id>/',views.task_toggle,name='task_toggle'),
    path('status/',views.task_status,name='task_status')
]