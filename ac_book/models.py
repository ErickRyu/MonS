from django.db import models
from django.utils import timezone

class Consume(models.Model):
	con_type = models.CharField(max_length=100)
	store_name = models.CharField(max_length=100)
	con_date = models.DateTimeField(default=timezone.now)
	# user_id = 
	con_price = models.IntegerField()

	def __str__(self):
		return self.store_name