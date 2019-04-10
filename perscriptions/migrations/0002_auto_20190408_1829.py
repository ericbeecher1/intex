# Generated by Django 2.1.5 on 2019-04-08 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perscriptions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perscriber',
            name='Credentials',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='perscriber',
            name='DoctorID',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='perscriber',
            name='Fname',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='perscriber',
            name='Lname',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='perscriber',
            name='Specialty',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='perscriber',
            name='State',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='perscriber',
            name='TotalPerscriptions',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='perscriptions',
            name='QuanityPerscribed',
            field=models.TextField(),
        ),
    ]
