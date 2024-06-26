from django.db import models

# Create your models here.

class Record(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    class Meta:
        db_table = "records"