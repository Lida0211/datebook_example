from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from picture.models import Picture

from django.contrib import messages

def picture_main(request):
    return render(request, "picture/picture.html")

def picture(request):
    template = loader.get_template("picture/picture.html")
    pictures = Picture.objects.order_by("data")
    #days = Day.objects.order_by("time")
    #menu = Menu.objects.order_by()
    context = {"pictures":pictures}
    return HttpResponse(template.render(context, request))