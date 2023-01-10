from django.shortcuts import render


def index(request) :

    page_title = 'Aperçu sur les aides et dons'


    return render(
        request,
        'fondation/donations/index.html',
        {
            'page_title' : page_title
        }
    )

def add_type(request) :

    page_title = 'Nouveau type de dons ou aides'

    return render(
        request,
        'fondation/donations/donations_type.html',
        {
            'page_title' : page_title
        }
    )


def add_donation_help(request) :

    page_title = 'Nouveau aide ou don'

    return render(
        request,
        'fondation/donations/donations_help.html',
        {
            'page_title' : page_title
        }
    )

def display(request) :
    
    page_title = 'Liste des dons et aides'

    return render(
        request,
        'fondation/donations/display.html',
        {
            'page_title' : page_title
        }
    )

def donors_display(request) :

    page_title = 'Liste des donateurs'

    return render(
        request,
        'fondation/donations/donors_display.html',
        {
            'page_title' : page_title
        }
    )