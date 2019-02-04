
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CategoriaForm, TarefaForm
from .models import Categoria, Tarefa


# Create your views here.
@login_required
def new_category(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.save()
            return redirect('list_category')
        else:
            print(form.errors)
    else:
        form = CategoriaForm()
    return render(request, 'tarefas/new_category.html', {'form': form})

@login_required
def list_category(request):
    categories = Categoria.objects.filter(user=request.user)
    return render(request, 'tarefas/list_categories.html', {'categories': categories})

@login_required
def new_task(request):
    categoria = Categoria.objects.filter(user=request.user)
    if not categoria:
        messages.error(request, 'Você precisa criar uma categoria primeiro!')
        return render(request, 'tarefas/list_categories.html')
    elif request.method == 'POST':
        form = TarefaForm(user=request.user, data=request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.save()
            return redirect('home')
        else:
            form.errors
    else:
        form = TarefaForm(user=request.user)
    return render(request, 'tarefas/new_task.html', {'form': form})

@login_required
def delete_task(request, id):
    task = Tarefa.objects.get(id=id)
    if task.user == request.user:
        task.delete()
    else:
        messages.error(request, 'Você não tem permissão para exlcuir essa tarefa.')
        return render(request, 'home/index.html')
    return redirect('home')

@login_required
def update_task(request, id):
    task = get_object_or_404(Tarefa, id=id, user=request.user)
    if request.method == 'POST':
        form = TarefaForm(user=request.user, data=request.POST, instance=task)
        if form.is_valid():
            form.save()    
            return redirect('home')
    else:
        form = TarefaForm(user=request.user, instance=task)
    return render(request, 'tarefas/new_task.html', {'form':form})

@login_required
def delete_category(request, id):
    categorie = Categoria.objects.get(id=id)
    if categorie.user == request.user:
        categorie.delete()
    else:
        messages.error(request, 'Você não tem permissão para exlcuir essa categoria.')
        return render(request, 'tarefas/list_categories.html')        
    return redirect('list_category')

@login_required
def update_category(request, id):
    category = get_object_or_404(Categoria, id=id, user=request.user)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=category)
        if form.is_valid():
            form.save()    
            return redirect('list_category')
    else:
        form = CategoriaForm(instance=category)
    return render(request, 'tarefas/new_category.html', {'form':form})


@login_required
def search(request):
    query = request.GET.get('search')
    if query is not None:
        result = Tarefa.objects.search(query, request.user)
    return render(request, 'tarefas/search_result.html', {'result':result})


@login_required
def task_details(request, id):
    task = get_object_or_404(Tarefa, id=id)
    return render(request, 'tarefas/result_details.html', {'task':task})