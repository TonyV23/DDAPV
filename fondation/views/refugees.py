from django.shortcuts import render


def index (request):

    page_title = 'Aperçu sur les refugiés'

    return render(
        request,
        'fondation/refugees/index.html',
        {
            'page_title' : page_title,
        }
    )


def add(request):

    page_title = 'Nouveau refugié'

    return render(
        request,
        'fondation/refugees/add.html',
        {
            'page_title' : page_title,
        }
    )


def display(request):

    page_title = 'Liste des refugiés'

    return render(
        request,
        'fondation/refugees/display.html',
        {
            'page_title' : page_title,
        }
    )