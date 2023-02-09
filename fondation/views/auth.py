from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.http import HttpRequest

from fondation.forms import UserForm, UserEditInfoForm, UserChangePasswordForm
from fondation.decorators import unauthenticated_user, allowed_users

@login_required(login_url ='login')
@allowed_users(allowed_roles= ['admins'])
def index(request):
    page_title = 'Aperçu sur les utilisateurs'
    template = 'fondation/user/index.html'

    variable = {
        'page_title' : page_title,
    }

    return render(
        request,
        template_name = template,
        context = variable
    )
    
@login_required(login_url ='login')
def userList(request) :
    page_title = 'Liste des utilisateurs'
    users = User.objects.all()
    template = 'fondation/user/list.html'

    variable = {
        'page_title' : page_title,
        'users' : users
    }

    return render(
        request,
        template_name = template,
        context = variable
    )

@login_required(login_url ='login')
def userRegister(request) :
    page_title = 'Nouveau utilisateur'
    template = 'fondation/user/register.html'
    form = UserForm()

    variable = {
        'page_title' : page_title,
        'form': form
    }
    
    return render(
        request, 
        template_name = template,
        context = variable
    )

@login_required(login_url ='login')
def userStore(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name = 'employees')
            user.groups.add(group)    
            messages.success(request, 'Le compte de '+username+' a été ajouté')
        
        return redirect('/userList/')

@unauthenticated_user
def userLogin(request) :
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/dashboard')
        else:
            messages.info(request, 'Nom d\'utilisateur ou mot de passe incorrect')

    page_title = 'Connexion'
    template  = 'fondation/user/login.html'
    
    variable = {

        'page_title' : page_title

    }

    return render(
        request,
        template_name = template,
        context = variable
    )

@login_required(login_url ='login')
@allowed_users(allowed_roles= ['admins'])
def userEdit(request, id) :
    assert isinstance(request, HttpRequest)
    page_title = 'Modifier les informations de l\'utilisateur'
    if request.method == 'GET':
        if id == 0:
            form = UserEditInfoForm()
        else:
            user = User.objects.get(pk=id)
            form = UserEditInfoForm(instance=user)
        return render(
            request,
            'fondation/user/edit_user.html',
            {
                'form': form,
                'page_title' :page_title
            }
        )

@login_required(login_url ='login')
@allowed_users(allowed_roles= ['admins'])
def userChangePassword(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'POST':
        form = UserChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            user = User
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Votre mot de passe a été bien modifié !')
            return redirect('/dashboard')
        else:
            messages.error(request, "Une erreur est survenue !")
    else:
        form = UserChangePasswordForm(request.user)
    return render(request, 'fondation/user/password_change.html', {
        'form': form
    })

@login_required(login_url ='login')
@allowed_users(allowed_roles= ['employees'])
def userChangePasswordEmployee(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'POST':
        form = UserChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            user = User
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Votre mot de passe a été bien modifié !')
            return redirect('/employeeDashboard')
        else:
            messages.error(request, "Une erreur est survenue !")
    else:
        form = UserChangePasswordForm(request.user)
    return render(request, 'fondation/user/password_change_employee.html', {
        'form': form
    })


@login_required(login_url ='login')
def userUpdate(request, id) :
    if request.method == 'POST':
        if id == 0:
            form = UserEditInfoForm(request.POST)
        else:
            user = User.objects.get(pk=id)
            form = UserEditInfoForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Les informations de l'utilisateur ont été modifié avec succès !")
        return redirect('/userList') 


def userLogout(request) :
    logout(request)

    return redirect('/login')

@login_required(login_url ='login')
def userDelete(request, id) :
    user = User.objects.get(pk = id)
    user.delete()
    messages.success(request, 'Le compte a été supprimé avec succès')
