from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .forms import ExcelForm
from .models import Registro
import pandas as pd
from io import BytesIO
from django.http import HttpResponse
import json
import csv


def index(request):
    return render(request, 'index.html', {})

# Vista para subir el archivo Excel y converƟrlo en registros
def cargar_excel(request):
    if request.method == 'POST' and request.FILES['excel_file']:
        excel_file = request.FILES['excel_file']
        df = pd.read_excel(excel_file)
        # Asumiendo que el archivo Excel Ɵene las columnas: 'nombre', 'edad', 'email'
        for _, row in df.iterrows():
            Registro.objects.create(
            nombre=row['nombre'],
            edad=row['edad'],
            email=row['email']
            )
        return HttpResponse("Archivo cargado y datos insertados en la base de datos.")
    form = ExcelForm()
    return render(request, 'cargar_excel.html', {'form': form})

# Vista para exportar registros a Excel
def exportar_excel(request):
    registros = Registro.objects.all()
    data = {
    'nombre': [r.nombre for r in registros],
    'edad': [r.edad for r in registros],
    'email': [r.email for r in registros]
    }
    df = pd.DataFrame(data)
   
    # Crear el archivo Excel
    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False)
    output.seek(0)
    response = HttpResponse(output.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="registros.xlsx"'
    return response

# Vista para exportar registros a CSV
def exportar_csv(request):
    registros = Registro.objects.all()
    # Preparamos la respuesta CSV
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="registros.csv"'
    writer = csv.writer(response)
    writer.writerow(['nombre', 'edad', 'email']) # Cabeceras del archivo CSV
    for registro in registros:
        writer.writerow([registro.nombre, registro.edad, registro.email])
    return response


# Vista para exportar registros a JSON
def exportar_json(request):
    registros = Registro.objects.all()
    # ConverƟr los registros a una lista de diccionarios
    data = [
    {'nombre': r.nombre, 'edad': r.edad, 'email': r.email}
    for r in registros
    ]
    # Preparamos la respuesta JSON
    response = HttpResponse(json.dumps(data), content_type='application/json')
    response['Content-Disposition'] = 'attachment; filename="registros.json"'
    return response
