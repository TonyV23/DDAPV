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
    type_aide = MultiSelectField(choices=TypeHelpChoices, max_length=150)

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
    type_assistance = MultiSelectField(choices=TypeAssistChoices, max_length=150)

    description = models.CharField("Autres",max_length=500, help_text='reseignez autre type d\'assistance qui ne figure pas dans la liste', blank=True)
    
    date_given = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.camp+"  "+self.beneficiaire+"  "+self.type_assistance+"  "+self.description
