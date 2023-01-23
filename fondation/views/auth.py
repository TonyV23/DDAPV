from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages


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