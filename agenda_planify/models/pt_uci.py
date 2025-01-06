from django.db import models
from .activity import Activity

class Pt_UCI(models.Model):
	month = models.IntegerField (blank =False)
	data_create = models.DateTimeField (blank =False)
	file = models.FileField (blank =False, upload_to='uploads/')
	processed = models.BooleanField (blank =False)
	activity = models.ManyToManyField(Activity)

	def __str__(self):
		return f"{self.month}"