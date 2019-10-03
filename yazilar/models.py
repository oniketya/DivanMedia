from django.db import models
from django.utils import timezone


class Yazi(models.Model):
    baslik = models.CharField(max_length=30)
    icerik = models.TextField()
    tarih = models.DateTimeField('tarih',auto_now_add=True)
    baglanti = models.CharField(max_length=15)
    secenekler = (
        ('K', 'Kose Yazisi'),
        ('A', 'Analiz'),
        ('Y', 'Yazili Tarih'),
        ('M', 'Makale')
    )
    kategori = models.CharField(max_length=1, choices=secenekler)   
    
    def __str__(self):
        return self.baslik

    def kisaicerik(self):
        return self.icerik[:600]