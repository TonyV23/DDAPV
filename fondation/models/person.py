from django.db import models
from phone_field import PhoneField

from fondation.models import Province, Commune, Vulnerability, LevelStudy, MatiralStatus

class Person (models.Model) :
    
    nom = models.CharField(max_length=30, help_text= 'tapez le nom de famille')
    prenom = models.CharField(max_length=30, help_text= 'tapez le prenom')
    GenderType = (
            ('M','Masculin'),('F', 'féminin')
        )
    sexe = models.CharField(choices=GenderType, max_length=20)
    age = models.DateField('date de naissance')
    numero_de_telephone = PhoneField(blank=True, help_text= 'tapez le numero de téléphone')
    nom_prenom_du_pere = models.CharField(max_length=50,help_text='tapez le nom et le prenom du père')
    nom_prenom_de_la_mere = models.CharField(max_length=50,help_text='tapez le nom et le prenom du mère')

    nom_de_la_province = models.ForeignKey(Province, on_delete=models.CASCADE, help_text="province d'origine")
    nom_de_la_commune = models.ForeignKey(Commune, on_delete=models.CASCADE, help_text="commune d'origine")
    nom_de_la_zone = models.CharField('Colline', max_length=20, help_text="zone d'origine")

    la_vulnerabilite = models.ForeignKey(Vulnerability, on_delete=models.CASCADE, help_text="sélectionez sa situation de vulnerabilité")
    le_niveau_etudes = models.ForeignKey(LevelStudy, on_delete=models.CASCADE, help_text="sélectionez son niveau d'études")
    situation_matrimoniale = models.ForeignKey(MatiralStatus, on_delete=models.CASCADE, help_text="sélectionez sa situation de situation matrimoniale", verbose_name='statut matrimonial')

    nombre_enfants =  models.PositiveIntegerField(help_text="renseignez le nombre d'enfants à sa charge")
    fonction = models.CharField(max_length=50, blank=True)

    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return self.nom+'--'+self.prenom+'--'+self.sexe

    class Meta : 

        constraints = [
            models.UniqueConstraint(
            fields = ['nom','prenom','sexe','age','numero_de_telephone','nom_prenom_du_pere','nom_prenom_de_la_mere','nom_de_la_province','nom_de_la_commune','nom_de_la_zone','la_vulnerabilite','le_niveau_etudes','situation_matrimoniale','nombre_enfants','fonction', 'date_joined'],
            
            name = 'unique_person'
            )
        ]