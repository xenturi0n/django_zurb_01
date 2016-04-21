from django.shortcuts import render

def inicio(request):
    return render(request, 'inicio/index.html',{})
    
def prueba(request):
    return render(request, 'inicio/prueba.html', {})
    
def barra_01(request):
    return render(request, 'inicio/barra_01.html', {})