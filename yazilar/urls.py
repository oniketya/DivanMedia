from django.urls import include,path
from . import views

app_name = 'yazilar'
urlpatterns = [
    path('', views.yazilar),
    path('koseyazilari/', views.koseyazilari, name='koseyazilari'),
    path("analiz/", views.analiz, name="analiz"),
    path("yazilitarih/", views.yazilitarih, name="yazilitarih"),
    path("makale/", views.makale, name="makale"),
    path('<yaziId>/', views.tekyazi, name='tekyazi')
]
