#------------------------------------------------------------------------------------------------------------------------------
# Declaramos una variable
calificacion = input("introduce tu calificacion de la AZ-900: ")

calificacion = int(calificacion)

#Preguntamos si la calificaion es menor a 700
if calificacion < 700 : # : es para indicar que empieza el if, el tabulador le da a entender que pertenece al mismo ciclo
    print("Vees. por no estudiar xD") # Si es menor a 700, muestra esto
elif calificacion > 1000 : # Si sobre pasa los 1000
    print("Estas mal prr, eso es imposible")
else : # Si no se cumple el if anterior, pasa a esta linea
    print("A huevo prr como el atlas, pasa por tu certificado") # Se ejecuta si ninguno de los if se cumple
#------------------------------------------------------------------------------------------------------------------------------
# Verificacor de edad
edad = input("Introduce tu edad: ")
edad = int(edad)

if edad >= 18 and edad <= 100 :
    print("Exelente, eres cancha oficial")
elif edad > 100 : # elif es igual al else if
    print("Si te fio alv!")
elif edad < 0 :
    print("Eres un sperman aun jajaja xd")
else :
    print("Eres ilegar, vete alv!")
# NO HAY SWITCH CASE EN PYTHON
