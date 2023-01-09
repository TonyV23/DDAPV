from django.shortcuts import render


def index (request) :
    
    page_title = 'Aperçu sur les vulnerabilités'

    return render(
        request,
        'fondation/vulnerabilities/index.html',
        {
            'page_title' : page_title
        }
    )


def add_vulnerabilities_type(request) :

    page_title = 'Nouveau type de vulnerabilités'

    return render(
        request,
        'fondation/vulnerabilities/vulnerabilities_type.html',
        {
            'page_title' : page_title
        }
    )


def add_vulnerabilities_value(request) :

    page_title = 'Nouvelle vulnerabilité'

    return render(
        request,
        'fondation/vulnerabilities/vulnerabilities_value.html',
        {
            'page_title' : page_title
        }
    )

def display (request) :
    
    page_title = 'Liste des vulnerabilités'

    return render(
        request,
        'fondation/vulnerabilities/display.html',
        {
            'page_title' : page_title
        }
    )