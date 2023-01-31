from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required

from fondation.forms import DistributionForm
from fondation.models import Distribution, Commune, TypeAssistance
from fondation.filters import DistributionFilter

@login_required(url ='login')
def index (request) :

    page_title = 'Aperçu sur les distributions'

    return render(
        request,
        'fondation/distributions/index.html',
        {
            'page_title' : page_title,
        }
    )

@login_required(url ='login')
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

@login_required(url ='login')
def distribution_store(request) :
    if request.method == 'POST':
        form = DistributionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"La distribution a été enregistré avec succès !")
        else :
            messages.error(request, form.errors)
        return redirect('/distributions/display')

@login_required(url ='login')
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

@login_required(url ='login')
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

@login_required(url ='login')
def distribution_delete(request, id) :
    distributions = Distribution.objects.get(pk = id)
    distributions.delete()
    messages.success(request,"La distribution a été supprimé avec succès !")
    return redirect('/distributions/display')

@login_required(url ='login')
def display(request) :

    page_title = 'Liste des distributions'
    distributions = Distribution.objects.all()
    filter = DistributionFilter(request.GET, distributions)
    distributions = filter.qs

    return render(
        request,
        'fondation/distributions/display.html',
        { 
            'page_title' : page_title,
            'distributions' : distributions,
            'filter' : filter,
        }
    )

@login_required(url ='login')
def getCommunes(request):
    province_id = request.GET.get('id_province')
    communes = Commune.objects.filter(nom_de_la_province_id = province_id)
    return render(
        request,
        'fondation/distributions/getCommune.html',
        {
            'communes': communes
        }
    )

@login_required(url ='login')
def getAssistance(request):
    type_aid_id = request.GET.get('id_type_aide')
    type_assistances = TypeAssistance.objects.filter(type_aide_id = type_aid_id)
    return render(
        request,
        'fondation/distributions/getAssistance.html',
        {
            'type_assistances': type_assistances
        }
    )