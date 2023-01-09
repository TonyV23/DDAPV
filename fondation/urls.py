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
from fondation.views import home, refugees, donations, vulnerabilities, address, level_studies

urlpatterns = [
    path('dashboard/', home.index, name ='dashboard'),

    
    # refugees urls

    path('refugees/', refugees.index, name = 'refugees_overview'),
    path('refugees/add/', refugees.add, name ='refugees_add'),
    path('refugees/display/', refugees.display, name ='refugees_display'),

    
    # donations urls
    
    path ('donations/', donations.index, name = 'donations_overview'),
    path ('donations/add_type', donations.add_type, name = 'donations_types_add'),
    path ('donations/add_donation_help', donations.add_donation_help, name = 'donations_donations_help_add'),
    path ('donations/display', donations.display, name = 'donations_display'),

    
    # vulnerabilities urls 
    
    path('vulnerabilities/', vulnerabilities.index, name = 'vulnerabilities_overview'),
    path('vulnerabilities/add_type', vulnerabilities.add_vulnerabilities_type, name = 'vulnerabilities_add_type'),
    path('vulnerabilities/add_value', vulnerabilities.add_vulnerabilities_value, name = 'vulnerabilities_add_value'),
    path ('vulnerabilities/display', vulnerabilities.display, name = 'vulnerabilities_display'),

    
    # address urls

    path ('address/', address.index, name = 'address_overview'),
    path ('address/add_province', address.add_province, name = 'address_add_province'),
    path ('address/add_commune', address.add_commune, name = 'address_add_commune'),
    path ('address/add_zone', address.add_zone, name = 'address_add_zone'),
    path ('address/view_provinces', address.view_provinces, name = 'view_provinces'),
    path ('address/view_communes', address.view_communes, name = 'view_communes'),
    path ('address/view_zones', address.view_zones, name = 'view_zones'),
    path ('address/display', address.display, name = 'address_display'),

    
    # level studies urls
    
    path ('levelStudies/', level_studies.index, name = 'level_studies_overview'),
    path ('levelStudies/add', level_studies.add_level_study, name = 'level_studies_add'),
    path ('levelStudies/display', level_studies.display, name = 'level_studies_display'),


]
