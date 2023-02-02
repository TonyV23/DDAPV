from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required

from fondation.models import Donor, TypeAssistance
from fondation.forms import DonorForm
from fondation.filters import DonorFilter

@login_required(login_url ='login')
def index(request) :

    page_title = 'Aperçu sur les aides et dons'

    return render(
        request,
        'fondation/donations/index_employee.html',
        {
            'page_title' : page_title
        }
    )

@login_required(login_url ='login')
def donors_add(request) :
    assert isinstance(request, HttpRequest)
    page_title = 'Faire un don'
    donors = Donor.objects.all()

    if request.method == 'GET' :
        form = DonorForm()

    return render(
        request,
        'fondation/donations/add_donor_employee.html',
        {
            'page_title' : page_title,
            'donors' : donors,
            'form' : form,
        }
    )

@login_required(login_url ='login')
def donors_store(request) :
    if request.method == 'POST':
        form = DonorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Le (la) donateur (trice) a été enregistré avec succès !")
        else :
            messages.error(request, form.errors)
        return redirect('/donationsEmployee/display')

@login_required(login_url ='login')
def donors_edit(request, id) :
    assert isinstance(request, HttpRequest)
    page_title = 'Modifier l\'état du don'
    if request.method == 'GET':
        if id == 0:
            form = DonorForm()
        else:
            donor = Donor.objects.get(pk=id)
            form = DonorForm(instance=donor)
        return render(
            request,
            'fondation/donations/edit_donor_employee.html',
            {
                'form': form,
                'page_title' :page_title
            }
        )

@login_required(login_url ='login')
def donors_update(request, id) :
    if request.method == 'POST':
        if id == 0:
            form = DonorForm(request.POST)
        else:
            donor = Donor.objects.get(pk=id)
            form = DonorForm(request.POST, instance=donor)
        if form.is_valid():
            form.save()
        messages.success(request, "L'état du donateur a été modifié avec succès !")
        return redirect('/donationsEmployee/display')

@login_required(login_url ='login')
def donors_delete(request,id) :
    donors = Donor.objects.get(pk = id)
    donors.delete()
    messages.success(request,"Le (la) donateur (trice) a été supprimé avec succès !")
    return redirect('/donationsEmployee/display')


@login_required(login_url ='login')
def donors_display(request) :
    
    page_title = 'Liste des donateurs'
    donors = Donor.objects.all()
    
    filter = DonorFilter(request.GET, queryset = donors)
    donors = filter.qs

    return render(
        request,
        'fondation/donations/donor_display_employee.html',
        {
            'donors' : donors,
            'page_title' : page_title,
            'filter' : filter,
        }
    )

@login_required(login_url ='login')
def getAssistance(request):
    type_aid_id = request.GET.get('id_type_aide')
    type_assistances = TypeAssistance.objects.filter(type_aide_id = type_aid_id)
    return render(
        request,
        'fondation/donations/getAssistance.html',
        {
            'type_assistances': type_assistances
        }
    )