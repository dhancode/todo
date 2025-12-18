from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo


def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todo/index.html', {'todos': todos})



def todo_create(request):
    if request.method == 'POST':
        Todo.objects.create(
            subject=request.POST['subject'],
            notes=request.POST['notes']
        )
        return redirect('todo_list')
    return render(request, 'todo/form.html')


def todo_detail(request, id):
    todo_item = get_object_or_404(Todo, id=id)
    return render(request, 'todo/detail.html', {'todo': todo_item})


def todo_update(request, id):
    todo_item = get_object_or_404(Todo, id=id)
    if request.method == 'POST':
        todo_item.subject = request.POST['subject']
        todo_item.notes = request.POST['notes']
        todo_item.save()
        return redirect('todo_list')
    return render(request, 'todo/form.html', {'todo': todo_item})


def todo_delete(request, id):
    todo_item = get_object_or_404(Todo, id=id)
    todo_item.delete()
    return redirect('todo_list')
