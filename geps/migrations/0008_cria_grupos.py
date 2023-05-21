# Generated by Django 4.1.9 on 2023-05-21 12:43

from django.db import migrations
from django.contrib.auth.models import Group

def load_initial_data(apps, schema_editor):
    # get our model
    # get_model(appname, modelname)
    Group.objects.get_or_create(name='Instituição')
    Group.objects.get_or_create(name='Docente')

def clean_reverse_data(apps, schema_editor):
    Group.objects.filter(name='Instituição').delete()
    Group.objects.filter(name='Docente').delete()

class Migration(migrations.Migration):
    dependencies = [
        ("geps", "0007_alter_bairro_options_bairro_bairro_nome_and_more"),
    ]

    operations = [
        migrations.RunPython(load_initial_data, clean_reverse_data),
    ]