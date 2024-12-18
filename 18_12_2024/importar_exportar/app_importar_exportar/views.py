from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .forms import ExcelForm
from .models import Registro
import pandas as pd
from io import BytesIO
from django.http import HttpResponse

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
    response = HttpResponse(output, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="registros.xlsx"'
    return response
