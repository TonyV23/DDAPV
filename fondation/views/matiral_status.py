from django.shortcuts import render


def index(request) :

    page_title = 'Aperçu sur les situations matrimoniales'


    return render(
        request,
        'fondation/matiralStatus/index.html',
        {
            'page_title' : page_title
        }
    )

def add_matiral_status(request) :

    page_title = 'Ajouter situation matrimoniale'


    return render(
        request,
        'fondation/matiralStatus/add_matiral_status.html',
        {
            'page_title' : page_title
        }
    )

def display(request) :

    page_title = 'Liste des situations matrimoniales'


    return render(
        request,
        'fondation/matiralStatus/display.html',
        {
            'page_title' : page_title
        }
    )

