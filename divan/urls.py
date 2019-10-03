from django.contrib import admin
from django.urls import include,path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.anasayfa, name='anasayfa'),
    path('yazilar/', include('yazilar.urls'), name='yazilar'),
]

urlpatterns += staticfiles_urlpatterns()