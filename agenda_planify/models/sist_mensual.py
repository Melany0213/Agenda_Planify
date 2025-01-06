from django.db import models
from agenda_planify.models.activity import Activity
from agenda_planify.models.pt_ftl import Pt_FTL


class ST_Mensual(models.Model):
	month = models.IntegerField (blank =False)
	data_create = models.DateTimeField (blank =False)
	file = models.FileField (blank =False, upload_to='uploads/')
	processed = models.BooleanField (blank =False)
	activity = models.ManyToManyField(Activity)
	pt_ftl = models.OneToOneField(Pt_FTL, on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.month}"