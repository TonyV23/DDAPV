from django.db import models
from phone_field import PhoneField

from fondation.models import Province, Commune, Vulnerability, LevelStudy, MatiralStatus

class Person (models.Model) :
    
    first_last_name = models.CharField('nom et prénom', max_length=30, help_text= 'tapez le nom et prénom')
    GenderType = models.TextChoices('Masculin', 'féminin')
    gender = models.CharField('sexe', choices=GenderType.choices, max_length=20)
    age = models.DateField('date de naissance')
    phone = PhoneField('numéro de téléphone', blank=True, help_text= 'tapez le numero de téléphone')
    father = models.CharField('nom et prenom du père',max_length=50,help_text='tapez le nom et le prenom du père')
    mother = models.CharField('nom et prenom de la mère',max_length=50,help_text='tapez le nom et le prenom du mère')

    province_name = models.ForeignKey(Province, on_delete=models.CASCADE)
    commune_name = models.ForeignKey(Commune, on_delete=models.CASCADE)
    zone_name = models.CharField('zone', max_length=20, help_text="tapez la zone d'origine")

    vulnerability_name = models.ForeignKey(Vulnerability, on_delete=models.CASCADE)
    level_study_name = models.ForeignKey(LevelStudy, on_delete=models.CASCADE)
    matiral_status_name = models.ForeignKey(MatiralStatus, on_delete=models.CASCADE)

    number_of_dependent_children =  models.PositiveIntegerField("nombre d'enfant(s) à sa charge")
    work_before_exile = models.CharField("fonction occupée avant l'exil", max_length=50, blank=True)

    date_joined = models.DateField("date d'arrivée",auto_created=True, editable=True)

    def __str__(self) -> str:
        return self.first_last_name+' '+self.gender+' '+self.age+' '+self.phone+' '+self.father+' '+self.mother+' '+self.province_name+' '+self.commune_name+' '+self.zone_name+' '+self.vulnerability_name+' '+self.level_study_name+' '+self.matiral_status_name+' '+self.number_of_dependent_children+' '+self.work_before_exile+''+self.date_joined

    class Meta : 

        constraints = [
            models.UniqueConstraint(
            fields = ['first_last_name','gender','age','phone','father','mother','province_name','commune_name','zone_name','vulnerability_name','level_study_name','matiral_status_name','number_of_dependent_children','work_before_exile'],
            name = 'unique_person'
            )
        ]
        ordering = ['-date_joined', 'first_last_name']