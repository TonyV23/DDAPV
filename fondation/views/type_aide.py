from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required

from fondation.forms import TypeAideForm
from fondation.models import TypeAide

@login_required(login_url ='login')
def index(request) :

    page_title = 'Aperçu sur les types d\'aides'

    return render(
        request,
        'fondation/typeAide/index.html',
        {
            'page_title' : page_title
        }
    )

@login_required(login_url ='login')
def type_aide_add(request) :
    assert isinstance(request, HttpRequest)
    page_title = 'Ajouter un type d\'aides'
    
    if request.method == 'GET' :
        form = TypeAideForm()

    return render(
        request,
        'fondation/typeAide/add_type_aide.html',
        {
            'form' : form,
            'page_title' : page_title
        }
    )

@login_required(login_url ='login')
def type_aide_store(request) :
    if request.method == 'POST':
        form = TypeAideForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Le type d\'aides a été enregistré avec succès !")
        else :
            messages.error(request, form.errors)
        return redirect('/typeAide/display')

@login_required(login_url ='login')
def type_aide_edit(request, id) :
    assert isinstance(request, HttpRequest)
    page_title = 'Modifier le type d\'aide'
    if request.method == 'GET':
        if id == 0:
            form = TypeAideForm()
        else:
            type_aide = TypeAide.objects.get(pk=id)
            form = TypeAideForm(instance=type_aide)
        
        return render(
            request,
            'fondation/typeAide/edit_type_aide.html',
            {
                'form': form,
                'page_title' :page_title
            }
        )

@login_required(login_url ='login')
def type_aide_update(request,id) :
    if request.method == 'POST':
        if id == 0:
            form = TypeAideForm(request.POST)
        else:
            type_aide = TypeAide.objects.get(pk=id)
            form = TypeAideForm(request.POST, instance=type_aide)
        if form.is_valid():
            form.save()
        messages.success(request, "Le type d\'aide a été modifié avec succès !")
        return redirect('/typeAide/display')

@login_required(login_url ='login')
def type_aide_delete(request, id) :
    type_aide = TypeAide.objects.get(pk = id)
    type_aide.delete()
    messages.success(request,"Le type d\'aide a été supprimé avec succès !")
    return redirect('/typeAide/display')

@login_required(login_url ='login')
def display(request) :

    page_title = 'Liste des types d\'aides'
    type_aides = TypeAide.objects.all()

    return render(
        request,
        'fondation/TypeAide/display.html',
        {
            'type_aides' : type_aides,
            'page_title' : page_title
        }
    )

