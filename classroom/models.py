from django.db import models
from datetime import datetime


class Student(models.Model):
    name = models.CharField(max_length=150, verbose_name="Nome do Aluno", blank=True, null=False)
    born_date = models.DateField(verbose_name="Data de Nascimento", blank=True, null=False)
    street = models.CharField(max_length=50, verbose_name="Rua", blank=True, null=False)
    number = models.SmallIntegerField(verbose_name="Número da Casa", blank=True, null=False)
    city = models.CharField(max_length=30, verbose_name="Cidade", blank=True, null=False)

    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'

    def __str__(self):
        return self.name


class Teacher(models.Model):
    first_name = models.CharField(max_length=25, verbose_name="Primeiro nome do Monitor(a)", null=False)
    last_name = models.CharField(max_length=25, verbose_name="Último nome do Monitor(a)", null=False)

    class Meta:
        verbose_name = 'Monitor'
        verbose_name_plural = 'Monitor'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Classroom(models.Model):
    hour = models.TimeField(verbose_name="Hora da aula", auto_now=True)
    date = models.DateField(verbose_name="Data da aula")
    subject = models.CharField(max_length=64, verbose_name="Assunto da aula")

    class Meta:
        verbose_name = 'Sala de Aula'
        verbose_name_plural = 'Salas de Aula'

    def __str__(self):
        date = datetime.strptime(str(self.date), '%Y-%m-%d').strftime('%d/%m/%Y')
        hour = datetime.strptime(str(self.hour), '%H:%M:%S.%f').strftime('%H:%M')
        return f"Aula do dia {date}, às {hour} horas"



class ClassStudent(models.Model):
    id_classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    id_student = models.ForeignKey(Student, on_delete=models.CASCADE)


class ClassTeacher(models.Model):
    id_classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    id_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
