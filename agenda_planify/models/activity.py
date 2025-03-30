from django.db import models
from django.core.exceptions import ValidationError

def validate_day(value):
    """Valida que el día esté entre 1 y 31."""
    if value < 1 or value > 31:
        raise ValidationError("El día debe estar entre 1 y 31.")

class Activity (models.Model):
	
	MONTH_CHOICES = [
        (1, "Enero"),
        (2, "Febrero"),
        (3, "Marzo"),
        (4, "Abril"),
        (5, "Mayo"),
        (6, "Junio"),
        (7, "Julio"),
        (8, "Agosto"),
        (9, "Septiembre"),
        (10, "Octubre"),
        (11, "Noviembre"),
        (12, "Diciembre"),
    ]
	name = models.CharField (blank =False, max_length=255)
	hour = models.TimeField (blank =False)
	day = models.IntegerField(blank=False, validators=[validate_day])
	month = models.IntegerField(choices=MONTH_CHOICES, blank=False)
	responsible = models.CharField (blank =False, max_length=255)
	participants = models.CharField (blank =False, max_length=255)
	place = models.CharField (blank =False, max_length=255)
		
	def __str__(self):
		return f"{self.month}"