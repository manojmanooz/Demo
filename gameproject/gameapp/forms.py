from django import forms
from . models import game
class gameform(forms.ModelForm):
    class Meta:
        model=game
        fields=['name','desc','img']