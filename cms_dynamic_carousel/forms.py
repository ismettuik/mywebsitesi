from django import forms
from dynamic_carousel.models  import Picture


class PictureWizardForm(forms.ModelForm):
    class Meta:
        model = Picture
        exclude = []
