from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from record.models import Record, Day, Menu
# Create your views here.

def index(request):
    template = loader.get_template("record/index.html")
    records = Record.objects.order_by("data")
    #days = Day.objects.order_by("time")
    #menu = Menu.objects.order_by()
    context = {"records":records}
    return HttpResponse(template.render(context, request))