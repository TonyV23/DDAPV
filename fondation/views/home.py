from django.shortcuts import render


from fondation.models import Person, Donor, Camp, Distribution ,Province, Vulnerability


def index(request) :

    page_title = 'Tableau de Bord'
    template = 'fondation/home/index.html'

    total_refugees = Person.objects.count()
    total_camps = Camp.objects.count()
    total_donors = Donor.objects.count()
    total_distributions = Distribution.objects.only('beneficiaire_id').count()

    all_province_list = getAllProvinceListName()
    all_vulnerabilities_list = getAllVulnerabilitiesListName()


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


def getAllProvinceListName() :
    get_all_provinces_name = Province.objects.values('nom_de_la_province')
    get_all_provinces_name_list = []

    for i in range(0, len(get_all_provinces_name)) :
        get_all_provinces_name_list.append(list(get_all_provinces_name[i].values())[0])
    
    return get_all_provinces_name_list


def getAllVulnerabilitiesListName():
    get_all_vulnerabilities_name = Vulnerability.objects.values('vulnerabilite')
    get_all_vulnerabilities_name_list = []

    for i in range (0, len(get_all_vulnerabilities_name)) :
        get_all_vulnerabilities_name_list.append(list(get_all_vulnerabilities_name[i].values())[0])

    return get_all_vulnerabilities_name_list