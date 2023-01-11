# Generated by Django 4.1.5 on 2023-01-11 12:38

from django.db import migrations, models
import multiselectfield.db.fields
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('fondation', '0008_person_person_unique_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donor_date_given', models.DateField(auto_created=True)),
                ('donor_type', models.CharField(choices=[('org', 'Organisation'), ('entrp', 'Entreprise'), ('assoc', 'Association'), ('part', 'Particulier'), ('anonym', 'Rester anonyme')], max_length=50, verbose_name='donateur (trice)')),
                ('donor_name', models.CharField(blank=True, help_text="tapez votre nom / le nom de l'entreprise , de l'association ou de l'organisation", max_length=50, verbose_name='Nom')),
                ('type_help', multiselectfield.db.fields.MultiSelectField(choices=[('aide_en_nature', 'Aide en nature'), ('aide_en_espece', 'Aide en éspèce'), ('accompagnement_psychosocial', 'Accompagnement psychosocial'), ('accompagnement_medical', 'Accompagnement médical')], max_length=150)),
                ('description', models.CharField(blank=True, help_text='décrivez le type de don et/ou aides que vous souhaitez donner à notre fondation', max_length=500)),
                ('donor_phone', phone_field.models.PhoneField(help_text='ce numero de téléphone sera utilisé pour entrer en contact avec vous', max_length=31, verbose_name='Téléphone')),
                ('donor_email', models.EmailField(help_text='cette addresse mail sera utilisée pour entrer en contact avec vous', max_length=254, verbose_name='email')),
            ],
        ),
        migrations.AddConstraint(
            model_name='donation',
            constraint=models.UniqueConstraint(fields=('donor_type', 'donor_name', 'type_help', 'description', 'donor_phone', 'donor_email', 'donor_date_given'), name='unique_donor'),
        ),
    ]