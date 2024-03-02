from django.urls import path
from . import views
urlpatterns = [
    path('', views.store_tasks.as_view(), name='add_task' ),
    path('show_task', views.ShowTask.as_view(), name='show_task'),
    path('edit_task/<int:pk>', views.EditTask.as_view(), name='edit_task'),
    path('delete_task/<int:pk>', views.DeleteTask.as_view(), name='delete_task'),
    path('task_complete/<int:pk>', views.is_complete.as_view(), name='task_complete'),
]