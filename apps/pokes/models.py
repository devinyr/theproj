from django.db import models
from apps.accounts.models import User


class Poke(models.Model):
	whom_id = models.ForeignKey(User)
	num_poke = models.IntegerField(default=0)
	class Meta:
		db_table = 'poke'

class Who(models.Model):
	usr_id = models.ForeignKey(User)
	pokes = models.ManyToManyField(Poke)
	class Meta:
		db_table = 'who'

