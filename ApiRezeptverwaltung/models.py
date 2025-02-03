from django.db import models

# Create your models here.


# Rezept (Titel, Beschreibung, Zubereitungszeit)
# Zutat (Name, Menge, Einheit)





class Zutat(models.Model):
    name = models.CharField(max_length=100)
    menge = models.CharField(max_length=100)
    einheit = models.CharField(max_length=20)


    def __str__(self):
        return self.name




class Rezept(models.Model):
    titel = models.CharField(max_length=100)
    beschreibung = models.TextField(max_length=1000)
    zubereitungszeit = models.DateTimeField()
    zutaten = models.ForeignKey(Zutat, related_name='zutaten', on_delete=models.SET_NULL,null=True, blank=True)


    def __str__(self):
        return self.titel



