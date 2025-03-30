from django.db import models
from .activity import Activity
from django.core.validators import MinValueValidator, MaxValueValidator

class Pt_UCI(models.Model):
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

	month = models.IntegerField(choices=MONTH_CHOICES, blank=False)
	data_create = models.DateTimeField (blank =False)
	file = models.FileField (blank =False, upload_to='uploads/')
	processed = models.BooleanField (blank =False)
	activity = models.ManyToManyField(Activity)

	def __str__(self):
		return f"{self.month}"