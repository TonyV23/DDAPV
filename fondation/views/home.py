from django.shortcuts import render
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from fondation.models import Person, Donor, Distribution ,Province, Vulnerability, LevelStudy, MatiralStatus
from fondation.decorators import admin_only

@login_required(login_url ='login')
@admin_only
def index(request) :

    page_title = 'Tableau de Bord'
    template = 'fondation/home/index.html'

    total_refugees = Person.objects.count()
    total_donors = Donor.objects.count()
    total_distributions = Distribution.objects.only('beneficiaire_id').count()
    total_employees = User.objects.filter(is_superuser=False).count()

    
    all_province_occurence = getProvinceOccurence()
    all_vulnerabilities_occurence = getVulnerabilitiesOccurence()

    all_level_studies_occurence = getAllLevelStudiesOccurence()
    all_matiral_status_occurence = getAllMatiralStatusOccurence()

    masculine_gender_occurence = getMasculineOccurence()
    feminine_gender_occurence = getFeminineOccurence()

    organization_occurence = getOrganizationOccurence()
    entreprise_occurence = getEntrepriseOccurence()
    association_occurence = getAssociationOccurence()
    particulier_occurence = getParticulierOccurence()
    anonyme_occurence = getAnonymOccurence() 

    refugees_arrived_per_day = getRefugeesArrivedPerDay()

    variable = {

        'page_title' : page_title,
        
        'total_refugees' : total_refugees,
        'total_donors' : total_donors,
        'total_distributions' : total_distributions,
        'total_employees' :total_employees,
        

        'all_province_occurence' : all_province_occurence,
        'all_vulnerabilities_occurence' :all_vulnerabilities_occurence,

        'all_level_studies_occurence' : all_level_studies_occurence,
        'all_matiral_status_occurence' :all_matiral_status_occurence,

        'masculine_gender_occurence' : masculine_gender_occurence,
        'feminine_gender_occurence' : feminine_gender_occurence,

        'organization_occurence' : organization_occurence,
        'entreprise_occurence' : entreprise_occurence,
        'association_occurence' : association_occurence,
        'particulier_occurence' : particulier_occurence,
        'anonyme_occurence' : anonyme_occurence,

        'refugees_arrived_per_day' : refugees_arrived_per_day,

    }

    return render(
        request,
        template_name = template,
        context = variable
    )


def getProvinceOccurence() :
    get_all_provinces_ids = Province.objects.values('id')
    get_all_provinces_ids_list = []

    for i in range(0, len(get_all_provinces_ids)) :
        get_all_provinces_ids_list.append(list(get_all_provinces_ids[i].values())[0]) 

    province_person_dict = {}

    for k in get_all_provinces_ids_list :
        get_all_provinces_names = Province.objects.filter(pk = k).values('nom_de_la_province')
        get_all_provinces_name = ""
        
        for i in range(0, len(get_all_provinces_names)) :
            get_all_provinces_name = list(get_all_provinces_names[i].values())[0]
            occurence_provinces = 0
            occurence_provinces = Person.objects.filter(nom_de_la_province_id = k).count()

            province_person_dict [get_all_provinces_name] = occurence_provinces

    return province_person_dict


def getVulnerabilitiesOccurence() :
    get_all_vulnerabilities_ids = Vulnerability.objects.values('id')
    get_all_vulnerabilities_ids_list = []

    for i in range(0, len(get_all_vulnerabilities_ids)) :
        get_all_vulnerabilities_ids_list.append(list(get_all_vulnerabilities_ids[i].values())[0])

    persons_vulnerabilities_dict = {}

    for k in get_all_vulnerabilities_ids_list :
        get_vulnerabilites_names = Vulnerability.objects.filter(pk = k).values('vulnerabilite')

        get_vulnerabilites_name = ""

        for i in range(0, len(get_vulnerabilites_names)) :
            get_vulnerabilites_name = list(get_vulnerabilites_names[i].values())[0]
        occurence_vulnerabilite = 0
        occurence_vulnerabilite = Person.objects.filter(la_vulnerabilite_id = k).count()
        
        persons_vulnerabilities_dict [get_vulnerabilites_name] = occurence_vulnerabilite
        
    return persons_vulnerabilities_dict    


