from django.db import models


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
    first_name = models.CharField(max_length=25, verbose_name="Primeiro nome do Professor(a)", null=False)
    last_name = models.CharField(max_length=25, verbose_name="Último nome do Professor(a)", null=False)

    class Meta:
        verbose_name = 'Professor'
        verbose_name_plural = 'Professores'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Classroom(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name="Professor")
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="Aluno")
    hour = models.SmallIntegerField(verbose_name="Hora da aula")
    date = models.DateField(verbose_name="Data da aula")
    subject = models.CharField(max_length=64, verbose_name="Assunto da aula")

    class Meta:
        verbose_name = 'Sala de Aula'
        verbose_name_plural = 'Salas de Aula'

    def __str__(self):
        return f"Aula do dia {self.date}, às {self.hour} horas"
