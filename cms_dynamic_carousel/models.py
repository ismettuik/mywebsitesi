#from django.db import models
from cms.models import CMSPlugin
from dynamic_carousel.models import Picture


class PicturePluginModel(CMSPlugin):
    pictures = Picture.objects.all().order_by('-upload_date')
    #picture = models.ForeignKey(Picture)
    pass
