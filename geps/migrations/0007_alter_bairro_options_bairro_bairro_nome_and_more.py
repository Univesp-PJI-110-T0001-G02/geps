# Generated by Django 4.1.9 on 2023-05-19 14:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("geps", "0006_disponibilidaderegiao_docente_regiao"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="bairro",
            options={},
        ),
        migrations.AddConstraint(
            model_name="bairro",
            constraint=models.UniqueConstraint(
                fields=("nome", "cidade_id"), name="bairro_nome"
            ),
        ),
        migrations.AddConstraint(
            model_name="cidade",
            constraint=models.UniqueConstraint(
                fields=("nome", "estado_id"), name="cidade_nome"
            ),
        ),
        migrations.AddConstraint(
            model_name="estado",
            constraint=models.UniqueConstraint(fields=("sigla",), name="estado_sigla"),
        ),
    ]
