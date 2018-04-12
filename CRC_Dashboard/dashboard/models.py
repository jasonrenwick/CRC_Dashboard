from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class a_Element(models.Model):
    elementID = models.CharField(max_length=3)
    element_weight = models.IntegerField()
    element_text = models.CharField(max_length=500)

    def __str__(self):
        return self.elementID


class b_Element(models.Model):
    elementID = models.CharField(max_length=3)
    element_weight = models.IntegerField()
    element_text = models.CharField(max_length=500)

    def __str__(self):
        return self.elementID


class Criteria(models.Model):
    criteria = models.CharField(max_length=1)
    criteria_weight = models.IntegerField()
    criteria_min_range = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ]
     )
    criteria_max_range = models.IntegerField(
        default=5,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ]
     )

    def __str__(self):
        return self.criteria +' -- weight: '+ str(self.criteria_weight) +' -- Range: '+ str(self.criteria_min_range) +':'+ str(self.criteria_max_range)


class Farmer_a_score(models.Model):
    farmerID = models.CharField(max_length=4)
    A1 = models. IntegerField(
        default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ]
     )
    A2 = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ]
     )
    A3 = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ]
     )
    A4 = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ]
     )
    A5 = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ]
     )


    def __str__(self):
        return self.farmerID


class Farmer_b_score(models.Model):
    farmerID = models.CharField(max_length=4)
    B1 = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ]
     )
    B2 = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ]
     )
    B3 = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ]
     )
    B4 = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ]
     )
    B5 = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ]
     )

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





