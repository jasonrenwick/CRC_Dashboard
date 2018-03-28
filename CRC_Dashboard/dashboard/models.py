from django.db import models


class Criterions(models.Model):
    criterionID = models.CharField(max_length=3)
    criterion_weight = models.IntegerField()
    criterion_text = models.CharField(max_length=500)

    def __str__(self):
        return self.criterionID


class Criteria(models.Model):
    criteria = models.CharField(max_length=1)
    criteria_weight = models.IntegerField()

    def __str__(self):
        return self.criteria


class Farmerscores(models.Model):
    farmerID = models.CharField(max_length=4)
    A1 = models.IntegerField()
    A2 = models.IntegerField()
    A3 = models.IntegerField()
    A4 = models.IntegerField()
    A5 = models.IntegerField()

    def __str__(self):
        return self.farmerID


    # def __str__(self):
    #     return self.flav



    # class Meta:
    #     app_label = 'dashboard'
    #     managed = False
    #     # db_table = 'scores'
    #
    # def __str__(self):
    #     return self.farmerID
