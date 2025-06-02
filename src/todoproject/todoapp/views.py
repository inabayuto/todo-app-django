from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Task
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView

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

class TaskUpdate(UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("tasks") # 成功したらtasksにリダイレクト

class TaskDelete(DeleteView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("tasks") # 成功したらtasksにリダイレクト

class TaskListLoginView(LoginView):
    fields = "__all__"
    template_name = "todoapp/login.html"
    
    def get_success_url(self):
        return reverse_lazy("tasks")

