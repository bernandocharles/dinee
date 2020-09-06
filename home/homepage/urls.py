from django.urls import path
from home.homepage import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('services/', views.services, name='services'),
    path('blog/', views.blog, name='blog'),
    path('faq/', views.faq, name='faq'),
    path('post/<postnumber>', views.blogpost, name='post')
]
