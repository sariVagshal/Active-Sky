from django.contrib import admin
from django.urls import path

from app.views import main_first_window, phon_scan
from . import view
# from app.views import *


urlpatterns = [
    path('phone_scan/', phon_scan.scan, name='phon_scan'),
    path('start/', main_first_window.open_window, name='open_window'),
]

