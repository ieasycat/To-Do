from django.urls import path
from todo.views import display_main, edit_todo, delete_todo, add_todo, \
    up, reset, down, done_todo

urlpatterns = [
    path('', display_main, name='display_main'),
    path('<int:todo_id>', done_todo, name='done_todo'),
    path('reset/', reset, name='reset'),
    path('up/<int:todo_pos>', up, name='up'),
    path('down/<int:todo_pos>', down, name='down'),
    path('todo_add/', add_todo, name='add_todo'),
    path('todo_edit/<int:todo_id>', edit_todo, name='edit_todo'),
    path('todo_del/<int:todo_id>', delete_todo, name='delete_todo'),
]
