from django.db import models

WHAT_CHOICES = (
    ('CA', 'Chiffre d\'affaires'),
    ('MEA', 'Mise en avant'),
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

TYPE_CHOICES = (
    ('T1', 'TYPE_1'),
    ('T2', 'TYPE_2'),
    ('T3', 'TYPE_3')
)

# Create your models here.


class Pharmacy(models.Model):
    cip = models.IntegerField()
    pharma_name = models.CharField(max_length=100)
    group = models.CharField(max_length=100, null=True)
    labo_name = models.CharField(max_length=100, null=True)
    # product = models.CharField(max_length=100, null=True)
    type = models.CharField(max_length=100, null=True)
    subtype = models.CharField(max_length=100, null=True)
    ca = models.IntegerField(null=True)
    unit = models.IntegerField(null=True)
    year = models.IntegerField(null=True)
    unit_evolution = models.FloatField(null=True)
    ca_evolution = models.FloatField(null=True)


class SimpleCondition(models.Model):
    what = models.CharField(max_length=100, choices=WHAT_CHOICES, verbose_name='Quoi', default='CA')
    who = models.CharField(max_length=100, choices=WHO_CHOICES, null=True, verbose_name='Qui', blank=True)
    first_year = models.IntegerField(null=True, verbose_name='Annee 1', blank=True)
    type = models.CharField(max_length=100, choices=TYPE_CHOICES, null=True, verbose_name='Type', blank=True)
    operator = models.CharField(max_length=100, choices=OPERATOR_CHOICES, null=True, verbose_name='Opérateur',
                                blank=True)
    quantity = models.FloatField(verbose_name='Quantité', null=True, blank=True)
    second_year = models.IntegerField(null=True, verbose_name='Annee 2', blank=True)
    unit = models.CharField(max_length=100, choices=UNIT_CHOICES, null=True, verbose_name='Unité', blank=True)
    rate_reduction = models.FloatField(null=True, verbose_name='RFA', blank=True)


class ComparativeCondition(models.Model):
    first_what = models.CharField(max_length=100, choices=WHAT_CHOICES, verbose_name='Quoi 1', default='CA')
    first_year = models.IntegerField(null=True, verbose_name='Annee 1', blank=True)
    operator = models.CharField(max_length=100, choices=OPERATOR_CHOICES, null=True, verbose_name='Opérateur',
                                blank=True)
    quantity = models.FloatField(verbose_name='Quantité', null=True, blank=True)
    second_what = models.CharField(max_length=100, choices=WHAT_CHOICES, verbose_name='Quoi 2', default='CA')
    second_year = models.IntegerField(null=True, verbose_name='Annee 2', blank=True)
    rate_reduction = models.FloatField(null=True, verbose_name='RFA', blank=True)


class NoCondition(models.Model):
    rate_reduction = models.FloatField(null=True, verbose_name='RFA', blank=True)
    who = models.CharField(max_length=100, choices=WHO_CHOICES, null=True, verbose_name='Qui', blank=True)
    first_year = models.IntegerField(null=True, verbose_name='Annee 1', blank=True)
    second_year = models.IntegerField(null=True, verbose_name='Annee 3', blank=True)