from django.shortcuts import render
from django.db.models import Count
from django.contrib.auth.decorators import login_required

from fondation.models import Person, Donor, Distribution ,Province, Vulnerability, LevelStudy, MatiralStatus
from fondation.decorators import admin_only

@login_required(login_url ='login')
def index(request) :

    page_title = 'Tableau de Bord'
    template = 'fondation/home/index_employee.html'

    total_refugees = Person.objects.count()
    total_donors = Donor.objects.count()
    total_distributions = Distribution.objects.only('beneficiaire_id').count()

    
    refugees_arrived_per_day = getRefugeesArrivedPerDay()

    variable = {

        'page_title' : page_title,
        
        'total_refugees' : total_refugees,
        'total_donors' : total_donors,
        'total_distributions' : total_distributions,
    
        'refugees_arrived_per_day' : refugees_arrived_per_day,

    }

    return render(
        request,
        template_name = template,
        context = variable
    )


def getRefugeesArrivedPerDay() :
    refugees_arrived_per_day = Person.objects.extra(select={'day': 'date( date_joined )'}).values('day').annotate(available=Count('date_joined'))
    
    return refugees_arrived_per_day
    get_all_provinces_ids = Province.objects.values('id')
    get_all_provinces_ids_list = []

    for i in range(0, len(get_all_provinces_ids)) :
        get_all_provinces_ids_list.append(list(get_all_provinces_ids[i].values())[0]) 

    province_person_dict = {}

    for k in get_all_provinces_ids_list :
        get_all_provinces_names = Province.objects.filter(pk = k).values('nom_de_la_province')

        for i in range(0, len(get_all_provinces_names)) :
            get_all_provinces_name = list(get_all_provinces_names[i].values())[0]
        occurence_provinces = Person.objects.filter(nom_de_la_province_id = k).count()
        province_person_dict [get_all_provinces_name] = occurence_provinces

    return province_person_dict