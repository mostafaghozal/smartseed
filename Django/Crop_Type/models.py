from django.conf import settings
from django.db import models
from Farm.models import Farm


class Crop(models.Model):
	farm = models.ForeignKey(Farm, on_delete=models.CASCADE, related_name='farm')
	CROP_TYPES = (
        ('Kharif crops', 'Kharif crops'),
        ('Rabi Crops', 'Rabi Crops'),
        ('Zaid Crop', 'Zaid Crop'),
        ('Rice', 'Rice'),
        ('Wheat', 'Wheat'),
        ('Pulses', 'Pulses'),
        ('Sugarcane', 'Sugarcane'),
        ('Cotton', 'Cotton'),
        ('Groundnut', 'Groundnut'),
        ('Tea', 'Tea'),
        ('Coffee', 'Coffee')
    )
	crop_type = models.CharField(max_length=20, choices=CROP_TYPES, default='Pulses')
	longitude = models.FloatField(default=0.00)
	latitude = models.FloatField(default=0.00)
	created_on = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.id)+'--'+ self.farm.__str__()+'--'+str(self.crop_type)