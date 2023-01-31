from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required

from fondation.forms import LevelStudyForm
from fondation.models import LevelStudy

@login_required(url ='login')
def index(request):
    
    page_title = "Aperçu sur les niveaux d'études"

    return render(
        request,
        'fondation/levelStudies/index.html',
        {
            'page_title' : page_title,
        }
    )

@login_required(url ='login')
def level_study_add(request) :
    assert isinstance(request, HttpRequest)
    page_title = "Ajouter niveau d'études"
    if request.method == 'GET' :
        form = LevelStudyForm ()

    return render(
        request,
        'fondation/levelStudies/add_level_studies.html',
        {
            'form': form,
            'page_title' : page_title,
        }
    )

@login_required(url ='login')
def level_study_store(request) :
    if request.method == 'POST':
        form = LevelStudyForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Le niveau d'études a été enregistré avec succès !")
        else :
            messages.error(request, form.errors)
        return redirect('/levelStudies/display')

@login_required(url ='login')
def level_study_edit(request, id) :
    assert isinstance(request, HttpRequest)
    page_title = 'Modifier le niveau d\'études'
    if request.method == 'GET':
        if id == 0:
            form = LevelStudyForm()
        else:
            level_study = LevelStudy.objects.get(pk=id)
            form = LevelStudyForm(instance=level_study)
        return render(
            request,
            'fondation/levelStudies/edit_level_study.html',
            {
                'form': form,
                'page_title' :page_title
            }
        )

@login_required(url ='login')
def level_study_update(request, id):
    if request.method == 'POST':
        if id == 0:
            form = LevelStudyForm(request.POST)
        else:
            level_studies = LevelStudy.objects.get(pk=id)
            form = LevelStudyForm(request.POST, instance=level_studies)
        if form.is_valid():
            form.save()
        messages.success(request, "Le niveau d'études a été modifié avec succès !")
        return redirect('/levelStudies/display')


@login_required(url ='login')
def level_study_delete(request, id):
    level_studies = LevelStudy.objects.get(pk = id)
    level_studies.delete()
    messages.success(request,"Le niveau d'études a été supprimé avec succès !")
    return redirect('/levelStudies/display')


@login_required(url ='login')
def display(request) :

    page_title = "Ajouter niveau d'études"
    level_studies = LevelStudy.objects.all()

    return render(
        request,
        'fondation/levelStudies/display.html',
        {
            'level_studies' : level_studies,
            'page_title' : page_title,
        }
    )