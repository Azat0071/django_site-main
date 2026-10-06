from django.contrib import admin
from django.urls import path

from main.views import home,noutbooks

urlpatterns = [
    path('admin/', admin.site.urls),
    # меню
    path('', home, name='home'),
    path('noutbooks/', noutbooks, name='noutbooks')
]

