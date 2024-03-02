from django import forms
from first_app.models import TodolistModel

class TodolistForms(forms.ModelForm):
    class Meta:
        model = TodolistModel
        fields = ['title', 'description']
        