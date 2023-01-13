from django.shortcuts import render

from fondation.forms import ProvinceForm

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

    page_title = 'Ajouter une province'
    form = ProvinceForm


    return render(
        request,
        'fondation/address/add_province.html',
        {
            'form' : form,
            'page_title' : page_title
        }
    )

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

    return render(
        request,
        'fondation/address/view_provinces.html',
        {
            'page_title' : page_title
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
