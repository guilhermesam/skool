# Generated by Django 3.1.1 on 2020-09-23 02:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0002_auto_20200913_0131'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='teacher',
            options={'verbose_name': 'Monitor', 'verbose_name_plural': 'Monitor'},
        ),
        migrations.AlterField(
            model_name='classroom',
            name='date',
            field=models.DateField(verbose_name='Data da aula'),
        ),
        migrations.AlterField(
            model_name='classroom',
            name='hour',
            field=models.TimeField(auto_now=True, verbose_name='Hora da aula'),
        ),
        migrations.AlterField(
            model_name='classroom',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classroom.student', verbose_name='Aluno'),
        ),
        migrations.AlterField(
            model_name='classroom',
            name='subject',
            field=models.CharField(max_length=64, verbose_name='Assunto da aula'),
        ),
        migrations.AlterField(
            model_name='classroom',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classroom.teacher', verbose_name='Professor'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='first_name',
            field=models.CharField(max_length=25, verbose_name='Primeiro nome do Monitor(a)'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='last_name',
            field=models.CharField(max_length=25, verbose_name='Último nome do Monitor(a)'),
        ),
        migrations.CreateModel(
            name='ClassTeacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classroom.classroom')),
                ('id_teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classroom.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='ClassStudent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classroom.classroom')),
                ('id_student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classroom.student')),
            ],
        ),
    ]