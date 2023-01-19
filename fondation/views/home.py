from django.shortcuts import render



from fondation.models import Person, Donor, Camp, Distribution


def index(request) :

    page_title = 'Tableau de Bord'
    template = 'fondation/home/index.html'

    total_refugees = Person.objects.count()
    total_camps = Camp.objects.count()
    total_donors = Donor.objects.count()
    total_distributions = Distribution.objects.count()





    variable = {

        'page_title' : page_title,
        
        'total_refugees' : total_refugees,
        'total_camps' : total_camps,
        'total_donors' : total_donors,
        'total_distributions' : total_distributions,
    
    }

    return render(
        request,
        template_name = template,
        context = variable
    )
