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
    all_province_occurence = getProvinceOccurence()
    all_vulnerabilities_occurence = getVulnerabilitiesOccurence()


    variable = {

        'page_title' : page_title,
        
        'total_refugees' : total_refugees,
        'total_camps' : total_camps,
        'total_donors' : total_donors,
        'total_distributions' : total_distributions,
        'all_province_list': all_province_list,
        'all_vulnerabilities_list' : all_vulnerabilities_list,
        'all_province_occurence' : all_province_occurence,
        'all_vulnerabilities_occurence' :all_vulnerabilities_occurence,
    
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


def getProvinceOccurence() :
    get_all_provinces_ids = Province.objects.values('id')
    get_all_provinces_ids_list = []

    for i in range(0, len(get_all_provinces_ids)) :
        get_all_provinces_ids_list.append(list(get_all_provinces_ids[i].values())[0]) 

    get_all_provinces_person_ids = Person.objects.values('nom_de_la_province_id')
    get_all_provinces_person_ids_list = []

    for j in range(0, len(get_all_provinces_person_ids)) :
        get_all_provinces_person_ids_list.append(list(get_all_provinces_person_ids[j].values())[0])

    province_person_dict = {}

    for k in range(0, len(get_all_provinces_ids_list)) :
        occurence_provinces = 0
        if get_all_provinces_ids_list[k] in get_all_provinces_person_ids :
            for l in range(0, len(get_all_provinces_person_ids)) :
                if get_all_provinces_person_ids[l] == get_all_provinces_ids_list[k] :
                    occurence_provinces = +1
            province_person_dict [get_all_provinces_ids_list[k]] = occurence_provinces

    return province_person_dict


def getVulnerabilitiesOccurence() :
    get_all_vulnerabilities_ids = Vulnerability.objects.values('id')
    get_all_vulnerabilities_ids_list = []

    for i in range(0, len(get_all_vulnerabilities_ids)) :
        get_all_vulnerabilities_ids_list.append(list(get_all_vulnerabilities_ids[i].values())[0])

    get_all_person_vulnerabilities_ids = Person.objects.values('la_vulnerabilite_id')
    get_all_person_vulnerabilities_ids_list = []

    for j in range(0, len(get_all_person_vulnerabilities_ids)) :
        get_all_person_vulnerabilities_ids_list.append(list(get_all_person_vulnerabilities_ids[j].values())[0])
    
    persons_vulnerabilities_dict = {}

    for k in range(0, len(get_all_vulnerabilities_ids_list)) :
        occurence_vulnerabilities = 0
        if get_all_vulnerabilities_ids_list[k] in get_all_person_vulnerabilities_ids_list :
            for l in range(0, len(get_all_person_vulnerabilities_ids_list)) :
                if get_all_person_vulnerabilities_ids_list[l] == get_all_vulnerabilities_ids_list[k] :
                    occurence_vulnerabilities = +1
            persons_vulnerabilities_dict[get_all_vulnerabilities_ids_list[k]] = occurence_vulnerabilities

    return persons_vulnerabilities_dict    

