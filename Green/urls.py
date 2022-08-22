from django.contrib import admin
from django.urls import path

import Green.views

urlpatterns = [
    path('', Green.views.homePage())
]