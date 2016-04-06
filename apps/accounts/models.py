from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.

class User(AbstractBaseUser):
	email = models.EmailField(verbose_name='email address', unique=True, db_index=True)
	name = models.CharField(max_length=100)
	alias = models.CharField(max_length=100)
	dob = models.DateField(default='1900-01-01')
	
	USERNAME_FIELD = 'email'

	def __unicode__(self):
		return self.email
