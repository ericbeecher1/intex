# Generated by Django 2.1.5 on 2019-04-10 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perscriptions', '0008_auto_20190410_1438'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='prescriber',
            options={'permissions': (('can_crud', 'Has Ability to Create Update and Delete'),)},
        ),
    ]
