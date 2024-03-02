from django.shortcuts import render
from first_app.forms import TodolistForms
from first_app.models import TodolistModel
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

class store_tasks(CreateView):
    model = TodolistModel
    template_name = 'add_task.html'
    form_class = TodolistForms
    success_url = reverse_lazy('show_task')
    
class ShowTask(ListView):
    model = TodolistModel
    template_name = 'show_task.html'
    context_object_name = 'task'


class EditTask(UpdateView):
    model = TodolistModel
    form_class = TodolistForms
    template_name = 'add_task.html'
    success_url = reverse_lazy('show_task')

class DeleteTask(DeleteView):
    model = TodolistModel
    template_name = 'delete_confirmation.html'
    success_url = reverse_lazy('show_task')

class is_complete(DeleteView):
    model = TodolistModel
    template_name = 'complete_task.html'
    success_url = reverse_lazy('show_task')

# Create your views here.
