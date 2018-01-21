from django.db import models
from django.utils import timezone

class Picture(models.Model):
    code = models.IntegerField()
    picture = models.FileField(upload_to = 'hbpictures')
    upload_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.code)
