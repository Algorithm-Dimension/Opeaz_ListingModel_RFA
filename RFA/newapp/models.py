from django.db import models


# Create your models here.
class Pharmacy(models.Model):
    name = models.CharField(max_length=100)
    group = models.CharField(max_length=100, null=True)
    labo_name = models.CharField(max_length=100, null=True)
    type = models.CharField(max_length=100, null=True)
    sub_type = models.CharField(max_length=100, null=True)
    ca = models.IntegerField(null=True)
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)


class Condition(models.Model):
    WHAT_CHOICES = (
        ('CA', 'Chiffre d\'affaires'),
        ('Benefice', 'Bénéfice'),
        ('gondole', 'Tête de gondole')
    )
    WHO_CHOICES = (
        ('produit', 'Produit'),
        ('gamme', 'Gamme'),
        ('total', 'Total')
    )
    OPERATOR_CHOICES = (
        ('lt', '<'),
        ('gt', '>'),
        ('eq', '='),
    )
    UNIT_CHOICES = (
        ('currency', '€'),
        ('percentile', '%'),
        ('quantity', 'quantité')
    )

    what = models.CharField(max_length=100, choices=WHAT_CHOICES, verbose_name='Quoi', default='CA')
    who = models.CharField(max_length=100, choices=WHO_CHOICES, null=True, verbose_name='Qui', blank=True)
    operator = models.CharField(max_length=100, choices=OPERATOR_CHOICES, null=True, verbose_name='Opérateur', blank=True)
    quantity = models.IntegerField(verbose_name='Quantité', null=True, blank=True)
    unit = models.CharField(max_length=100, choices=UNIT_CHOICES, null=True, verbose_name='Unité', blank=True)
    start_date = models.DateField(null=True, verbose_name='Date de début', blank=True)
    end_date = models.DateField(null=True, verbose_name='Date de fin', blank=True)