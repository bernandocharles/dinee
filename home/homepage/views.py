from django.shortcuts import render
from django.http import HttpResponse
##from utils import utils

template = 'home/homepage/'
dataset_list = 'CEP_OVO_DS_DEV.OVO_ref_province_DEV'

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
    return render(request, template + "blog.html")

def blogpost(request):
    return render(request, template + 'blogpost.html')

def faq(request):
    #project = Project.objects.get(pk=pk)
    #context = {"project": project}
    return render(request, template + "faq.html")

