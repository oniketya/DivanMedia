from django.urls import include,path
from . import views

app_name = 'yazilar'
urlpatterns = [
    path('', views.yazilar),
    path('koseyazilari/', views.koseyazilari, name='koseyazilari'),
    path('<yaziId>/', views.tekyazi)
]
