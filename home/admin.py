from django.contrib import admin
from .models import Blogpost
from .models import Question

# Register your models here.

admin.site.register(Blogpost)
admin.site.register(Question)
