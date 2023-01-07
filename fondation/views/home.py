from django.shortcuts import render


def index(request) :

    page_title = 'Accueil'


    return render(
        request,
        'fondation/home/index.html',
        {
            'page_title' : page_title
        }
    )
