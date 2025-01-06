from django.db import models
from agenda_planify.models.activity import Activity

class Pt_FTL(models.Model):
	month = models.IntegerField (blank =False)
	data_create = models.DateTimeField (blank =False)
	file = models.FileField (blank =False, upload_to='uploads/')
	generated = models.BooleanField (blank =False)
	activity = models.ManyToManyField(Activity)
	

	def __str__(self):
		return f"{self.month}"