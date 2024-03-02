from django.contrib import admin
from first_app.models import TodolistModel

class TodolistModelAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'description', 'status')

admin.site.register(TodolistModel, TodolistModelAdmin)

# Register your models here.
