from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required

from fondation.forms import MatiralStatusForm
from fondation.models import MatiralStatus
from fondation.decorators import allowed_users

@login_required(login_url ='login')
@allowed_users(allowed_roles= ['admins'])
def index(request) :

    page_title = 'Aperçu sur les situations matrimoniales'

    return render(
        request,
        'fondation/matiralStatus/index.html',
        {
            'page_title' : page_title
        }
    )

@login_required(login_url ='login')
def matiral_status_add(request) :
    assert isinstance(request, HttpRequest)
    page_title = 'Ajouter une situation matrimoniale'
    
    if request.method == 'GET' :
        form = MatiralStatusForm()

    return render(
        request,
        'fondation/matiralStatus/add_matiral_status.html',
        {
            'form' : form,
            'page_title' : page_title
        }
    )

@login_required(login_url ='login')
def matiral_status_store(request) :
    if request.method == 'POST':
        form = MatiralStatusForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"La situation matrimoniale a été enregistré avec succès !")
        else :
            messages.error(request, form.errors)
        return redirect('/matiralStatus/display')

@login_required(login_url ='login')
def matiral_status_edit(request, id) :
    assert isinstance(request, HttpRequest)
    page_title = 'Modifier la situation matrimoniale'
    if request.method == 'GET':
        if id == 0:
            form = MatiralStatusForm()
        else:
            matiral_status = MatiralStatus.objects.get(pk=id)
            form = MatiralStatusForm(instance=matiral_status)
        
        return render(
            request,
            'fondation/matiralStatus/edit_matiral_status.html',
            {
                'form': form,
                'page_title' :page_title
            }
        )

@login_required(login_url ='login')
def matiral_status_update(request,id) :
    if request.method == 'POST':
        if id == 0:
            form = MatiralStatusForm(request.POST)
        else:
            matiral_status = MatiralStatus.objects.get(pk=id)
            form = MatiralStatusForm(request.POST, instance=matiral_status)
        if form.is_valid():
            form.save()
        messages.success(request, "La situation matrimoniale a été modifié avec succès !")
        return redirect('/matiralStatus/display')

@login_required(login_url ='login')
def matiral_status_delete(request, id) :
    matiral_status = MatiralStatus.objects.get(pk = id)
    matiral_status.delete()
    messages.success(request,"La situation matrimoniale a été supprimé avec succès !")
    return redirect('/matiralStatus/display')

@login_required(login_url ='login')
def display(request) :

    page_title = 'Liste des situations matrimoniales'
    matiral_status = MatiralStatus.objects.all()

    return render(
        request,
        'fondation/matiralStatus/display.html',
        {
            'matiral_status' : matiral_status,
            'page_title' : page_title
        }
    )

