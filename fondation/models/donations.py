from django.db import models

from multiselectfield import MultiSelectField
from phone_field import PhoneField

class Donation(models.Model) : 
    
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
    type_aide = MultiSelectField(choices=TypeHelpChoices, max_length=150)

    description = models.CharField(max_length=500, help_text='décrivez le type de don et/ou aides que vous souhaitez donner à notre fondation',blank=True)

    numero_de_telephone = PhoneField(help_text='ce numero de téléphone sera utilisé pour entrer en contact avec vous')
    adresse_mail = models.EmailField(help_text='cette addresse mail sera utilisée pour entrer en contact avec vous')

    donor_date_given = models.DateField(auto_created=True)

    def __str__(self) -> str:
        return self.type_donneur+' '+self.nom_du_donneur+' '+self.type_aide+' '+self.description+''+self.numero_de_telephone+' '+self.adresse_mail+' '+self.donor_date_given

    class Meta :
        constraints = [
            models.UniqueConstraint(
                fields = ['type_donneur','nom_du_donneur','type_aide','description','numero_de_telephone','adresse_mail','donor_date_given'],
                name = 'unique_donor'
            )            
        ]        