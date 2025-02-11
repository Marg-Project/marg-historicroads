from django.urls import path
from . import views

urlpatterns = [
    path('' , views.home , name = 'home'),
    path('about/' , views.about , name = 'about'),
    path('explore/' , views.explore , name = 'explore'),
    path('identification_documentation/' , views.identification_documentation , name = 'identification_documentation'),
    path('conservation/' , views.conservation , name = 'conservation'),
    path('management/' , views.management , name = 'management'),
    path('network/' , views.network , name = 'network')
]