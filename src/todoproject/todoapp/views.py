from django.forms.models import BaseModelForm
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Task
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    redirect_field_name = "login"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["tasks"] = context["tasks"].filter(user=self.request.user)
        return context

class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'

class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ["title", "description", "completed"]
    success_url = reverse_lazy('tasks') # 成功したらtasksにリダイレクト

    def form_invalid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
            
class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("tasks") # 成功したらtasksにリダイレクト

class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("tasks") # 成功したらtasksにリダイレクト

class TaskListLoginView(LoginView):
    fields = "__all__"
    template_name = "todoapp/login.html"
    
    def get_success_url(self):
        return reverse_lazy("tasks")

