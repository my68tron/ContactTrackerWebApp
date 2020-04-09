from django.db import models

# Create your models here.
# class EndUserProfile(models.Model):
# 	full_name = models.CharField(max_length=50)
# 	mob_no = models.IntegerField(unique=True)
# 	pin_code = models.IntegerField()

# 	def __str__(self):
# 		return self.full_name
class Contact(models.Model):
    from_mob_no = models.IntegerField()
    to_mob_no = models.IntegerField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return str(self.from_mob_no)
