from home.models import Blogpost
from home.models import Question

def forblog(characters):
  result = Blogpost.objects.filter(content__contains=characters)
  return result

def faqrestoran():
  result = Question.objects.filter(category='restoran')
  return result

def faqpelanggan():
  result = Question.objects.filter(category='pelanggan')
  return result

def forfaq(characters):
  pelanggan = Question.objects.filter(question__contains=characters, category='pelanggan')
  restoran = Question.objects.filter(question__contains=characters, category='restoran')
  result = {
    "pelanggan": pelanggan,
    "restoran": restoran,
    "searching": True,
    "searchcount": len(pelanggan) + len(restoran),
    "characters": characters
  }
  return result