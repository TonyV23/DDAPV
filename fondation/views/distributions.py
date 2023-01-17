from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpRequest

from fondation.forms import DistributionForm
from fondation.models import Distribution , Camp, Person


def index (request) :

    page_title = 'Aperçu sur les distributions'

    return render(
        request,
        'fondation/distributions/index.html',
        {
            'page_title' : page_title,
        }
    )

def distribution_add(request) :
    assert isinstance(request, HttpRequest)
    page_title = 'Nouvelle distribution'
    if request.method == 'GET' :
        form = DistributionForm()

    return render(
        request,
        'fondation/distributions/add_distribution.html',
        {
            'form' : form,
            'page_title' : page_title,
        }
    )

def distribution_store(request) :
    if request.method == 'POST':
        form = DistributionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"La distribution a été enregistré avec succès !")
        else :
            messages.error(request, form.errors)
        return redirect('/distributions/display')

def distribution_edit(request, id) :
    assert isinstance(request, HttpRequest)
    page_title = 'Modifier la distribution'
    if request.method == 'GET':
        if id == 0:
            form = DistributionForm()
        else:
            distribution = Distribution.objects.get(pk=id)
            form = DistributionForm(instance=distribution)
        return render(
            request,
            'fondation/distributions/edit_distribution.html',
            {
                'form': form,
                'page_title' :page_title
            }
        )

def distribution_update(request, id) :
    if request.method == 'POST':
        if id == 0:
            form = DistributionForm(request.POST)
        else:
            distribution = Distribution.objects.get(pk=id)
            form = DistributionForm(request.POST, instance=distribution)
        if form.is_valid():
            form.save()
        messages.success(request, "La distribution a été modifié avec succès !")
        return redirect('/distributions/display')

def distribution_delete(request, id) :
    distributions = Distribution.objects.get(pk = id)
    distributions.delete()
    messages.success(request,"La distribution a été supprimé avec succès !")
    return redirect('/distributions/display')

def display(request) :

    page_title = 'Liste des distributions'
    distributions = Distribution.objects.all()
    camps = Camp.objects.all()

    return render(
        request,
        'fondation/distributions/distributions_overview.html',
        { 
            'camps' : camps,
            'page_title' : page_title,
            'distributions' : distributions,
        }
    )

def display_by_id(request, id) :
    assert isinstance(request, HttpRequest)
    page_title = 'Les refugiés du camps' 
    distributions = Distribution.objects.filter(camp_id=id).all()
 
    return render(
        request,
        'fondation/distributions/display_distribution_by_id.html',
        {
            'distributions' : distributions,
            'page_title' : page_title,        
        }
    ) 

def getBeneficiaire(request) :
    camp_id = request.GET.get('id_camp')
    beneficiaires = Person.objects.filter(camp_id = camp_id)
    return render(
        request,
        'fondation/distributions/getBeneficiaire.html',
        {
            'beneficiaires': beneficiaires,
        }
    )