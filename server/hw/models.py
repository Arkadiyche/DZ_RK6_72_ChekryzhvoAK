from django.db import models


class First(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(verbose_name='Полное имя', max_length=150)

    def __str__(self):
        return f'[{self.id}] {self.full_name}'


class Second(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='Название вакансии', max_length=150)
    company = models.CharField(verbose_name='Название вакансии', max_length=150)
    fk = models.ForeignKey('First', on_delete=models.CASCADE)

