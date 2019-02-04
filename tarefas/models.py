from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class TarefaManager(models.Manager):
    def search(self, query, user):
        return self.get_queryset().filter(models.Q(nome__icontains=query) | 
                                    models.Q(descricao__icontains=query) | 
                                    models.Q(categoria__nome__icontains=query), 
                                    user=user)

class Categoria(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome')
    descricao = models.TextField(verbose_name='Descrição')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.nome


class Tarefa(models.Model):
    PRIORIDADE_CHOICES = (
        ('B', 'Baixa'),
        ('M', 'Média'),
        ('A', 'Alta'),
    )
    
    CONCLUIDO = 'C'
    CANCELADO = 'CD'
    STATUS_CHOICES = (
        (CONCLUIDO, 'Concluído'),
        (CANCELADO, 'Cancelado'),

    )
    nome = models.CharField(max_length=100, verbose_name='Nome')
    descricao = models.TextField(blank=True, verbose_name='Descrição')
    data_final = models.DateField(verbose_name='Data final')
    prioridade = models.CharField(max_length=1, choices=PRIORIDADE_CHOICES, verbose_name='Prioridade')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name='Categoria')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(u'Status', max_length=5, choices=STATUS_CHOICES, blank=True, default='')

    objects = TarefaManager()

    def __str__(self):
        return self.nome
