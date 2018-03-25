from django.db import models


class Farmbenexpec(models.Model):
    farmerID = models.CharField(max_length=5)
    flavour = models.IntegerField()
    consistency = models.IntegerField()


class Farmben(models.Model):
    flav = models.IntegerField()
    consist = models.IntegerField()

    # def __str__(self):
    #     return self.flav



    # class Meta:
    #     app_label = 'dashboard'
    #     managed = False
    #     # db_table = 'scores'
    #
    # def __str__(self):
    #     return self.farmerID
