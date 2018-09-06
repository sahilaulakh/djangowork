from django.shortcuts import render
from . import forms
# Create your views here.

def index(request):
    return render(request, 'basicapp/index.html')

def view_form(request):
    form = forms.FormName()

    if request.method == "POST":
        form = forms.FormName(request.POST)

        if form.is_valid():
            print("Title is :" + form.cleaned_data["Title"])
            print("Author is :" + form.cleaned_data["Author"])
            print("Description is :" + form.cleaned_data["Description"])
            print("CreationDate is :" + form.cleaned_data["CreationDate"])
            print("Location is :" + form.cleaned_data["Location"])

    return render(request, 'basicapp/form_page.html',{'form':form})