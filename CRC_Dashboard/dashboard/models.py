# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class FarmBenExpec(models.Model):
    idfarm_ben_expec = models.AutoField(db_column='idFarm_Ben_Expec', primary_key=True)  # Field name made lowercase.
    flavour = models.IntegerField(db_column='Flavour', blank=True, null=True)  # Field name made lowercase.
    consistency = models.IntegerField(db_column='Consistency', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.idfarm_ben_expec
