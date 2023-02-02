from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required

from fondation.forms import TypeAssistanceForm
from fondation.models import TypeAssistance
from fondation.decorators import allowed_users

@login_required(login_url ='login')
@allowed_users(allowed_roles= ['admins'])
def index(request) :

    page_title = 'Aperçu sur les types d\'assistance'

    return render(
        request,
        'fondation/typeAssistance/index.html',
        {
            'page_title' : page_title
        }
    )

@login_required(login_url ='login')
def type_assistance_add(request) :
    assert isinstance(request, HttpRequest)
    page_title = 'Ajouter un type d\'assistance'
    
    if request.method == 'GET' :
        form = TypeAssistanceForm()

    return render(
        request,
        'fondation/typeAssistance/add_type_assistance.html',
        {
            'form' : form,
            'page_title' : page_title
        }
    )

@login_required(login_url ='login')
def type_assistance_store(request) :
    if request.method == 'POST':
        form = TypeAssistanceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Le type d\'assistance a été enregistré avec succès !")
        else :
            messages.error(request, form.errors)
        return redirect('/typeAssistance/display')

@login_required(login_url ='login')
def type_assistance_edit(request, id) :
    assert isinstance(request, HttpRequest)
    page_title = 'Modifier le type d\'aide'
    if request.method == 'GET':
        if id == 0:
            form = TypeAssistanceForm()
        else:
            type_assistance = TypeAssistance.objects.get(pk=id)
            form = TypeAssistanceForm(instance=type_assistance)
        
        return render(
            request,
            'fondation/typeAssistance/edit_type_assistance.html',
            {
                'form': form,
                'page_title' :page_title
            }
        )

@login_required(login_url ='login')
def type_assistance_update(request,id) :
    if request.method == 'POST':
        if id == 0:
            form = TypeAssistanceForm(request.POST)
        else:
            type_assistance = TypeAssistance.objects.get(pk=id)
            form = TypeAssistanceForm(request.POST, instance=type_assistance)
        if form.is_valid():
            form.save()
        messages.success(request, "Le type d\'aide a été modifié avec succès !")
        return redirect('/typeAssistance/display')

@login_required(login_url ='login')
def type_assistance_delete(request, id) :
    type_assistance = TypeAssistance.objects.get(pk = id)
    type_assistance.delete()
    messages.success(request,"Le type d\'aide a été supprimé avec succès !")
    return redirect('/typeAssistance/display')

@login_required(login_url ='login')
def display(request) :

    page_title = 'Liste des types d\'assistance'
    type_assistances = TypeAssistance.objects.all()

    return render(
        request,
        'fondation/typeAssistance/display.html',
        {
            'type_assistances' : type_assistances,
            'page_title' : page_title
        }
    )

