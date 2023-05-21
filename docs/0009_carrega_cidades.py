# Generated by Django 3.2.12 on 2023-05-19 13:19

from django.db import migrations

def load_initial_data(apps, schema_editor):
    # get our model
    # get_model(appname, modelname)
    estado_model = apps.get_model('geps', 'Estado')
    cidade_model = apps.get_model('geps', 'Cidade')
    
    # Inclua na lista todas as cidades necessárias
    for i in [('Santo André','SP')]:
        cidade, estado = i
        
        estado_id=estado_model.objects.get(sigla = estado)
        
        cidade_model.objects.create(nome = cidade, estado_id = estado_id.id)

def clean_reverse_data(apps, schema_editor):
    cidade_model = apps.get_model('geps', 'Cidade')
    cidade_model.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('geps', '0008_carrega_estados'),
    ]

    operations = [
        migrations.RunPython(load_initial_data, clean_reverse_data),        
    ]
