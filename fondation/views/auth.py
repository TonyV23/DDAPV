from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from fondation.forms import UserForm

@login_required(url ='login')
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
    
@login_required(url ='login')
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

@login_required(url ='login')
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

@login_required(url ='login')
def userStore(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Le compte de '+user+' a été ajouté')
        return redirect('/userList/')

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

def userLogout(request) :
    logout(request)

    return redirect('/login')