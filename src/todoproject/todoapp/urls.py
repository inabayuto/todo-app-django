from django.urls import path
from . import views
from .views import TaskList, TaskDetail

urlpatterns = [
    path('', views.TaskList.as_view()),
    path('task/<int:pk>/', views.TaskDetail.as_view(), name='task')
]