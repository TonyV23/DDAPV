from django.db import models
from phone_field import PhoneField

from fondation.models import TypeAide, TypeAssistance

class Donor(models.Model) : 

    TypeDonor = (
        ('org', 'Organisation'),
        ('entrp', 'Entreprise'),
        ('assoc', 'Association'),
        ('part', 'Particulier'),
        ('anonym','Rester anonyme')
    )
    type_donneur = models.CharField(choices=TypeDonor, max_length=50)

    nom_du_donneur = models.CharField(max_length=50, help_text="tapez votre nom / le nom de l'entreprise , de l'association ou de l'organisation", blank=True)

    type_aide = models.ForeignKey(TypeAide, on_delete=models.CASCADE)

    type_assistance = models.ForeignKey(TypeAssistance, on_delete=models.CASCADE)

    numero_de_telephone = PhoneField(help_text='ce numero de téléphone sera utilisé pour entrer en contact avec vous')

    adresse_mail = models.EmailField(help_text='cette addresse mail sera utilisée pour entrer en contact avec vous')

    description = models.TextField(max_length=500, help_text='décrivez le type de don et/ou aides que vous souhaitez donner à notre fondation',blank=True)

    donor_date_given = models.DateTimeField(auto_now_add=True)
