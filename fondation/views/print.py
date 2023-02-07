from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from fondation.models import Donor, Distribution

@login_required(login_url ='login')
def printDonors(request) :

    page_title = 'Impression des donateurs'
    template = 'fondation/donations/print.html'

    donors = Donor.objects.all()


    variable  = {
            'page_title' : page_title,
            'donors' : donors
        }

    return render(
        request,
        template_name = template,
        context = variable 
    )

@login_required(login_url ='login')
def printDistributions(request) :

    page_title = 'Impression des bénéficiaires'
    template = 'fondation/distributions/print.html'

    distributions = Distribution.objects.all()


    variable  = {
            'page_title' : page_title,
            'distributions' : distributions
        }

    return render(
        request,
        template_name = template,
        context = variable 
    )