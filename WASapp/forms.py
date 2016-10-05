from __future__ import unicode_literals

from django import forms
from WASapp.models import *
from django.contrib.auth.models import User

class PdfForm(forms.ModelForm):
    title = forms.CharField(required=True,widget=forms.TextInput(attrs={'size':'200','required':'True'}))
    pdffile = forms.FileField()
    class Meta:
        model = Pdfdata
        fields = '__all__'