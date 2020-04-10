from django.db import models


class Contact(models.Model):
    from_mob_no = models.CharField(max_length=10)
    to_mob_no = models.CharField(max_length=10)
    timestamp = models.DateTimeField()

    def __str__(self):
        return str(self.from_mob_no)
