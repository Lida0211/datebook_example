from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from record.models import Record, Day, Menu
from record.forms import RecordForm, DayForm, MenuForm
from django.contrib import messages
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

def create_day(request):
    if request.method =='POST':
        form = DayForm(request.POST)
        if form.is_valid():
            day = form.save()
            record_pk = day.record.id
            return redirect("record", record_id=record_pk)
    else:
        form = DayForm()
    return render(request, "record/create_day.html", {"form":form})

def edit_record(request, day_id):
    day = get_object_or_404(Day, pk=day_id)
    record = day.record 
    if request.method == 'POST':
        form = DayForm(request.POST, instance=day)
        if form.is_valid():
            form.save()
            return redirect('record', record_id=record.id)
    else:
        form = DayForm(instance=day)
    return render(request, 'record/edit_record.html', {'form': form, 'day': day, 'record': record})

def delete_day(request, day_id):
    day = get_object_or_404(Day, pk=day_id)
    record_id = day.record.id
    if request.method == 'POST':
        day.delete()
        messages.success(request, 'Запись успешно удалена')
        return redirect('record', record_id=record_id)

    return render(request, 'record/delete_day.html', {'day': day, 'record_id': record_id})


def delete_record(request, record_id):
    record = get_object_or_404(Record, pk=record_id)
    if request.method == 'POST':
        record.delete()
        return redirect('records') 
    
    return render(request, "record/delete_record.html", {"record": record})

def create_menu(request, record_id=None):
    record = get_object_or_404(Record, pk=record_id) if record_id else None
    menu = Menu.objects.filter(record=record).first() if record else None
    if request.method == 'POST':
        form = MenuForm(request.POST, instance=menu)
        if form.is_valid():
            menu = form.save(commit=False)
            if record:
                menu.record = record
            menu.save()
            return redirect('record', record_id=menu.record.id if menu.record else 1)
    else:
        form = MenuForm(instance=menu)

    if record:
        form.fields['record'].initial = record
    
    return render(request, "record/create_menu.html", {
        "form": form,
        "menu": menu,
        "record": record
    })
    



def edit_menu(request, record_id):
    
    record = get_object_or_404(Record, pk=record_id)
    menu = get_object_or_404(Menu, record=record) 
    
    if request.method == 'POST':
        form = MenuForm(request.POST, instance=menu)
        if form.is_valid():
            form.save()
            messages.success(request, 'Меню успешно обновлено')
            return redirect('record', record_id=record.id)
    else:
        form = MenuForm(instance=menu)
    
    return render(request, "record/edit_menu.html", {
        "form": form,
        "record": record,
    })