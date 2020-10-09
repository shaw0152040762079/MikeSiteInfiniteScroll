from django.contrib import admin
from django.urls import path, include
from . import views
from . import views
from django.contrib.staticfiles.urls import static
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = [
                  path('', views.home, name='home'),
                  path('add', views.add, name='add'),
                  path('meme', views.meme, name='meme'),
                  path('story', views.story, name='story'),
                  path('art', views.art, name='art'),
                  path('test', views.meme,  name='test'),
                  path('definitions', views.definitions, name='definitions'),
                  path('experiment', views.experiment, name='experiment'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
