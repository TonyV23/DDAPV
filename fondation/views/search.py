from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpRequest

def index (request) :

    page_title = 'Rechercher'
    template = 'fondation/search/index.html'
    
    variable = {
        
        'page_title' : page_title
        
    }

    return render (
        request,
        template_name = template,
        context = variable
    )