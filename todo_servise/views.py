from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from todo_servise.forms import TaskForm
from todo_servise.models import Task, Tag


class TodoListView(LoginRequiredMixin, generic.ListView):
    model = Task
    template_name = "todo_servise/todo_list.html"
    context_object_name = "task_list"


class TaskCreatedView(LoginRequiredMixin, generic.edit.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo_servise:todo-list")


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo_servise:todo-list")


class TaskDeleteView(LoginRequiredMixin, generic.edit.DeleteView):
    model = Task
    success_url = reverse_lazy("todo_servise:todo-list")


@login_required
def switch_done_or_not_done(request, pk):
    task = Task.objects.get(pk=pk)
    if task.done:
        task.done = False
    else:
        task.done = True
    task.save()
    return HttpResponseRedirect(reverse_lazy("todo_servise:todo-list"))


class TagListView(LoginRequiredMixin, generic.ListView):
    model = Tag
    context_object_name = "tag_list"
    template_name = "todo_servise/tag_list.html"


class TagCreatedView(LoginRequiredMixin, generic.edit.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo_servise:tag-list")


class TagUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo_servise:tag-list")


class TagDeleteView(LoginRequiredMixin, generic.edit.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo_servise:tag-list")
