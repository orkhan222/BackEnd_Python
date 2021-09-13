from django.forms import ModelForm
from django import forms


from .models import *

class IndexForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'