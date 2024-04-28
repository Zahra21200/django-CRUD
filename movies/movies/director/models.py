from django.db import models

# Create your models here.
class Director(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)

    @classmethod
    def Get_all(cls):
        return [(director.id, director.name) for director in cls.objects.all()]

    @classmethod
    def getDirector(cls,id):
        return cls.objects.get(id=id)

    def __str__(self):
        return self.name
