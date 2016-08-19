from django.db import models
from django.utils import timezone

class User(models.Model):
	user_name = models.CharField(max_length=50)
	user_email = models.EmailField()
	user_password = models.CharField(unique=True, max_length=50)

	def __str__(self):
		return self.user_name

class Consume(models.Model):
	con_type = models.CharField(max_length=100)
	store_name = models.CharField(max_length=100)
	con_date = models.DateTimeField(default=timezone.now)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	con_price = models.IntegerField()

	def __str__(self):
		return self.store_name

