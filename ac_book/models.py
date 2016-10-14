from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (
		    BaseUserManager, AbstractBaseUser
		)

# class User(models.Model):
# 	user_name = models.CharField(max_length=50)
# 	user_email = models.EmailField()
# 	user_password = models.CharField(unique=True, max_length=50)

# 	def __str__(self):
# 		return self.user_name

class Consume(models.Model):
	con_type = models.CharField(max_length=100)
	store_name = models.CharField(max_length=100)
	con_date = models.DateTimeField(default=timezone.now)
	con_price = models.IntegerField()
	user = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		on_delete=models.CASCADE,
	)
	# user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.store_name


class MyUserManager(BaseUserManager):
	def create_user(self, email, date_of_birth, password=None):
		"""
		Creates and saves a User with the given email, date of
		birth and password.
		"""
		if not email:
			raise ValueError('Users must have an email address')

		user = self.model(
		email=self.normalize_email(email),
		date_of_birth=date_of_birth,
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, date_of_birth, password):
		"""
		Creates and saves a superuser with the given email, date of
		birth and password.
		"""
		user = self.create_user(
		email,
		password=password,
		date_of_birth=date_of_birth,
		)
		user.is_admin = True
		user.save(using=self._db)
		return user


class MyUser(AbstractBaseUser):
	email = models.EmailField(
		verbose_name='email address',
		max_length=255,
		unique=True,
	)
	date_of_birth = models.DateField()
	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)

	objects = MyUserManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['date_of_birth']

	def get_full_name(self):
		# The user is identified by their email address
		return self.email

	def get_short_name(self):
		# The user is identified by their email address
		return self.email

	def __str__(self):              # __unicode__ on Python 2
		return self.email

	def has_perm(self, perm, obj=None):
		"Does the user have a specific permission?"
		# Simplest possible answer: Yes, always
		return True

	def has_module_perms(self, app_label):
		"Does the user have permissions to view the app `app_label`?"
		# Simplest possible answer: Yes, always
		return True

	@property
	def is_staff(self):
		"Is the user a member of staff?"
		# Simplest possible answer: All admins are staff
		return self.is_admin

class Category(models.Model):
	category_name = models.CharField(default="Unknown", unique=True, max_length=100)
	class Meta:
		abstract = True

class ConsumeCategory(Category):{}
class SocialCategory(Category):{}

class Con_ConCategory(models.Model):
	consume_id = models.ForeignKey(
		Consume,
		on_delete=models.CASCADE
	)
	category_id = models.ForeignKey(ConsumeCategory,on_delete=models.CASCADE)
