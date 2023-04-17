from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

from .models import DogPatient
from .forms import BloodReportForm, DogPatientForm
#from .models import DogPatient




def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome, {username}!')
            return redirect('main')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')







def main_view(request):
    if request.user.is_authenticated:
        return render(request, 'main.html')
    else:
        messages.error(request, 'You must be logged in to access this page')
        return redirect('login')






def register_view(request):
    if request.method == 'POST':
        form = DogPatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
    else:
        form = DogPatientForm()
    return render(request, 'register.html', {'form': form})

def success(request):
    return render(request, 'success.html')



def blood_report(request):
    if request.method == 'POST':
        form = BloodReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = BloodReportForm()
    return render(request, 'blood_report.html', {'form': form})

def success(request):
    return render(request, 'success.html')







def search_results(request):
    query = request.GET.get('q')
    if query:
        dog_patients = DogPatient.objects.filter(name__icontains=query)
        return render(request, 'search_results.html', {'dog_patients': dog_patients})
    else:
        return render ( request, 'search_results.html' )


def dog_patient_detail(request, registration_no):
    dog_patient = DogPatient.objects.get(registration_no=registration_no)
    context = {'dog_patient': dog_patient}
    return render(request, 'dog_patient_detail.html', context)
