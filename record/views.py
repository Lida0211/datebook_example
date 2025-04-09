from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from record.models import Record, Day, Menu
from record.forms import RecordForm, DayForm, MenuForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
# Create your views here.

@login_required
def index(request):
    records = Record.objects.filter(user=request.user).order_by("data")
    return render(request, "record/index.html", {"records": records})

@login_required
def index_id(request, record_id):
    record = get_object_or_404(Record, pk=record_id, user=request.user)
    return render(request, "record/index_id.html", {"record": record})

@login_required
def create_record(request):
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.user = request.user
            record.save()
            return redirect("record", record_id=record.pk)
    else:
        form = RecordForm()
    return render(request, "record/create_record.html", {"form": form})

@login_required
def create_day(request):
    if request.method == 'POST':
        form = DayForm(request.POST)
        if form.is_valid():
            day = form.save(commit=False)
            day.user = request.user 
            day.save()
            return redirect("record", record_id=day.record.id)
    else:

        form = DayForm()
        form.fields['record'].queryset = Record.objects.filter(user=request.user)
    
    return render(request, "record/create_day.html", {"form": form})

@login_required
def edit_record(request, day_id):
    day = get_object_or_404(Day, pk=day_id, record__user=request.user)
    record = day.record
    if request.method == 'POST':
        form = DayForm(request.POST, instance=day)
        if form.is_valid():
            form.save()
            return redirect('record', record_id=record.id)
    else:
        form = DayForm(instance=day)
    return render(request, 'record/edit_record.html', {'form': form, 'day': day, 'record': record})

@login_required
def delete_day(request, day_id):
    day = get_object_or_404(Day, pk=day_id, record__user=request.user)
    record_id = day.record.id
    if request.method == 'POST':
        day.delete()
        messages.success(request, 'Запись успешно удалена')
        return redirect('record', record_id=record_id)
    return render(request, 'record/delete_day.html', {'day': day, 'record_id': record_id})

@login_required
def delete_record(request, record_id):
    record = get_object_or_404(Record, pk=record_id, user=request.user)
    if request.method == 'POST':
        record.delete()
        return redirect('records')
    return render(request, "record/delete_record.html", {"record": record})
@login_required
def create_menu(request):
    if request.method == 'POST':
        form = MenuForm(request.POST)
        if form.is_valid():
            menu = form.save(commit=False)
            menu.user = request.user 
            menu.save()
            return redirect("record", record_id=menu.record.id)
    else:

        form = MenuForm()
        form.fields['record'].queryset = Record.objects.filter(user=request.user)
    
    return render(request, "record/create_menu.html", {"form": form})


@login_required
def edit_menu(request, record_id):
    record = get_object_or_404(Record, pk=record_id, user=request.user)
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