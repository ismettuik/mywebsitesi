from django.db import models
from cms.models import CMSPlugin
from duyuru.models import Duyuru 


class TekDuyuruPluginModel(CMSPlugin):
   
    duyuru = models.ForeignKey(Duyuru)


class CokDuyuruPluginModel(CMSPlugin):
   
    pass
