from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('index.html', views.index , name='index'),
    path('about.html', views.about , name='about'),
    path('contact.html', views.contact , name='contact'),
    path('do.html', views.do , name='do'),
    path('portfolio.html', views.portfolio , name='portfolio'),     
    path('thank-you/', views.thank_you, name='thank_you'),
    path('gallery/', views.gallery, name='gallery'),  
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)