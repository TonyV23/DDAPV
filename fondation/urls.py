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
from fondation.views import home, refugees, donations

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
    
]
