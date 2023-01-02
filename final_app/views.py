from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from final_app.models import Producto, Curso
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
def save_producto(request):
    if request.method == 'POST':
        codigo = request.POST['codigo']
        nombre = request.POST['nombre']
        precio_compra = request.POST['precio_compra']
        precio_venta = request.POST['precio_venta']
        fecha_compra = request.POST['fecha_compra']
        estado = request.POST['estado']
 
        producto = Producto(
            codigo = codigo,
            nombre = nombre,
            precio_compra = precio_compra,
            precio_venta = precio_venta,
            fecha_compra = fecha_compra,
            estado = estado
        )
        producto.save()
        messages.success(request, f'Se agregó correctamente la producto {producto.id}')
        return redirect('crear_producto')
    else:
        return HttpResponse("<h2>No se ha podido registrar el curso</h2>")

def crear_curso(request):
     return render(request, 'crear_curso.html', {
        'titulo': 'Inicio',
        'mensaje': 'Examen Final'
    })
def save_curso(request):
    if request.method == 'POST':
        codigo = request.POST['codigo']
        nombre = request.POST['nombre']
        horas = request.POST['horas']
        creditos = request.POST['creditos']
        estado = request.POST['estado']
 
        curso = Curso(
            codigo = codigo,
            nombre = nombre,
            horas = horas,
            creditos = creditos,
            estado = estado
        )
        curso.save()
        messages.success(request, f'Se agregó correctamente la curso {curso.id}')
        return redirect('crear_curso')
    else:
        return HttpResponse("<h2>No se ha podido registrar el curso</h2>")


