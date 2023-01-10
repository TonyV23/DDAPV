# Generated by Django 4.1.5 on 2023-01-10 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fondation', '0006_typehelp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Help',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='ex : vivre alimentaires , personnes vivant avec handicap', max_length=40, unique=True, verbose_name='aides')),
                ('type_help', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fondation.typehelp')),
            ],
            options={
                'ordering': ['type_help', 'name'],
            },
        ),
        migrations.AddConstraint(
            model_name='help',
            constraint=models.UniqueConstraint(fields=('type_help', 'name'), name='unique_aide'),
        ),
    ]
