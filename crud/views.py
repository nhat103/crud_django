from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from crud.models import Users

# Create your views here.


def show(request):
    users = Users.objects.all()
    template = loader.get_template('show.html')
    return HttpResponse(template.render({'users': users}))
