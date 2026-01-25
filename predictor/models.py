from django.db import models

class Place(models.Model):
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    price_per_sqft = models.IntegerField()

    def __str__(self):
        return f"{self.city}, {self.state}"
