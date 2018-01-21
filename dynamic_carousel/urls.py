from django.conf.urls import include, url
from .import views

urlpatterns = [
    url(r'^$', views.dycarousel_view, name='dycarousel_view'),
    url(r'^picture/new/$', views.savePicture, name='savePicture'),
]

