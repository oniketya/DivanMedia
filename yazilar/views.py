from django.shortcuts import render
from django.http import HttpResponse
from .models import Yazi

def yazilar(request):
   return render(request, 'yazilar/yazilar.html')

def koseyazilari(request):
    yazilarim = Yazi.objects.all()
    return render(request,'yazilar/koseyazilari.html',{'yazilarim':yazilarim})

def analiz(request):
    yazilarim = Yazi.objects.all()
    return render(request, 'yazilar/analiz.html',{'yazilarim':yazilarim})
    
def yazilitarih(request):
    yazilarim = Yazi.objects.all()
    return render(request, 'yazilar/yazilitarih.html',{'yazilarim':yazilarim})
    
def makale(request):
    yazilarim = Yazi.objects.all()
    return render(request, 'yazilar/makale.html',{'yazilarim':yazilarim})

def tekyazi(request, yaziId):
    try:
        yazi = Yazi.objects.get(pk=yaziId)
    except Yazi.DoesNotExist:
        return render(request,'yazilar/yazibulunamadi.html')
    return render(request,'yazilar/tekyazi.html',{'yazi':yazi},)