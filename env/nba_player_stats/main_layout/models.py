from django.db import models

class Stats(models.Model):
	_id 			= models.CharField(max_length=4)
	first_name 		= models.CharField(max_length=32)
	last_name 		= models.CharField(max_length=32)
	position 		= models.CharField(max_length=32)
	height_feet 	= models.CharField(max_length=32)
	height_inches 	= models.CharField(max_length=32)
	weight_pounds 	= models.CharField(max_length=32)
	team_name 		= models.CharField(max_length=32)
	conference 		= models.CharField(max_length=32)
	division 		= models.CharField(max_length=32)

	class Meta:
		verbose_name_plural = 'Statistics'