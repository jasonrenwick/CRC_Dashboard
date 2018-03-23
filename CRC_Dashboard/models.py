# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class FarmBenExpec(models.Model):
    idfarm_ben_expec = models.AutoField(db_column='idFarm_Ben_Expec', primary_key=True)  # Field name made lowercase.
    flavour = models.IntegerField(db_column='Flavour', blank=True, null=True)  # Field name made lowercase.
    consistency = models.IntegerField(db_column='Consistency', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'farm_ben_expec'

