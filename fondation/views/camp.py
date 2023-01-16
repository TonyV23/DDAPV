from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpRequest

from fondation.models import Camp
from fondation.forms import CampForm

def index(request) :

    page_title = 'Aperçu sur les camps'

    return render(
        request,
        'fondation/camps/index.html',
        {
            'page_title' : page_title
        }
    )

def camps_add(request) :
    assert isinstance(request, HttpRequest)
    page_title = 'Ajouter un camp'

    if request.method == 'GET' :
        form = CampForm()

    return render(
        request,
        'fondation/camps/add_camp.html',
        {
            'page_title' : page_title,
            'form' : form,
        }
    )


def camps_store(request) :
    if request.method == 'POST':
        form = CampForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Le camp a été enregistré avec succès !")
        else :
            messages.error(request, form.errors)
        return redirect('/camps/camps_display')


def camps_edit(request, id) :
    assert isinstance(request, HttpRequest)
    page_title = 'Modifier le camp'
    if request.method == 'GET':
        if id == 0:
            form = CampForm()
        else:
            camp = Camp.objects.get(pk=id)
            form = CampForm(instance=camp)
        return render(
            request,
            'fondation/camps/edit_camp.html',
            {
                'form': form,
                'page_title' :page_title
            }
        )


def camps_update(request, id) :
    if request.method == 'POST':
        if id == 0:
            form = CampForm(request.POST)
        else:
            camp = Camp.objects.get(pk=id)
            form = CampForm(request.POST, instance=camp)
        if form.is_valid():
            form.save()
        messages.success(request, "Le camp a été modifié avec succès !")
        return redirect('/camps/camps_display')


def camps_delete(request, id) :
    camps = Camp.objects.get(pk = id)
    camps.delete()
    messages.success(request,"Le camp a été supprimé avec succès !")
    return redirect('/camps/camps_display')


def camps_display(request) :
    camps = Camp.objects.all()
    page_title = 'Les camps d\'intervention'

    return render(
        request,
        'fondation/camps/view_camp.html',
        {
            'camps' : camps,
            'page_title' : page_title
        }
    ) 