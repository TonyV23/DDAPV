from django.shortcuts import render


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

    page_title = 'Ajouter province'

    return render(
        request,
        'fondation/address/add_province.html',
        {
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


def add_zone(request) :

    page_title = 'Ajouter zone'

    return render(
        request,
        'fondation/address/add_zone.html',
        {
            'page_title' : page_title
        }
    )

def add_quartier_colline(request) :

    page_title = 'Ajouter quartier/ colline'

    return render(
        request,
        'fondation/address/add_quartier_colline.html',
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

def view_zones(request) :
    
    page_title = 'Liste des zones'

    return render(
        request,
        'fondation/address/view_zones.html',
        {
            'page_title' : page_title
        }
    )
