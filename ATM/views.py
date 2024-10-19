from django.shortcuts import render

def atm_locators(request):
    return render(request, 'AtmLocations.html')