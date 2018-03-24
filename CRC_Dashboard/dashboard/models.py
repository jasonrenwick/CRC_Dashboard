from django.db import models


class Scores(models.Model):
    farmerid = models.IntegerField(primary_key=True, max_length=1)
    flavour = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'scores'

    def __str__(self):
        return self.idfarm_ben_expec
