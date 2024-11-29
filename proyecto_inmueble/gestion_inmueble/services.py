from gestion_inmueble.models import Comuna, Region,User, Profile


def listarComunas():
    lista = Comuna.objects.all()
    return lista

def getProfile(rut):
    try:
        u = Profile.objects.get(rut=rut)
        return u
    except Exception as ex:
        return ex

def addUser(username, password):
    try:
        user = User(username=username, password=password, is_active=True)
        user.save()
        return user
    except Exception as ex:
        return ex
    
def addRegion(id, nombre):
    try:
        r = Region(id_region=id, nombre_region=nombre)
        r.save()
        return r
    except Exception as ex:
        return ex
    
def delRegion(id):
    try:
        Region.objects.get(id_region=id).delete()
        return True
    except Exception as ex:
        return ex
    
    

