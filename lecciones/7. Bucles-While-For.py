#Un bucle nos permite ejecutar un fragmento de código X veces
#Tenemos los bucles While y For

#While: van a ejecutar un código mientras que una condición sea verdad
# == si dos valores son iguales ( 3 == 5) -> false
# != si dos valores no son iguales ( 3 != 5) -> true

numero = 0

while numero <= 10:
    print("Mi numero es " +str(numero))
    numero += 1 #numero = numero + 1

#podremos crear un bucle infinito si nos interesa    
respuesta = input("Es una tupla un valor mutable en Python?: ")
while respuesta != "No":
    respuesta = input("Incorrecto, intentalo de nuevo: ")
    
print("Bravo")

#Bucle FOR
#Va a servir para recorrer una colección de datos (tupla, una lista y un conjunto)

ciudades = ['Toulouse', 'Montevideo', 'Cordoba', 'Lisboa', 'Paris', 'Madrid', 'Barcelona']

print("La ciudad es " + ciudades[0])
print("La ciudad es " + ciudades[1])
print("La ciudad es " + ciudades[2])
print("La ciudad es " + ciudades[3])

print("-------")


#Usando un bucle for podremos recorrer la colección de datos de una forma más eficiente
#En cada iteracción, el valor que recorramos de la colección será almacenado en la variable que indiquemos
#después del for, en este caso ciudades
#en la primera iteracción ciudad = ciudades[0]
#en la segunda iteracción ciudad = ciudades[1]...

for ciudad in ciudades:
    print("La ciudad es " + ciudad)
    
print("El bucle for se ha acabado")