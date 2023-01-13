from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpRequest

from fondation.forms import ProvinceForm
from fondation.models import Province

def index (request) :

    page_title = 'Aperçu sur les addresses'

    return render(
        request,
        'fondation/address/index.html',
        {
            'page_title' : page_title
        }
    )

def add_province(request) :
    assert isinstance(request, HttpRequest)
    page_title = 'Ajouter une province'
    if request.method == 'GET' :
        form = ProvinceForm

    return render(
        request,
        'fondation/address/add_province.html',
        {
            'form' : form,
            'page_title' : page_title
        }
    )

def store_province(request) : 
    if request.method == 'POST':
        form = ProvinceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"La province a été enregistré avec succès !")
        else :
            messages.error(request, form.errors)
        return redirect('/address/address_view_provinces')

def province_edit(request, id) :
    assert isinstance(request, HttpRequest)
    page_title = 'Modifier la province'
    if request.method == 'GET':
        if id == 0:
            form = ProvinceForm()
        else:
            province = Province.objects.get(pk=id)
            form = ProvinceForm(instance=province)
        return render(
            request,
            'fondation/address/address_edit_province.html',
            {
                'form': form,
                'page_title' :page_title
            }
        )

def province_update(request, id):
    if request.method == 'POST':
        if id == 0:
            form = ProvinceForm(request.POST)
        else:
            province = Province.objects.get(pk=id)
            form = ProvinceForm(request.POST, instance=province)
        if form.is_valid():
            form.save()
        messages.success(request, "La province a été modifié avec succès !")
        return redirect('/address/address_view_provinces')

def province_delete(request, id):
    provinces = Province.objects.get(pk = id)
    provinces.delete()
    messages.success(request,"La province a été supprimé avec succès !")
    return redirect('/address/address_view_provinces')


def add_commune(request) :

    page_title = 'Ajouter commune'

    return render(
        request,
        'fondation/address/add_commune.html',
        {
            'page_title' : page_title
        }
    )



def display(request) :

    page_title = 'Origines des refugiés'

    return render(
        request,
        'fondation/address/display.html',
        {
            'page_title' : page_title
        }
    )

def view_provinces(request) :
    
    page_title = 'Liste des provinces'
    provinces = Province.objects.all()

    return render(
        request,
        'fondation/address/address_view_provinces.html',
        {
            'page_title' : page_title,
            'provinces' : provinces
        }
    )

def view_communes(request) :
    
    page_title = 'Liste des communes'

    return render(
        request,
        'fondation/address/view_communes.html',
        {
            'page_title' : page_title
        }
    )
