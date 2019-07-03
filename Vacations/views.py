from django.shortcuts import render, redirect
from .models import Vacation
from .forms import VacationForm

# Create your views here.
# list_vacations, create_vacation, update_vacation, delete_vacation

def list_vacations(request):
    vacations = Vacation.objects.all()
    return render(request, 'vacations/index.html', {'vacations': vacations})


def create_vacation(request):
    form = VacationForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('vacations:list_vacations')

    return render(request, 'vacations/vacations-form.html', {'form': form})


def update_vacation(request, id):
    vacation = Vacation.objects.get(id=id)
    form = VacationForm(request.POST or None, instance=vacation)

    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request, 'vacations/vacations-form.html', {'form': form, 'vacation': vacation})


def delete_vacation(request, id):
    vacation = Vacation.objects.get(id=id)

    if request.method == 'POST':
        vacation.delete()
        return redirect('vacations:list_vacations')

    return render(request, 'vacations/delete-vacation.html', {'vacation': vacation})
