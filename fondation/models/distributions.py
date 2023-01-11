from django.db import models
from multiselectfield import MultiSelectField


from fondation.models import Person

class Distribution(models.Model) : 
    
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    
    TypeHelpChoices = (
        ('aide_en_nature','Aide en nature'),
        ('aide_en_espece','Aide en éspèce'),
        ('accompagnement_psychosocial','Accompagnement psychosocial'),
        ('accompagnement_medical','Accompagnement médical')
    )
    type_help = MultiSelectField(choices=TypeHelpChoices, max_length=150)
    description = models.CharField(max_length=500, help_text='décrivez le type de don et/ou aides que le bénéficiaire reçoit')
    date_given = models.DateField('date de distribution', auto_created=True)

    def __str__(self) -> str:
        return self.person+" "+self.type_help+" "+self.description+''+self.date_given

    class Meta : 
        constraints = [
            models.UniqueConstraint(
                fields = ['person', 'type_help', 'description','date_given'],
                name = 'unique_distribution'
            )
        ]

        ordering = ['-date_given']