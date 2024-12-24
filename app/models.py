from django.db import models

class IrrigationZone(models.Model):
    name = models.CharField(max_length=255)
    soil_moisture = models.FloatField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    # pour la màj de status avant la modif
    def save(self, *args, **kwargs):
        self.status = self.soil_moisture < 30
        super().save(*args, **kwargs)