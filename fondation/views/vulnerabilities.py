from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpRequest


from fondation.forms import VulnerabilityForm
from fondation.models import Vulnerability

def index (request) :
    
    page_title = 'Aperçu sur les vulnerabilités'

    return render(
        request,
        'fondation/vulnerabilities/index.html',
        {
            'page_title' : page_title
        }
    )


def vulnerabilities_add(request) :

    assert isinstance(request, HttpRequest)
    page_title = 'Nouvelle vulnerabilité'

    if request.method == 'GET' :
        form = VulnerabilityForm()
    
    return render(
        request,
        'fondation/vulnerabilities/add_vulnerabilities.html',
        {
            'form' : form,
            'page_title' : page_title
        }
    )

def vulnerabilities_store(request) :
    if request.method == 'POST':
        form = VulnerabilityForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"La situation de vulnerabilité a été enregistré avec succès !")
        else :
            messages.error(request, form.errors)
        return redirect('/vulnerabilities/display')

def vulnerabilities_edit(request, id) :
    assert isinstance(request, HttpRequest)
    page_title = 'Modifier la situation de vulnerabilité'
    if request.method == 'GET':
        if id == 0:
            form = VulnerabilityForm()
        else:
            vulnerability = Vulnerability.objects.get(pk=id)
            form = VulnerabilityForm(instance=vulnerability)
        
        return render(
            request,
            'fondation/vulnerabilities/edit_vulnerability.html',
            {
                'form': form,
                'page_title' :page_title
            }
        )

def vulnerabilities_update(request, id) :
    if request.method == 'POST':
        if id == 0:
            form = VulnerabilityForm(request.POST)
        else:
            vulnerability = Vulnerability.objects.get(pk=id)
            form = VulnerabilityForm(request.POST, instance=vulnerability)
        if form.is_valid():
            form.save()
        messages.success(request, "La situation de vulnerabilité a été modifié avec succès !")
        return redirect('/vulnerabilities/display')

def vulnerabilities_delete(request, id) :
    vulnerabilities = Vulnerability.objects.get(pk = id)
    vulnerabilities.delete()
    messages.success(request,"La situation de vulnerabilité a été supprimé avec succès !")
    return redirect('/vulnerabilities/display')


def display (request) :
    page_title = 'Liste des vulnerabilités'
    vulnerabilities = Vulnerability.objects.all()

    return render(
        request,
        'fondation/vulnerabilities/display.html',
        {
            'vulnerabilities' : vulnerabilities,
            'page_title' : page_title
        }
    )