def getAllLevelStudiesOccurence() :
    
    get_all_level_studies_ids =  LevelStudy.objects.values('id')
    get_all_level_studies_ids_list = []
    
    for i in range(0, len(get_all_level_studies_ids)) :
        get_all_level_studies_ids_list.append(list(get_all_level_studies_ids[i].values())[0])

    refugees_level_studies_dict = {}

    for k in get_all_level_studies_ids_list :
        get_all_level_studies_names = LevelStudy.objects.filter(pk = k).values('niveau_etudes')
        get_level_studies_name = ""

        for i in range (0, len(get_all_level_studies_names)) :
            get_level_studies_name = list(get_all_level_studies_names[i].values())[0]
            occurence_level_studies = 0
            occurence_level_studies = Person.objects.filter(le_niveau_etudes_id = k).count()

            refugees_level_studies_dict[get_level_studies_name] = occurence_level_studies

    return refugees_level_studies_dict    


def getAllMatiralStatusOccurence() :
    get_all_matiral_status_ids = MatiralStatus.objects.values('id')
    get_all_matiral_status_ids_list = []
    for i in range(0, len(get_all_matiral_status_ids)) :
        get_all_matiral_status_ids_list.append(list(get_all_matiral_status_ids[i].values())[0])
    
    
    person_matiral_status = {}

    for k in get_all_matiral_status_ids_list :
        get_all_matiral_status_names = MatiralStatus.objects.filter(pk=k).values('situation_matrimoniale')
        get_all_matiral_status_name = ""

        for i in range(0, len(get_all_matiral_status_names)) :
            get_all_matiral_status_name = list(get_all_matiral_status_names[i].values())[0]
            occurence_matiral_status = 0
            occurence_matiral_status = Person.objects.filter(situation_matrimoniale_id = k).count()
            person_matiral_status[get_all_matiral_status_name] = occurence_matiral_status
    
    return person_matiral_status


def getFeminineOccurence() :
    feminine_gender_occurence = Person.objects.values('sexe').filter(sexe ='F').annotate(feminine_gender = Count('sexe'))
    feminine_gender_occurence_list = []
    for i in range(0,len(feminine_gender_occurence)) :
        feminine_gender_occurence_list.append(list(feminine_gender_occurence[i].values())[1])
    
    return feminine_gender_occurence_list


def getMasculineOccurence() :
    masculine_gender_occurence = Person.objects.values('sexe').filter(sexe ='M').annotate(masculine_gender = Count('sexe'))
    masculine_gender_occurence_list = []
    for i in range(0,len(masculine_gender_occurence)) :
        masculine_gender_occurence_list.append(list(masculine_gender_occurence[i].values())[1])
    
    return masculine_gender_occurence_list


def getOrganizationOccurence() : 
    organization_occurence = Donor.objects.values('type_donneur').filter(type_donneur='org').annotate(organization = Count('type_donneur'))
    organization_occurence_list = []
    for i in range (0, len(organization_occurence)) :
        organization_occurence_list.append(list(organization_occurence[i].values())[1])
    
    return organization_occurence_list


def getEntrepriseOccurence() : 
    entreprise_occurence = Donor.objects.values('type_donneur').filter(type_donneur='entrp').annotate(entreprise = Count('type_donneur'))
    entreprise_occurence_list = []
    for i in range (0, len(entreprise_occurence)) :
        entreprise_occurence_list.append(list(entreprise_occurence[i].values())[1])
    
    return entreprise_occurence_list


def getAssociationOccurence() : 
    association_occurence = Donor.objects.values('type_donneur').filter(type_donneur='assoc').annotate(association = Count('type_donneur'))
    association_occurence_list = []
    for i in range (0, len(association_occurence)) :
        association_occurence_list.append(list(association_occurence[i].values())[1])
    
    return association_occurence_list


def getParticulierOccurence() : 
    particulier_occurence = Donor.objects.values('type_donneur').filter(type_donneur='part').annotate(particulier = Count('type_donneur'))
    particulier_occurence_list = []
    for i in range (0, len(particulier_occurence)) :
        particulier_occurence_list.append(list(particulier_occurence[i].values())[1])
    
    return particulier_occurence_list


def getAnonymOccurence() : 
    anonym_occurence = Donor.objects.values('type_donneur').filter(type_donneur='anonym').annotate(anonym = Count('type_donneur'))
    anonym_occurence_list = []
    for i in range (0, len(anonym_occurence)) :
        anonym_occurence_list.append(list(anonym_occurence[i].values())[1])
    
    return anonym_occurence_list


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