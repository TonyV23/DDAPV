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
from fondation.views import home, refugees, donations, vulnerabilities, address, level_studies, matiral_status, distributions

urlpatterns = [
    path('dashboard/', home.index, name ='dashboard'),

    
    # refugees urls

    path('refugees/', refugees.index, name = 'refugees_overview'),
    path('refugees/add/', refugees.add, name ='refugees_add'),
    path('refugees/display/', refugees.display, name ='refugees_display'),

    
    # donations urls
    
    path ('donations/', donations.index, name = 'donations_overview'),
    path ('donations/donors_add', donations.donors_add, name = 'donors_add'),
    path ('donations/donors_store', donations.donors_store, name = 'donors_store'),
    path ('donations/donors_edit/<int:id>', donations.donors_edit, name = 'donoros_edit'),
    path ('donations/donors_update/<int:id>', donations.donors_update, name = 'donoros_update'),
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
    path ('distributions/', distributions.add_distribution, name = 'distributions_add'),
    path ('distributions/', distributions.display, name = 'distributions_display'),
]
