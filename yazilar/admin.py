from django.contrib import admin

from .models import Yazi


class YaziTarihGoster(admin.ModelAdmin):
    readonly_fields = ('tarih',)

admin.site.register(Yazi,YaziTarihGoster)


# Register your models here.
