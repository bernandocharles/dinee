from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth.models import User
##from utils import utils

template = 'home/homepage/'
dataset_list = 'CEP_OVO_DS_DEV.OVO_ref_province_DEV'

blogposts = ['eatngo', 'Services', 'Payment', 'Restaurant', 'Customer', 'Appetizer', 'Customer', 'Food', 'Beverages', 'Dessert']
colors = ['primary', 'secondary', 'success', 'danger', 'warning', 'info', 'muted', 'dark', 'success', 'info']

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
        "blogposts": blogposts,
        "colors": colors
    }
    return render(request, template + "blog.html", blogdata)

def blogpost(request, postnumber):
    data = {
        "postnumber": postnumber
    }
    return render(request, template + 'blogpost.html', data)

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
