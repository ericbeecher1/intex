# Generated by Django 2.1.5 on 2019-04-09 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perscriptions', '0003_auto_20190408_2116'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Perscriber',
            new_name='Prescriber',
        ),
        migrations.RenameModel(
            old_name='Perscriptions',
            new_name='Prescriptions',
        ),
        migrations.RenameField(
            model_name='prescriber',
            old_name='OpioidPerscriber',
            new_name='OpioidPrescriber',
        ),
        migrations.RenameField(
            model_name='prescriber',
            old_name='TotalPerscriptions',
            new_name='TotalPrescriptions',
        ),
        migrations.RenameField(
            model_name='prescriptions',
            old_name='Perscriber',
            new_name='Prescriber',
        ),
    ]
