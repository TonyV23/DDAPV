"""ddapv URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from fondation.views import home, refugees, donations, vulnerabilities, address, level_studies, matiral_status, distributions, camp

urlpatterns = [
    path('dashboard/', home.index, name ='dashboard'),

    
    # refugees urls

    path ('refugees/', refugees.index, name = 'refugees_overview'),
    path ('refugees/refugees_add/', refugees.refugees_add, name ='refugees_add'),
    path ('refugees/refugees_store/', refugees.refugees_store, name ='refugees_store'),
    path ('refugees/refugees_edit/<int:id>', refugees.refugees_edit, name ='refugees_edit'),
    path ('refugees/refugees_update/<int:id>', refugees.refugees_update, name ='refugees_update'),
    path ('refugees/refugees_delete/<int:id>', refugees.refugees_delete, name ='refugees_delete'),
    path ('refugees/display/', refugees.refugees_display, name ='refugees_display'),
    path ('refugees/refugees_display/<int:id>', refugees.refugees_display_by_id, name = 'refugees_display_by_id'),
    path ('refugees/getCommunes', refugees.getCommunes, name = 'refugees_getCommunes'),

    
    # donations urls
    
    path ('donations/', donations.index, name = 'donations_overview'),
    path ('donations/donors_add', donations.donors_add, name = 'donors_add'),
    path ('donations/donors_store', donations.donors_store, name = 'donors_store'),
    path ('donations/donors_edit/<int:id>', donations.donors_edit, name = 'donors_edit'),
    path ('donations/donors_update/<int:id>', donations.donors_update, name = 'donors_update'),
    path ('donations/donors_delete/<int:id>', donations.donors_delete, name = 'donors_delete'),
    path ('donations/display', donations.donors_display, name = 'donors_display'),
    

    
    # vulnerabilities urls 
    
    path ('vulnerabilities/', vulnerabilities.index, name = 'vulnerabilities_overview'),
    path ('vulnerabilities/vulnerabilities_add', vulnerabilities.vulnerabilities_add, name = 'vulnerabilities_add'),
    path ('vulnerabilities/vulnerabilities_store', vulnerabilities.vulnerabilities_store, name = 'vulnerabilities_store'),
    path ('vulnerabilities/vulnerabilities_edit/<int:id>', vulnerabilities.vulnerabilities_edit, name = 'vulnerabilities_edit'),
    path ('vulnerabilities/vulnerabilities_update/<int:id>', vulnerabilities.vulnerabilities_update, name = 'vulnerabilities_update'),
    path ('vulnerabilities/vulnerabilities_delete/<int:id>', vulnerabilities.vulnerabilities_delete, name = 'vulnerabilities_delete'),
    path ('vulnerabilities/display', vulnerabilities.display, name = 'vulnerabilities_display'),

    
    # address urls

    path ('address/', address.index, name = 'address_overview'),
    
    path ('address/add_province', address.add_province, name = 'address_add_province'),
    path ('address/address_store_province', address.store_province, name = 'address_store_province'),
    path ('address/address_province_edit/<int:id>', address.province_edit, name = 'address_province_edit'),
    path ('address/address_province_update/<int:id>', address.province_update, name = 'address_province_update'),
    path ('address/address_province_delete/<int:id>', address.province_delete, name = 'address_province_delete'),
    path ('address/address_view_provinces', address.view_provinces, name = 'view_provinces'),
    
    path ('address/add_commune', address.add_commune, name = 'address_add_commune'),
    path ('address/address_store_commune', address.store_commune, name = 'address_store_commune'),
    path ('address/address_commune_edit/<int:id>', address.commune_edit, name = 'address_commune_edit'),
    path ('address/address_commune_update/<int:id>', address.commune_update, name = 'address_commune_update'),
    path ('address/address_commune_delete/<int:id>', address.commune_delete, name = 'address_commune_delete'),
    path ('address/address_view_communes', address.view_communes, name = 'view_communes'),
    
    
    # level studies urls
    
    path ('levelStudies/', level_studies.index, name = 'level_studies_overview'),
    path ('levelStudies/level_study_add', level_studies.level_study_add, name = 'level_studies_add'),
    path ('levelStudies/level_study_store', level_studies.level_study_store, name = 'level_studies_store'),
    path ('levelStudies/level_study_edit/<int:id>', level_studies.level_study_edit, name = 'level_studies_edit'),
    path ('levelStudies/level_study_store/<int:id>', level_studies.level_study_update, name = 'level_studies_update'),
    path ('levelStudies/level_study_delete/<int:id>', level_studies.level_study_delete, name = 'level_studies_delete'),
    path ('levelStudies/display', level_studies.display, name = 'level_studies_display'),


    # matiral status urls

    path('matiralStatus/', matiral_status.index, name = 'matiral_status_overview'),
    path('matiralStatus/matiral_status_add', matiral_status.matiral_status_add, name = 'matiral_status_add'),
    path('matiralStatus/matiral_status_store', matiral_status.matiral_status_store, name = 'matiral_status_store'),
    path('matiralStatus/matiral_status_edit/<int:id>', matiral_status.matiral_status_edit, name = 'matiral_status_edit'),
    path('matiralStatus/matiral_status_update/<int:id>', matiral_status.matiral_status_update, name = 'matiral_status_update'),
    path('matiralStatus/matiral_status_delete/<int:id>', matiral_status.matiral_status_delete, name = 'matiral_status_delete'),
    path('matiralStatus/display', matiral_status.display, name = 'matiral_status_display'),


    # distribution urls

    path ('distributions/', distributions.index, name = 'distributions_overview'),
    path ('distributions/distribution_add', distributions.distribution_add, name = 'distributions_add'),
    path ('distributions/distribution_store', distributions.distribution_store, name = 'distributions_store'),
    path ('distributions/distribution_edit/<int:id>', distributions.distribution_edit, name = 'distributions_edit'),
    path ('distributions/distribution_update/<int:id>', distributions.distribution_update, name = 'distributions_update'),
    path ('distributions/distribution_delete/<int:id>', distributions.distribution_delete, name = 'distributions_delete'),
    path ('distributions/display', distributions.display, name = 'distributions_display'),
    path ('distributions/distribution_display_by_id/<int:id>', distributions.display_by_id, name = 'distribution_display_by_id'),
    path ('distributions/getBeneficiaire', distributions.getBeneficiaire, name = 'distributions_getBeneficiaire'),


    # camps urls

    path ('camps/', camp.index, name = 'camps_overview'),
    path('camps/camps_add', camp.camps_add, name='camps_add'),
    path('camps/camps_store', camp.camps_store, name='camps_store'),
    path('camps/camps_edit/<int:id>', camp.camps_edit, name='camps_edit'),
    path('camps/camps_update/<int:id>', camp.camps_update, name='camps_update'),
    path('camps/camps_delete/<int:id>', camp.camps_delete, name='camps_delete'),
    path('camps/camps_display', camp.camps_display, name='camps_display'),
    
]
