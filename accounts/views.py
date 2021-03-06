from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

from .forms import UserForm


def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            u = form.save()
            u.set_password(u.password)
            u.save()
            messages.success(request, 'Login criado com sucesso!')
            return redirect('user_login')
    else:
        form = UserForm()
    return render(request, 'accounts/add_user.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return redirect(request.GET.get('next', '/')) # redirecionar o next da url.
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
    return render(request, 'accounts/user_login.html')


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Senha alterada com sucesso.')
            return redirect('change_password')
        else:
            messages.error(request, 'Não foi possível alterar a senha.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {'form': form})


@login_required
def user_logout(request):
    logout(request)
    messages.info(request, 'Você se deslogou.')
    return redirect('user_login')
