from django.db import models


class Person(models.Model):
    first_name = models.CharField('Имя', max_length=30)
    last_name = models.CharField(max_length=30)
    # last_update = models.DateField()
    last_update = models.DateField(auto_now=True)
    registration_date = models.DateField(auto_now_add=True)
    height = models.DecimalField(max_digits=5, decimal_places=2)
