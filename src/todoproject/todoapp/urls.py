from django.urls import path
from . import views
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, TaskListLoginView

urlpatterns = [
    path('', views.TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', views.TaskDetail.as_view(), name='task'),
    path('create-task/', views.TaskCreate.as_view(), name='create-task'),
    path('edit-task/<int:pk>/', views.TaskUpdate.as_view(), name='edit-task'),
    path('delete-task/<int:pk>/', views.TaskDelete.as_view(), name='delete-task'),
    path('login/', views.TaskListLoginView.as_view(), name='login'),
]