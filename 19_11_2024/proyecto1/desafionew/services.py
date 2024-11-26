from desafionew.models import Curso
from desafionew.models import Direccion
from desafionew.models import Estudiante
from desafionew.models import Seccion
from desafionew.models import DetalleSeccion
from desafionew.models import Profesor

def listarEstudiantes():
    estudiantes = Estudiante.objects.all().exclude(activo=False)
    return {"titulo":"Listado de Estudiantes ", "estudiantes" : estudiantes}


def listadoSecciones():
    secciones = Seccion.objects.all()
    lista=[]
    for s in secciones:
        detalle_seccion = s.detalleseccion.all()
        #print(detalle_seccion)
        estudiantes = detalle_seccion.values('estudiante')
        #print(estudiantes)
        detalle = {"titulo":"Listado Sección","seccion":s, "estudiantes":estudiantes}
        lista.append(detalle)

    return lista
            




