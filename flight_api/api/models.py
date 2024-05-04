from django.db import models

class Flight(models.Model):
    Flight_No = models.CharField(max_length=100, primary_key=True)
    Airline = models.CharField(max_length=20)
    From = models.CharField(max_length=100)
    To = models.CharField(max_length=100)
    Duration = models.CharField(max_length=20)
    Price = models.CharField(max_length=20)
    
    def __str__(self):
        return self.Flight_No
