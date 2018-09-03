from django import forms

class FormName(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    contactnum = forms.CharField()
    text = forms.CharField(widget = forms.Textarea)
