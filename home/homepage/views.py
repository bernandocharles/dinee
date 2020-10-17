from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth.models import User
from home.homepage import search
from home.models import Blogpost
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
    return render(request, template + "homepage.html")

def aboutus(request):
    #project = Project.objects.get(pk=pk)
    #context = {"project": project}
    return render(request, template + "aboutus.html")

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
        "category": 'else'
    }
    return render(request, template + "blog.html", blogdata)

def blogcategory(request, category):
    #project = Project.objects.get(pk=pk)
    #context = {"project": project}
    blogdata = {
        "blogposts": Blogpost.objects.order_by('published_date').reverse(),
        "pagenumber": range(1, int(pagenumber) + 1, 1), # needs to be range to be iterable on template
        "category": category
    }
    return render(request, template + "blog.html", blogdata)

def blogpost(request, postnumber):
    data = {
        "postnumber": int(postnumber),
        "post": Blogpost.objects.get(id=postnumber)
    }
    return render(request, template + 'blogpost.html', data)

def blogsearch(request, characters):
    searchresult = search.forblog(characters)
    searchdata = {
        "blogposts": searchresult,
        "searchcount": len(searchresult),
        "characters": characters,
        "pagenumber": range(1, int(4)) # needs to be range to be iterable on template
    }
    return render(request, template + "blogsearch.html", searchdata)

def faq(request):
    #project = Project.objects.get(pk=pk)
    #context = {"project": project}
    return render(request, template + "faq.html")

def jsontest(request):
    testdata = {
        "foo": "bar",
        "FU": "BAR"
    }
    return JsonResponse(testdata)

def getuser(request, userid):
    user = User.objects.get(id=userid)
    print(user.__dict__)
    print("Knock knock console.")

    return JsonResponse({
        "username": user.username,
        "id": user.id
    })
