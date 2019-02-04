# Generated by Django 2.0.5 on 2018-05-31 00:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('descricao', models.TextField(verbose_name='Descrição')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tarefa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('descricao', models.TextField(blank=True, verbose_name='Descrição')),
                ('data_final', models.DateField(verbose_name='Data final')),
                ('prioridade', models.CharField(choices=[('B', 'Baixa'), ('M', 'Média'), ('A', 'Alta')], max_length=1, verbose_name='Prioridade')),
                ('status', models.CharField(blank=True, choices=[('C', 'Concluído'), ('CD', 'Cancelado')], default='', max_length=5, verbose_name='Status')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tarefas.Categoria', verbose_name='Categoria')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
