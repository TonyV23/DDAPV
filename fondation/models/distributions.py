from django.db import models
from multiselectfield import MultiSelectField


from fondation.models import Camp, Person

class Distribution(models.Model) : 
    
    camp = models.ForeignKey(Camp, on_delete=models.CASCADE, help_text="sélectionez le camp du refugié (e)")
    beneficiaire = models.ForeignKey(Person, on_delete=models.CASCADE ,help_text="sélectionez le (la) bénéficiaire", unique_for_date='date_given')
    
    TypeHelpChoices = (
        ('aide_en_nature','Aide en nature'),
        ('aide_en_espece','Aide en éspèce'),
        ('accompagnement_psychosocial','Accompagnement psychosocial'),
        ('accompagnement_medical','Accompagnement médical')
    )
    type_assistance = MultiSelectField(choices=TypeHelpChoices, max_length=150)
    description = models.CharField(max_length=500, help_text='décrivez le type de don et/ou aides que le bénéficiaire reçoit')
    date_given = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.camp+" "+self.beneficiaire+" "+self.type_assistance+" "+self.description+''+self.date_given
