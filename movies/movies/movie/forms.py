from django import forms
from .models import *
# from .director.models import Director
from director.models import  Director
class NewMovieForm(forms.Form):
    movie_name = forms.CharField(max_length=100,required=True)
    part = forms.IntegerField()
    movie_image = forms.FileField()
    director=forms.ChoiceField(choices=Director.Get_all())

    # director = forms.ChoiceField(choices=Director.Get_all())
class NewMovieFormModel(forms.ModelForm):
    class Meta:
        model=Movie
        fields='__all__'
