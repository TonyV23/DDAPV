from django.db import models

from phone_field import PhoneField

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

    TypeHelpChoices = (
        ('aide_en_nature','Aide en nature'),
        ('aide_en_espece','Aide en éspèce'),
        ('accompagnement_psychosocial','Accompagnement psychosocial'),
        ('accompagnement_medical','Accompagnement médical')
    )
    type_aide = models.CharField(choices=TypeHelpChoices, max_length=150)

    TypeAssistChoices = (
        ('vivre_alimentaire','Vivre alimentaire'),
        ('ustenciles_de_cuisines','Ustenciles de cuisines'),
        ('eau_potable','Eau potable'),
        ('briquettes','briquettes'),
        ('kit_de_dignite','Kit de dignité pour les femmes'),
        ('vetements','Les Vêtements'),
        ('kit_scolaire','Kit Scolaire'),
        ('medicaments','Médicaments / Soins médicaux'),
        ('fonds_de_roulements','Fonds de roulements de micro-projets'),
        ('enseignements_de_metiers','Enseignements de métiers'),
        ('reunification_familliale','Réunification familliale'),
        ('reinstallation','Réinstallation'),
        ('kinesitherapie','kinésithérapie'),
    )

    type_assistance = models.CharField(choices=TypeAssistChoices, max_length=150)

    numero_de_telephone = PhoneField(help_text='ce numero de téléphone sera utilisé pour entrer en contact avec vous')

    adresse_mail = models.EmailField(help_text='cette addresse mail sera utilisée pour entrer en contact avec vous')

    description = models.TextField(max_length=500, help_text='décrivez le type de don et/ou aides que vous souhaitez donner à notre fondation',blank=True)

    donor_date_given = models.DateTimeField(auto_now_add=True)
