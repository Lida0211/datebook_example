from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from record.models import Record, Day, Menu
from record.forms import RecordForm
# Create your views here.

def index(request):
    template = loader.get_template("record/index.html")
    records = Record.objects.order_by("data")
    #days = Day.objects.order_by("time")
    #menu = Menu.objects.order_by()
    context = {"records":records}
    return HttpResponse(template.render(context, request))


def index_id(request, record_id):
    template = loader.get_template("record/index_id.html")
    record = Record.objects.get(pk = record_id)
    #days = Day.objects.order_by("time")
    #menu = Menu.objects.order_by()
    context = {"record":record}
    return HttpResponse(template.render(context, request))

def create_record(request):
    if request.method =='POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            record = form.save()
            return redirect("record", record_id = record.pk)
    else:
        form = RecordForm()
    return render(request, "record/create_record.html", {"form":form})


def edit_record(request, record_id):
    record = Record.objects.get(pk=record_id)
    if request.method =='POST':
        form = RecordForm(request.POST, instance=record)
        if form.is_valid():
            record = form.save()
            return redirect("record", record_id = record.pk)
    else:
        form = RecordForm(instance=record)
    return render(request, "record/edit_record.html", {"form":form, "record":record})

def delete_record(request, record_id):
    pass