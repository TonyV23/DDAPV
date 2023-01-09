from django.shortcuts import render


def index(request):
    
    page_title = "Aperçu sur les niveaux d'études"

    return render(
        request,
        'fondation/levelStudies/index.html',
        {
            'page_title' : page_title,
        }
    )

def add_level_study(request) :

    page_title = "Ajouter niveau d'études"

    return render(
        request,
        'fondation/levelStudies/add_level_studies.html',
        {
            'page_title' : page_title,
        }
    )


def display(request) :

    page_title = "Ajouter niveau d'études"

    return render(
        request,
        'fondation/levelStudies/add_level_studies.html',
        {
            'page_title' : page_title,
        }
    )