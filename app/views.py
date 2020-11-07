from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'app/home.html')

def contacto(request):
    return render(request, 'app/contacto.html')

def terminos_condiciones(request):
    return render(request, 'app/terminos-condiciones.html')

def registro(request):
    return render(request, 'app/registro.html')