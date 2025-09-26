# El gobierno quiere otorgar becas de excelencia a los estudiantes con un mínimo de un 8 de media.
# Además para acceder a la beca el estudiante debe tener entre 17 y 21 años. Crea un script que
# pida el nombre, la edad y la nota media del estudiante e indique si puede optar a la beca o no.

# Pedimos los datos del alumno
nombre_alumno = input("Nombre del alumno: ")
edad_alumno = int(input("Edad: "))
Nota_Media_Alumno = float(input("Nota media (Para obtener la beca se necesita de media un 8): "))

# Condicion de que si el alumno coincide con todos esos datos, obtendra la beca
if (17 <= edad_alumno >= 21) and (Nota_Media_Alumno >= 8):
    print("El alumno",nombre_alumno.title(),"obtiene la beca")
else:
    # Por el caso de que el alumno no cumpla con la edad minima o con la media de la beca
    # Se le negara la beca
    print("El alumno",nombre_alumno.title(),"no puede obtener la beca")