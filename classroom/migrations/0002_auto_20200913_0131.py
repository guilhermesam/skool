# Generated by Django 3.1.1 on 2020-09-13 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='classroom',
            options={'verbose_name': 'Sala de Aula', 'verbose_name_plural': 'Salas de Aula'},
        ),
        migrations.AlterField(
            model_name='classroom',
            name='date',
            field=models.DateField(),
        ),
    ]
