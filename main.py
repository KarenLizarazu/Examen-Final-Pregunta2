from estudiante import Estudiante
from administrativo import Administrativo
from docente import Docente

# Crear un solo ejemplo de cada clase
personaX = Estudiante("Carla", "Soto", "2568928", "1999-10-05", "Administracion")
personaY = Administrativo("Pedro", "Rios", "25568745", "1997-08-09", "Cajero")
personaZ = Docente("Ivan", "Claros", "2584758", "1984-07-09", "Noche")

# Mostrar datos de cada persona
print(personaX.mostrar_datos())
print(personaY.mostrar_datos())
print(personaZ.mostrar_datos())