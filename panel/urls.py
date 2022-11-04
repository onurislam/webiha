from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.index, name="home"),
    path("index", views.index, name="home"),
    path("ihaadd", views.Add, name="ihaadd"),
    path("ihalist", views.List, name="ihalist"),
    path("ihaupdate/<int:id>", views.Update, name="ihaupdate"),
    path("ihadelete/<int:id>", views.Delete, name="ihadelete"),

]

# Yüklenen resimlerin lokasyonunu belirlenmek için kullanıldı.
urlpatterns += static(settings.STATIC_URL, document_root=settings.MEDIA_ROOT)
