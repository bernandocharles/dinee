from django.urls import include, path
from . import views

urlpatterns = [
    path('', include('home.homepage.urls')),
]