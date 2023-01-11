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
    donor_type = models.CharField('donateur (trice)', choices=TypeDonor, max_length=50)
    donor_name = models.CharField('Nom', max_length=50, help_text="tapez votre nom / le nom de l'entreprise , de l'association ou de l'organisation", blank=True)

    TypeHelpChoices = (
        ('aide_en_nature','Aide en nature'),
        ('aide_en_espece','Aide en éspèce'),
        ('accompagnement_psychosocial','Accompagnement psychosocial'),
        ('accompagnement_medical','Accompagnement médical')
    )
    type_help = MultiSelectField(choices=TypeHelpChoices, max_length=150)

    description = models.CharField(max_length=500, help_text='décrivez le type de don et/ou aides que vous souhaitez donner à notre fondation',blank=True)

    donor_phone = PhoneField('Téléphone', help_text='ce numero de téléphone sera utilisé pour entrer en contact avec vous')
    donor_email = models.EmailField('email', help_text='cette addresse mail sera utilisée pour entrer en contact avec vous')

    donor_date_given = models.DateField(auto_created=True)

    def __str__(self) -> str:
        return self.donor_type+' '+self.donor_name+' '+self.type_help+' '+self.description+''+self.donor_phone+' '+self.donor_email+' '+self.donor_date_given

    class Meta :
        constraints = [
            models.UniqueConstraint(
                fields = ['donor_type','donor_name','type_help','description','donor_phone','donor_email','donor_date_given'],
                name = 'unique_donor'
            )            
        ]

        ordering = ['-donor_date_given']        