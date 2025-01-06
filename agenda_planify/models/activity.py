from django.db import models

class Activity (models.Model):
	
	month = models.IntegerField (blank =False)
	year= models.IntegerField (blank =False)
	responsible = models.CharField (blank =False, max_length=255)
	participants = models.CharField (blank =False, max_length=255)
	place = models.CharField (blank =False, max_length=255)
		
	def __str__(self):
		return f"{self.month}"
	

class ActivityDay (models.Model):
	day = models.IntegerField (blank=False)
	activity_id = models.ForeignKey (Activity, on_delete= models.CASCADE)
