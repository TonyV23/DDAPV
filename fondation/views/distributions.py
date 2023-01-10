from django.shortcuts import render 


def index (request) :

    page_title = 'Aperçu sur les distributions'

    return render(
        request,
        'fondation/distributions/index.html',
        {
            'page_title' : page_title,
        }
    )

def add_distribution(request) :

    page_title = 'Nouvelle distribution'

    return render(
        request,
        'fondation/distributions/add_distribution.html',
        {
            'page_title' : page_title,
        }
    )

def display(request) :

    page_title = 'Liste des distributions'

    return render(
        request,
        'fondation/distributions/display.html',
        {
            'page_title' : page_title,
        }
    )

        