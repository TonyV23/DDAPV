from django.shortcuts import render


from fondation.models import Person, Donor, Camp, Distribution ,Province, Vulnerability, LevelStudy, MatiralStatus


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

    all_level_studies_list = getAllLevelStudiesListName()
    all_level_studies_occurence = getAllLevelStudiesOccurence()
    all_matiral_status_list = getAllMatiralStatusListName()
    all_matiral_status_occurence = getAllMatiralStatusOccurence()

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

        'all_level_studies_list' : all_level_studies_list,
        'all_level_studies_occurence' : all_level_studies_occurence,
        'all_matiral_status_list' : all_matiral_status_list,
        'all_matiral_status_occurence' :all_matiral_status_occurence,

    
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
        if get_all_provinces_ids_list[k] in get_all_provinces_person_ids_list :
            for l in range(0, len(get_all_provinces_person_ids_list)) :
                if get_all_provinces_person_ids_list[l] == get_all_provinces_ids_list[k] :
                    occurence_provinces = occurence_provinces +1
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


def getAllLevelStudiesListName() : 
    get_all_level_studies_ids =  LevelStudy.objects.values('niveau_etudes')
    get_all_level_studies_ids_list = []

    for i in range(0, len(get_all_level_studies_ids)) :
        get_all_level_studies_ids_list.append(list(get_all_level_studies_ids[i].values())[0])

    return get_all_level_studies_ids_list


def getAllLevelStudiesOccurence() :
    
    get_all_level_studies_ids =  LevelStudy.objects.values('id')
    get_all_level_studies_ids_list = []
    for i in range(0, len(get_all_level_studies_ids)) :
        get_all_level_studies_ids_list.append(list(get_all_level_studies_ids[i].values())[0])

    get_all_level_studies_refugees = Person.objects.values('le_niveau_etudes_id')
    get_all_level_studies_refugees_list = []
    for j in range(0, len(get_all_level_studies_refugees)) :
        get_all_level_studies_refugees_list.append(list(get_all_level_studies_refugees[j].values())[0])

    refugees_level_studies_dict = {}

    for k in range(0, len(get_all_level_studies_ids_list)) :
        occurence_level_studies = 0
        if get_all_level_studies_ids_list[k] in get_all_level_studies_refugees_list :
            for l in range(0, len(get_all_level_studies_refugees_list)) :
                if get_all_level_studies_refugees_list[l] == get_all_level_studies_ids_list[k] :
                    occurence_level_studies = +1
            refugees_level_studies_dict[get_all_level_studies_ids_list[k]] = occurence_level_studies

    return refugees_level_studies_dict    


def getAllMatiralStatusListName() :
    get_all_matiral_status_names =  MatiralStatus.objects.values('situation_matrimoniale')
    get_all_matiral_status_names_list = []

    for i in range(0, len(get_all_matiral_status_names)) :
        get_all_matiral_status_names_list.append(list(get_all_matiral_status_names[i].values())[0])

    return get_all_matiral_status_names_list


def getAllMatiralStatusOccurence() :
    get_all_matiral_status_ids = MatiralStatus.objects.values('id')
    get_all_matiral_status_ids_list = []
    for i in range(0, len(get_all_matiral_status_ids)) :
        get_all_matiral_status_ids_list.append(list(get_all_matiral_status_ids[i].values())[0])
    
    get_all_person_matiral_status_ids = Person.objects.values('situation_matrimoniale_id')
    get_all_person_matiral_status_ids_list = []
    for j in range(0, len(get_all_person_matiral_status_ids)) :
        get_all_person_matiral_status_ids_list.append(list(get_all_person_matiral_status_ids[j].values())[0])

    person_matiral_status = {}

    for k in range (0, len(get_all_matiral_status_ids_list)) :
        occurence_matiral_status = 0
        if get_all_matiral_status_ids_list[k] in get_all_person_matiral_status_ids_list :
            for l in range(0, len(get_all_person_matiral_status_ids_list)) :
                if get_all_person_matiral_status_ids_list[l] == get_all_matiral_status_ids_list[k] :
                    occurence_matiral_status =+ 1            
            person_matiral_status[get_all_matiral_status_ids_list[k]] = occurence_matiral_status
    
    return person_matiral_status
