from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpRequest

def index(request) :
    page_title = 'Fondation Evan You'
    template = 'fondation/visitor/index.html'


    variable = {

        'page_title' : page_title,
    }

    return render(
        request,
        template_name = template,
        context = variable
    )