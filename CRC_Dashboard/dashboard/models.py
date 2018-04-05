from django.db import models


class Element(models.Model):
    elementID = models.CharField(max_length=3)
    element_weight = models.IntegerField()
    element_text = models.CharField(max_length=500)

    def __str__(self):
        return self.elementID


class Criteria(models.Model):
    criteria = models.CharField(max_length=1)
    criteria_weight = models.IntegerField()

    def __str__(self):
        return self.criteria


class Farmerscore(models.Model):
    farmerID = models.CharField(max_length=4)
    A1 = models.IntegerField()
    A2 = models.IntegerField()
    A3 = models.IntegerField()
    A4 = models.IntegerField()
    A5 = models.IntegerField()

    def __str__(self):
        return self.farmerID


class Farmer(models.Model):
    farmerID = models.CharField(max_length=4)
    Name = models.CharField(max_length=40)
    Location = models.CharField(max_length=40)
    Region = models.CharField(max_length=40)
    Country = models.CharField(max_length=40)

    def __str__(self):
        return self.farmerID +' - '+ self.Name

