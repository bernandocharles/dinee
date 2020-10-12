from home.models import Blogpost

def forblog(characters):
  result = Blogpost.objects.filter(content__contains=characters)
  print(result)
  print('+++++ SEARCHR ESUlt aBOVE ++++++')
  return result

def forfaq():
  print('another')