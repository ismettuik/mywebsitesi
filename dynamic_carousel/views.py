#-*- coding: utf-8 -*-
from .models import Picture
from .forms import PictureForm
from django.shortcuts import render, redirect

def savePicture(request):
   saved = False
   
   if request.method == "POST":
      #Get the posted form
      pictureForm = PictureForm(request.POST, request.FILES)
      
      if pictureForm.is_valid():
         picture = Picture()
         picture.code = pictureForm.cleaned_data["code"]
         picture.picture = pictureForm.cleaned_data["picture"]
         picture.save()
         saved = True
         return redirect('dycarousel_view') 
   else:
      pictureForm = PictureForm()
		
   return render(request, 'dynamic_carousel/picture_edit.html', {'pictureForm': pictureForm})


def dycarousel_view(request):
    pictures = Picture.objects.all().order_by('-upload_date')
    return render(request, 'dynamic_carousel/dycarousel_list.html', {'pictures': pictures}) 

