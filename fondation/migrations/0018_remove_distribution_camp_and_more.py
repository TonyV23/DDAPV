# Generated by Django 4.1.5 on 2023-01-26 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fondation', '0017_alter_distribution_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='distribution',
            name='camp',
        ),
        migrations.AlterField(
            model_name='distribution',
            name='description',
            field=models.CharField(blank=True, help_text="reseignez autre type d'assistance qui ne figure pas dans la liste", max_length=500),
        ),
        migrations.AlterField(
            model_name='distribution',
            name='type_aide',
            field=models.CharField(choices=[('aide_en_nature', 'Aide en nature'), ('aide_en_espece', 'Aide en éspèce'), ('accompagnement_psychosocial', 'Accompagnement psychosocial'), ('accompagnement_medical', 'Accompagnement médical')], max_length=150),
        ),
        migrations.AlterField(
            model_name='distribution',
            name='type_assistance',
            field=models.CharField(choices=[('vivre_alimentaire', 'Vivre alimentaire'), ('ustenciles_de_cuisines', 'Ustenciles de cuisines'), ('eau_potable', 'Eau potable'), ('briquettes', 'briquettes'), ('kit_de_dignite', 'Kit de dignité pour les femmes'), ('vetements', 'Les Vêtements'), ('kit_scolaire', 'Kit Scolaire'), ('medicaments', 'Médicaments / Soins médicaux'), ('fonds_de_roulements', 'Fonds de roulements de micro-projets'), ('enseignements_de_metiers', 'Enseignements de métiers'), ('reunification_familliale', 'Réunification familliale'), ('reinstallation', 'Réinstallation'), ('kinesitherapie', 'kinésithérapie')], max_length=500),
        ),
    ]
