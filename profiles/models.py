from django.db import models

# Create your models here.
class EndUserProfile(models.Model):
	full_name = models.CharField(max_length=50)
	mob_no = models.IntegerField(unique=True)
	pin_code = models.IntegerField()

	def __str__(self):
		return self.full_name