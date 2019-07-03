from django.db import models

# Create your models here.
class Vacation(models.Model):
    vacation_desc = models.TextField()
    date_from = models.DateTimeField('date from')
    date_to = models.DateTimeField('date to')

    def __str__(self):
        return self.vacation_desc
