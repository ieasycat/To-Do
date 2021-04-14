from todo.models import ToDo


def add_edit(form):
    cd = form.cleaned_data
    name = cd.get('name')
    priority = cd.get('priority')

    return name, priority


def up_down(todo_up, todo_down):
    if todo_up and todo_down:
        todo_up.position -= 1
        todo_down.position += 1
        todo_up.save()
        todo_down.save()
    todos_order = ToDo.objects.order_by('position')
    context = {
        'todos': todos_order
    }
    return context
