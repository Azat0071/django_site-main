from django.contrib import admin
from django.urls import path

from main.views import home, smartphones, noutbooks, wathchas, musics

urlpatterns = [
    path('admin/', admin.site.urls),
    # меню
    path('', home, name='home'),
    path('smartphones/', smartphones, name='smartphones'),
    path('noutbooks/', noutbooks, name='noutbooks'),
    path('wathchas/', wathchas, name='wathchas'),
    path('musics/', musics, name='musics'),
]

