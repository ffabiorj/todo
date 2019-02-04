from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.contrib.auth.decorators import login_required

from tarefas.models import Tarefa

@login_required
def home(request):
    tarefas = Tarefa.objects.filter(user=request.user, status='')
    return render(request, 'home/index.html', {'tarefas': tarefas})