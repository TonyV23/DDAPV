from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpRequest

from fondation.models import Donor
from fondation.forms import DonorForm

def index(request) :

    page_title = 'Aperçu sur les aides et dons'

    return render(
        request,
        'fondation/donations/index.html',
        {
            'page_title' : page_title
        }
    )

def donors_add(request) :
    assert isinstance(request, HttpRequest)
    page_title = 'Faire un don'
    donors = Donor.objects.all()

    if request.method == 'GET' :
        form = DonorForm()

    return render(
        request,
        'fondation/donations/add_donator.html',
        {
            'page_title' : page_title,
            'donors' : donors,
            'form' : form,
        }
    )

def donors_store(request) :
    if request.method == 'POST':
        form = DonorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Le (la) donateur (trice) a été enregistré avec succès !")
        else :
            messages.error(request, form.errors)
        return redirect('/donations/display')

def donors_edit(request, id) :
    assert isinstance(request, HttpRequest)
    page_title = 'Modifier l\'état du don'
    if request.method == 'GET':
        if id == 0:
            form = DonorForm()
        else:
            donor = Donor.objects.get(pk=id)
            form = DonorForm(instance=donor)
        return render(
            request,
            'fondation/donations/edit_donor.html',
            {
                'form': form,
                'page_title' :page_title
            }
        )

def donors_update(request, id) :
    if request.method == 'POST':
        if id == 0:
            form = DonorForm(request.POST)
        else:
            donor = Donor.objects.get(pk=id)
            form = DonorForm(request.POST, instance=donor)
        if form.is_valid():
            form.save()
        messages.success(request, "L'état du donateur a été modifié avec succès !")
        return redirect('/donations/display')

def donors_delete(request,id) :
    donors = Donor.objects.get(pk = id)
    donors.delete()
    messages.success(request,"Le (la) donateur (trice) a été supprimé avec succès !")
    return redirect('/donations/display')


def donors_display(request) :
    
    page_title = 'Liste des donateurs'
    donors = Donor.objects.all()

    return render(
        request,
        'fondation/donations/donors_display.html',
        {
            'donors' : donors,
            'page_title' : page_title
        }
    )