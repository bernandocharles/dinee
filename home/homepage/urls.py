from django.urls import path
from home.homepage import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('services/', views.services, name='services'),
    path('blog/', views.blog, name='blog'),
    path('blog/category/<category>', views.blogcategory, name='blogcategory'),
    path('blog/<pagenumber>', views.blog, name='blogpages'),
    path('blog/search/<characters>', views.blogsearch, name='blogsearch'),
    path('faq/', views.faq, name='faq'),
    path('faq/<characters>', views.faqsearch, name='faqsearch'),
    path('post/<postnumber>', views.blogpost, name='post'),
    path('syarat-ketentuan/', views.syarat, name='syarat'),
    path('kebijakan-privasi/', views.privasi, name='privasi')
]
