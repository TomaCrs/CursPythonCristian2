from django.db import models

class Reteta(models.Model):
    nume = models.CharField(max_length=100)
    text_reteta = models.CharField(max_length=1000)
    timp_executie= models.CharField(max_length=100)
    data_adaugare = models.DateTimeField(auto_now_add=True, blank=True)
    data_actualizare = models.DateTimeField(auto_now=True, blank=True)
    active = models.BooleanField(default=True)


    def __str__(self):
        return f"{self.nume} {self.timp_executie}"