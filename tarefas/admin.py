from django.contrib import admin

from .models import Categoria, Tarefa

# Register your models here.


class CategariaAdmin(admin.ModelAdmin):
    pass


class TarefaAdmin(admin.ModelAdmin):
    pass


admin.site.register(Categoria, CategariaAdmin)
admin.site.register(Tarefa, TarefaAdmin)
