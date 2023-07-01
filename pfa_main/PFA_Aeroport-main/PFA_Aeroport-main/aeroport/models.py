from django.db import models

class Vol (models.Model):
    Id_vols = models.CharField(max_length=50)
    Aeroport_depart = models.CharField(max_length=50)
    Aeroport_arrivée = models.CharField (max_length=50)
    Heure_départ = models.TimeField()
    Heure_arrivée = models.TimeField()
    Id_avion = models.CharField(max_length=50)
    Num_porte = models.ForeignKey('portes', on_delete=models.CASCADE)
    Images = models.ImageField()
    
    def __str__(self) :
        return self.Id_vols

class Compagnie (models.Model):
    Id_compagnie = models.CharField(max_length=50)
    Nom = models.CharField(max_length=50)
    pays = models.CharField(max_length=50)
    Images = models.ImageField()

    def __str__(self) :
        return self.Id_compagnie
    
class avion (models.Model):
    Id_avion = models.CharField(max_length=50)
    Modèle = models.CharField(max_length=50)
    capacité = models.CharField(max_length=50)

    def __str__(self) :
        return self.Id_avion
    
class Portes (models.Model):
    Num_porte = models.CharField(max_length=50)
    Id_compagnie = models.ForeignKey('Compagnie', on_delete=models.CASCADE)
    Id_vols = models.ForeignKey('Vol', on_delete=models.CASCADE)

    def __str__(self) :
        return self.Num_porte