from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Account(models.Model):
    account_id = models.IntegerField()
    account_child_id = models.IntegerField()
    potential = models.CharField(max_length=200)
    pipeline = models.CharField(max_length=200)
    stage = models.CharField(max_length=200)

class Account_Risk(models.Model):
    account_id = models.IntegerField()
    account_name = models.CharField(max_length=100)
    customer_name = models.CharField(max_length=100)
    account_risk = models.CharField(max_length=100)
