from django.shortcuts import render, redirect
from todo.business_logic import add_edit, up_down
from todo.models import ToDo, Priority
from todo.forms import ToDoForm

# Create your views here.


def display_main(request):
    todos_order = ToDo.objects.order_by('position')
    context = {
        'todos': todos_order,
         }
    return render(request, 'main_page.html', context)


def reset(request, check_todo=None):
    todos = ToDo.objects.all()
    for i, todo in enumerate(todos):
        if not check_todo:
            todo.position = i
            todo.save()
        else:
            if check_todo == todo:
                todo.position = i
                todo.save()
    return redirect('display_main')


def add_todo(request):
    context = {
        'form': ToDoForm()
    }

    if request.POST:
        form = ToDoForm(request.POST)
        if form.is_valid():
            name, priority = add_edit(form)

            todo = ToDo.objects.create(
                name=name,
                priority=Priority.objects.get(id=priority)
            )

            reset(request, todo)

            return redirect('display_main')

    return render(request, 'todo_edit_add.html', context)


def edit_todo(request, todo_id):
    todo = ToDo.objects.get(id=todo_id)

    context = {
        'form': ToDoForm()
    }

    if request.POST:
        form = ToDoForm(request.POST)

        if form.is_valid():
            name, priority = add_edit(request, form)

            todo.name = name
            todo.priority = Priority.objects.get(id=priority)
            todo.save()

            return redirect('display_main')

    return render(request, 'todo_edit_add.html', context)


def delete_todo(request, todo_id):
    if request.POST:
        todo = ToDo.objects.get(id=todo_id)
        todo.delete()

    return redirect('display_main')


def up(request, todo_pos):
    todo_up = ToDo.objects.filter(position=todo_pos).first()
    todo_down = ToDo.objects.filter(position=todo_pos - 1).first()

    if todo_down:
        context = up_down(todo_up, todo_down)

    else:
        context = up_down(todo_up, todo_down)

    return render(request, 'main_page.html', context)


def down(request, todo_pos):
    todo_down = ToDo.objects.filter(position=todo_pos).first()
    todo_up = ToDo.objects.filter(position=todo_pos + 1).first()

    if todo_up:
        context = up_down(todo_up, todo_down)

    else:
        context = up_down(todo_up, todo_down)

    return render(request, 'main_page.html', context)


def done_todo(request, todo_id):
    todo = ToDo.objects.get(id=todo_id)
    todo.status = 'Done'
    todo.save()
    return redirect('display_main')
