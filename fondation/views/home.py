from django.shortcuts import render


def index(request) :

    page_title = 'Tableau de Bord'


    return render(
        request,
        'fondation/home/index.html',
        {
            'page_title' : page_title
        }
    )
