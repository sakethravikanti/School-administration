from django.db import models

# Create your models here.
class Data(models.Model):
    name=models.CharField(max_length=50)
    grade=models.SmallIntegerField()
    section=models.CharField(max_length=2)
    marks=models.IntegerField()
    def __str__(self):
        return f"{self.name} {self.grade}{self.section}"