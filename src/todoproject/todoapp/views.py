from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from .models import Task
from django.urls import reverse_lazy

# Create your views here.
class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'

class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'

class TaskCreate(CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy('tasks') # 成功したらtasksにリダイレクト