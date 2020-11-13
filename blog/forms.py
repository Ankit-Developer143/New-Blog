from ckeditor import fields
from django import forms
from django import forms
import widget_tweaks
from .models import*

class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("name","body")
        widgets = {
            "name":forms.TextInput(attrs={"class":"col-sm-12"}),
             "body":forms.TextInput(attrs={"class":"col-sm-12"}),
            
            
            
        }