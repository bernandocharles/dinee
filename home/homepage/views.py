from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth.models import User
from home.homepage import search
from home.models import Blogpost
from home.models import Question
##from utils import utils

template = 'home/homepage/'
dataset_list = 'CEP_OVO_DS_DEV.OVO_ref_province_DEV'

pagenumber = len(Blogpost.objects.order_by('published_date')) / 12 + 1

#def homepage(request):
    ##conn = utils.get_kinetica_conn()
    ##cursor = conn.cursor()
    ##cursor.execute("SELECT * FROM " + dataset_list)
    ##lists = cursor.fetchall()
    ##print(lists)
    ##cursor.close()
    ##conn.close()
    ##return render(request, template + 'homepage.html')
    ##return HttpResponse("I want to eat and go")


def homepage(request):
    #project = Project.objects.get(pk=pk)
    #context = {"project": project}
    data = {
        "blogposts": Blogpost.objects.order_by('published_date').reverse(),
        "homepage": True
    }
    return render(request, template + "homepage.html", data)

def aboutus(request):
    data = {
        "aboutus": True
    }
    #project = Project.objects.get(pk=pk)
    #context = {"project": project}
    return render(request, template + "aboutus.html", data)

def services(request):
    #project = Project.objects.get(pk=pk)
    #context = {"project": project}
    return render(request, template + "services.html")

def blog(request):
    #project = Project.objects.get(pk=pk)
    #context = {"project": project}
    blogdata = {
        "blogposts": Blogpost.objects.order_by('published_date').reverse(),
        "pagenumber": range(1, int(pagenumber) + 1, 1), # needs to be range to be iterable on template
        "category": 'else',
        "blog": True
    }
    return render(request, template + "blog.html", blogdata)

def blogpost(request, postnumber):
    post = Blogpost.objects.get(id=postnumber)
    recommended = search.blogcategory(post.category)
    data = {
        "postnumber": int(postnumber),
        "post": post,
        "recommendation": recommended,
        "blog": True
    }
    return render(request, template + 'blogpost.html', data)

def blogsearch(request, characters):
    searchresult = search.forblog(characters)
    pages = len(searchresult) / 12 + 1
    searchdata = {
        "blogposts": searchresult,
        "searchcount": len(searchresult),
        "characters": characters,
        "pagenumber": range(1, int(pages) + 1, 1), # needs to be range to be iterable on template
        "blog": True
    }
    return render(request, template + "blogsearch.html", searchdata)

def blogrestoran(request):
    searchresult = search.blogcategory('restoran')
    pages = len(searchresult) / 12 + 1
    searchdata = {
        "blogposts": searchresult,
        "category": 'Tentang Restoran',
        "pagenumber": range(1, int(pages) + 1, 1),
        "blog": True
    }
    return render(request, template + "blogsearch.html", searchdata)

def blogpelanggan(request):
    searchresult = search.blogcategory('pelanggan')
    pages = len(searchresult) / 12 + 1
    searchdata = {
        "blogposts": searchresult,
        "category": 'Tentang Pelanggan',
        "pagenumber": range(1, int(pages) + 1, 1),
        "blog": True
    }
    return render(request, template + "blogsearch.html", searchdata)

def faq(request):
    faqdata = {
        "restoran": search.faqrestoran(),
        "pelanggan": search.faqpelanggan(),
        "faq": True
    }
    #project = Project.objects.get(pk=pk)
    #context = {"project": project}
    return render(request, template + "faq.html", faqdata)

def faqsearch(request, characters):
    searchdata = search.forfaq(characters)
    #project = Project.objects.get(pk=pk)
    #context = {"project": project}
    return render(request, template + "faq.html", searchdata)

def syarat(request):
    return render(request, template + "syarat.html")

def privasi(request):
    return render(request, template + "privasi.html")
