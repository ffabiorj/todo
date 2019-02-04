from django.urls import path

from . import views

urlpatterns = [
    path('lista-categorias/', views.list_category, name='list_category'),
    path('nova-categoria/', views.new_category, name='new_category'),
    path('nova-tarefa/', views.new_task, name='new_task'),
    path('deleta-tarefa/<int:id>', views.delete_task, name='delete_task'),
    path('atualizar-tarefa/<int:id>', views.update_task, name='update_task'),
    path('deleta-categoria/<int:id>', views.delete_category, name='delete_category'),
    path('atualizar-cagegoria/<int:id>', views.update_category, name='update_category'),
    path('detalhe-tarefa/<int:id>', views.task_details, name='task_details'),
    path('buscar/', views.search, name='search'),
]
