from django.shortcuts import render
from django.http import HttpResponse
from .models import Yazi

def yazilar(request):
   return render(request, 'yazilar/yazilar.html')

def koseyazilari(request):
    koseyazilarim = Yazi.objects.all()
    return render(request,'yazilar/koseyazilari.html',{'koseyazilarim':koseyazilarim})

def analizler(request):
    analizlerim = Yazi.objects.all()
    return render(request, 'yazilar/analizler.html',{'analizlerim':analizlerim})

def tekyazi(request, yaziId):
    yazilarim = Yazi.objects.all()
    return render(request,'yazilar/tekyazi.html',{'yazilarim':yazilarim} )