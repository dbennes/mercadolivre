# Generated by Django 4.0 on 2021-12-10 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordemfila', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordem_fila',
            name='vaga',
            field=models.CharField(max_length=200),
        ),
    ]
