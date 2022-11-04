from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.LoginView),
    path("login", views.LoginView, name="login"),
    path("register", views.RegisterView, name="register"),
    path("logout", views.Logout, name="logout")
]

# Yüklenen resimlerin lokasyonunu belirlenmek için kullanıldı.
urlpatterns += static(settings.STATIC_URL, document_root=settings.MEDIA_ROOT)
