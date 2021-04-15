from django.urls import path
from todo.views import display_main, edit_todo, delete_todo, add_todo, up, reset, down, done_todo, filter_priority

urlpatterns = [
    path('', display_main, name='display_main'),
    path('done_todo/<int:todo_id>', done_todo, name='done_todo'),
    path('reset/', reset, name='reset'),
    path('up/<int:todo_pos>', up, name='up'),
    path('down/<int:todo_pos>', down, name='down'),
    path('add_todo', add_todo, name='add_todo'),
    path('edit_todo/<int:todo_id>', edit_todo, name='edit_todo'),
    path('delete_todo/<int:todo_id>', delete_todo, name='delete_todo'),
    path('filter_priority', filter_priority, name='filter_priority'),
]
