from django.shortcuts import render
from yazilar.models import Yazi

def anasayfa(request):
    yazilar = Yazi.objects.all().order_by('-tarih')[0:4]
    return render(request,'anasayfa.html',{'yazilar':yazilar})