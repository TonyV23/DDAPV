# Generated by Django 4.1.5 on 2023-01-11 21:27

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('fondation', '0012_alter_person_options_remove_person_unique_person_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Distribution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_given', models.DateField(auto_created=True, verbose_name='date de distribution')),
                ('type_help', multiselectfield.db.fields.MultiSelectField(choices=[('aide_en_nature', 'Aide en nature'), ('aide_en_espece', 'Aide en éspèce'), ('accompagnement_psychosocial', 'Accompagnement psychosocial'), ('accompagnement_medical', 'Accompagnement médical')], max_length=150)),
                ('description', models.CharField(help_text='décrivez le type de don et/ou aides que le bénéficiaire reçoit', max_length=500)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fondation.person')),
            ],
            options={
                'ordering': ['-date_given'],
            },
        ),
        migrations.AddConstraint(
            model_name='distribution',
            constraint=models.UniqueConstraint(fields=('person', 'type_help', 'description', 'date_given'), name='unique_distribution'),
        ),
    ]
