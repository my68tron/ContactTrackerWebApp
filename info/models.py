from django.db import models


class Contact(models.Model):
    from_mob_no = models.IntegerField()
    to_mob_no = models.IntegerField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return str(self.from_mob_no)
