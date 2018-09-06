from django import forms

class FormName(forms.Form):
    Title = forms.CharField()
    Author = forms.EmailField()
    Description = forms.CharField(widget=forms.Textarea)
    CreationDate = forms.DateField()
    Location = forms.CharField()
