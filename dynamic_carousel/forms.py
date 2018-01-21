#-*- coding: utf-8 -*-
from django import forms

class PictureForm(forms.Form):
   code = forms.IntegerField()
   picture = forms.FileField()

