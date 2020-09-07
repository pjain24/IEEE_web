from django import forms
from django.forms import ModelForm
from .models import Contact


class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=254, required = True)
    email = forms.EmailField(max_length=254, required = True)
    message = forms.CharField(max_length=750, widget=forms.Textarea, required = True)
    subject = forms.CharField(max_length=255, required = True)

    class Meta:
        model = Contact
        fields = {'name','email', 'message', 'subject',}