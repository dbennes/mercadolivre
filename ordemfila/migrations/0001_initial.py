# Generated by Django 4.0 on 2021-12-10 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('filadigital', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ordem_fila',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_usuario', models.CharField(max_length=200)),
                ('celular_usuario', models.CharField(max_length=200)),
                ('posicao', models.IntegerField(blank=True, null=True)),
                ('vaga', models.IntegerField(max_length=200)),
                ('fila', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='filadigital.fila')),
            ],
        ),
    ]
