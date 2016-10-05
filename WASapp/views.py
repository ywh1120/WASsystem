from django.shortcuts import render
from WASapp.models import *
from WASapp.forms import *
from django.shortcuts import (render,get_object_or_404,redirect)
from django.forms.formsets import formset_factory
from django.http import Http404
#from django.db.models.Field import Empty
from django.forms.models import modelformset_factory
from django.contrib.auth.decorators import login_required
# Create your views here.
def mainpage(request):
    list = Pdfdata.objects.filter()
    return render(request,'index.html',{'list':list})

def insert(request):
    
    pdfForm = PdfForm()
    
    if request.method == 'GET':
        pdfForm = PdfForm()
    elif request.method == 'POST':
        pdfForm = PdfForm(request.POST, request.FILES)
        if pdfForm.is_valid():
            insert = pdfForm.save(commit=False)
            insert.user = request.user
            insert.save()
    
    return render(request, 'insert.html',{'pdfForm':pdfForm})