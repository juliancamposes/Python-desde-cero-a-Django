#IF-ELIF-ELSE
#and va a ser la palabra reservada que nos va a permitir que se analicen dos condiciones
#y solo se cumpla cuando las dos son true

numero_viewers = 25
dia_semana = "Miercoles"

if numero_viewers < 10:
    print("Hoy hay pocos viewers")
elif numero_viewers < 20:
    print("Es la media del canal")
elif numero_viewers < 30:
    print("Hoy estamos por encima de la media")
else:
    print("Hoy el stream es un exito")

print("---------")

if numero_viewers < 10 and dia_semana == "Lunes":
    print("Hoy hay pocos viewers")
elif numero_viewers < 20 and dia_semana == "Martes":
    print("Es la media del canal")
elif numero_viewers < 30 and dia_semana == "Miercoles":
    print("Hoy estamos por encima de la media")
else:
    print("Hoy el stream es un exito")


#or nos sirve para ejecutar un código si una de las dos condiciones se cumplen

numero_viewers = 35
dia_semana = "Martes"
    
if numero_viewers < 10 or dia_semana == "Lunes":
    print("Hoy hay pocos viewers")
elif numero_viewers < 20 or dia_semana == "Martes":
    print("Es la media del canal")
elif numero_viewers < 30 or dia_semana == "Miercoles":
    print("Hoy estamos por encima de la media")
else:
    print("Hoy el stream es un exito")

print("-------")

#El orden es muy importante
numero_usuarios = 10

if numero_usuarios == 30:
    print("A")
elif numero_usuarios == 10:
    print("B")
    