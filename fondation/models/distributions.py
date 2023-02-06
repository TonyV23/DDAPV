from django.db import models
from djmoney.models.fields import MoneyField

from fondation.models import Province, Commune, Person, TypeAide, TypeAssistance

class Distribution(models.Model) : 
    
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    commune =  models.ForeignKey(Commune, on_delete=models.CASCADE)
    zone =  models.CharField("Colline",max_length=50)
    beneficiaire = models.ForeignKey(Person, on_delete=models.CASCADE ,help_text="sélectionez le (la) bénéficiaire", unique_for_date='date_given')
    
    type_aide = models.ForeignKey(TypeAide, on_delete=models.CASCADE)
    type_assistance = models.ForeignKey(TypeAssistance, on_delete=models.CASCADE)
    montant = MoneyField(max_digits=14, decimal_places=2, null=True, default_currency='BIF')
    
    description = models.TextField(max_length=500, help_text='reseignez autre type d\'assistance qui ne figure pas dans la liste', blank=True)
    
    date_given = models.DateTimeField(auto_now_add=True)

    def __str__(self)-> str :
        return self.province+" - "+self.commune+" - "+self.beneficiaire+" - "+self.type_assistance+" - "+self.description
