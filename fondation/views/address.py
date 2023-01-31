from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required

from fondation.forms import ProvinceForm, CommuneForm
from fondation.models import Province, Commune

@login_required(url ='login')
def index (request) :

    page_title = 'Aperçu sur les addresses'

    return render(
        request,
        'fondation/address/index.html',
        {
            'page_title' : page_title
        }
    )

@login_required(url ='login')
def add_province(request) :
    assert isinstance(request, HttpRequest)
    page_title = 'Ajouter une province'
    if request.method == 'GET' :
        form = ProvinceForm ()

    return render(
        request,
        'fondation/address/add_province.html',
        {
            'form' : form,
            'page_title' : page_title
        }
    )

@login_required(url ='login')
def store_province(request) : 
    if request.method == 'POST':
        form = ProvinceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"La province a été enregistré avec succès !")
        else :
            messages.error(request, form.errors)
        return redirect('/address/address_view_provinces')

@login_required(url ='login')
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

@login_required(url ='login')
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


@login_required(url ='login')
def add_commune(request) :
    assert isinstance(request, HttpRequest)
    page_title = 'Ajouter une commune'
    provinces = Province.objects.all()

    if request.method == 'GET' :
        form = CommuneForm()

    return render(
        request,
        'fondation/address/add_commune.html',
        {
            'form' : form,
            'page_title' : page_title,
            'provinces' : provinces
        }
    )

@login_required(url ='login')
def store_commune(request) :
    if request.method == 'POST':
        form = CommuneForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"La commune a été enregistré avec succès !")
        else :
            messages.error(request, form.errors)
        return redirect('/address/address_view_communes')

def commune_edit(request, id) :
    assert isinstance(request, HttpRequest)
    page_title = 'Modifier la commune'
    if request.method == 'GET':
        if id == 0:
            form = CommuneForm()
        else:
            province = Commune.objects.get(pk=id)
            form = CommuneForm(instance=province)
        return render(
            request,
            'fondation/address/address_edit_commune.html',
            {
                'form': form,
                'page_title' :page_title
            }
        )

@login_required(url ='login')
def commune_update(request, id) :
    if request.method == 'POST':
        if id == 0:
            form = CommuneForm(request.POST)
        else:
            commune = Commune.objects.get(pk=id)
            form = CommuneForm(request.POST, instance=commune)
        if form.is_valid():
            form.save()
        messages.success(request, "La commune a été modifié avec succès !")
        return redirect('/address/address_view_communes')

@login_required(url ='login')
def commune_delete(request, id) :
    communes = Commune.objects.get(pk = id)
    communes.delete()
    messages.success(request,"La commune a été supprimé avec succès !")
    return redirect('/address/address_view_communes')


    page_title = 'Origines des refugiés'

    return render(
        request,
        'fondation/address/display.html',
        {
            'page_title' : page_title
        }
    )
@login_required(url ='login')
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

@login_required(url ='login')
def view_communes(request) :
    
    page_title = 'Liste des communes'
    communes = Commune.objects.all()

    return render(
        request,
        'fondation/address/address_view_communes.html',
        {
            'page_title' : page_title,
            'communes' : communes
        }
    )
