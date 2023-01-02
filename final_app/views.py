from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', {
        'titulo': 'Inicio',
        'mensaje': 'Examen Final'
    })

def inicio(request):
     return render(request, 'inicio.html', {
        'titulo': 'Inicio',
        'mensaje': 'Examen Final'
    })
def integrantes(request):
     return render(request, 'integrantes.html', {
        'titulo': 'Inicio',
        'mensaje': 'Examen Final'
    })

def crear_producto(request):
     return render(request, 'crear_producto.html', {
        'titulo': 'Inicio',
        'mensaje': 'Examen Final'
    })

def crear_curso(request):
     return render(request, 'crear_curso.html', {
        'titulo': 'Inicio',
        'mensaje': 'Examen Final'
    })


