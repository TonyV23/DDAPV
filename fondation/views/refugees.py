from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpRequest

from fondation.forms import RefugeeForm
from fondation.models import Person, Province, Commune


def index (request):

    page_title = 'Aperçu sur les personnes vulnérables'

    return render(
        request,
        'fondation/refugees/index.html',
        {
            'page_title' : page_title,
        }
    )

def refugees_add(request) :
    assert isinstance(request, HttpRequest)
    page_title = 'Nouvelle personne'
    provinces = Province.objects.all()
    if request.method == 'GET' :
        form = RefugeeForm()

    return render(
        request,
        'fondation/refugees/add_refugee.html',
        {
            'provinces' : provinces,
            'form' : form,
            'page_title' : page_title,
        }
    )

def refugees_store(request) :
    if request.method == 'POST':
        form = RefugeeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"La personne a été enregistré avec succès !")
        else :
            messages.error(request, form.errors)
        return redirect('/refugees/display/')

def refugees_edit(request, id) :
    assert isinstance(request, HttpRequest)
    page_title = 'Modifier les infos de la personne'
    if request.method == 'GET':
        if id == 0:
            form = RefugeeForm()
        else:
            refugee = Person.objects.get(pk=id)
            form = RefugeeForm(instance=refugee)
        return render(
            request,
            'fondation/refugees/edit_refugee.html',
            {
                'form': form,
                'page_title' :page_title
            }
        )


def refugees_update(request, id) :
    if request.method == 'POST':
        if id == 0:
            form = RefugeeForm(request.POST)
        else:
            refugee = Person.objects.get(pk=id)
            form = RefugeeForm(request.POST, instance=refugee)
        if form.is_valid():
            form.save()
        messages.success(request, "Les infos de la personne ont été modifié avec succès !")
        return redirect('/refugees/display/')

def refugees_delete(request, id) :
    refugee = Person.objects.get(pk = id)
    refugee.delete()
    messages.success(request,"Les infos de la personne ont été supprimé avec succès !")
    return redirect('/refugees/display/')

def refugees_display(request) :
    page_title = 'Liste des personnes vulnérables'
    refugees = Person.objects.all()

    return render(
        request,
        'fondation/refugees/display_refugees.html',
        {
            'refugees' : refugees,
            'page_title' : page_title,
        }
    )

def getCommunes(request):
    province_id = request.GET.get('id_nom_de_la_province')
    communes = Commune.objects.filter(nom_de_la_province_id = province_id)
    return render(
        request,
        'fondation/address/getCommunes.html',
        {
            'communes': communes
        }
    )