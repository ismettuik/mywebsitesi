from django.db import models
from django.utils import timezone


class Duyuru(models.Model):

    kod = models.IntegerField()
    baslik = models.CharField(max_length=200)
    icerik = models.TextField()
    eklenme_tarihi = models.DateTimeField(
           default=timezone.now)   
    EVET = 'E'
    HAYIR = 'H'
    YAYINLANSINMI = (
        (EVET, 'Evet'),
        (HAYIR, 'Hayır'),
    )
    yayinlansinmi = models.CharField(max_length=1, choices=YAYINLANSINMI, default=HAYIR )


    def __str__(self):
        return self.baslik
