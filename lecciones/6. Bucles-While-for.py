##Empezamos con los bucles
###Vamos a usar valores boolean para analizar la condición

###While
a = 11

while a >= 0: #Esta condición puede tener un valor true o false
    #print(a)
    a -= 1
    
###Bucles for
mi_lista = ['Toulouse', 'Montevideo', 'Cordoba', 'Lisboa']

for x in mi_lista: #Con el bucle for vamos a tener una forma de recorrer una lista, donde la variable x (en este caso) va a ir tomando el valor de cada elemento de la lista
    print(x)
    
    
###Palabras reservadas break y continue
#La palabra reservada break va a servir para terminar un bucle en un momento determinado

mi_coleccion = {1,2,3,4,5,6,7,8,9,10}
i = 1

print("Parte del break con while")
while i < 10:
    if i == 5:
        break
    else:
        print(i)
        i += 1

print("Parte del bucle for con break")
for x in mi_coleccion:
    if x == 8:
        break
    else:
        print(x)

#La palabra continue sirve para SALTAR una iteracción de un bucle
print("Parte del continue con for")

for x in mi_coleccion:
    if x == 5:
        continue
    else:
        print(x) 

