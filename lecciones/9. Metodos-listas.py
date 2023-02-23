# Métodos para manipular listas
# Los objetos tienen lo que se llama métodos
# los métodos son funciones características de un objeto que nos permite realizar una acción con ese objeto
# Para llamar a un método de un objeto, tenemos que instanciar el objeto y utilizar su instancia 
# seguido de un punto, donde luego irá el nombre del método
# objeto1.nombre_Metodo() -> miLista.nombre_del_metodo()

mis_redes = ['Twitter', 'Twitch', 'Instagram']
print(mis_redes)

#Añadir un elemento al final de una lista ya creada previamente
#con el método append() voy a poder añadir un elemento al final de mi lista

mis_redes.append('Youtube') #mis_redes = ['Twitter', 'Twitch', 'Instagram', 'Youtube']
print(mis_redes)

#Añadir un elemento en una posición determinada de nuestra lista
#con el método insert()
#ahora mismo mis_redes = ['Twitter', 'Twitch', 'Instagram', 'Youtube']

mis_redes.insert(1, 'Tiktok')
print(mis_redes)

#Tenemos una función llamada del, que nos permite eleminar un objeto o un elemento de mi lista

#print(mis_redes[2])
#del mis_redes[2]

#con el método pop() voy a eliminar el último elemento de mi lista
print("Mi lista antes de utilizar el metodo pop()")
print(mis_redes)
mis_redes.pop()
print("Mi lista después de utilizar el metodo pop()")
print(mis_redes)

#Con el metodo pop() y el índice 0 (pop(0)) también puedo eliminar el primer elemento de mi lista
mis_redes.pop(0)
print(mis_redes)

#Eliminar un objeto conocimiento su valor con el método remove()

mis_redes.remove('Tiktok')
print(mis_redes)


#Podemos ordernar los elementos de mi lista por un criterio ascendente o descendente
#Utilizaremos el método .sort() (para ordenarlos de forma ascendente) o sort(reverse=True) para descendente
#Y los valores se modificarán dentro de la memoria (variable)



mis_redes.sort()
print(mis_redes)
mis_redes.sort(reverse=True)
print(mis_redes)

#Puedo también con la función sorted() modificar y ordenar mi lista de forma temporal y que los cambios
#no se guarden en la memoria del programa(variable)
#sorted(valor) o sorted(valor,reverse=True)

mis_numeros = [3,1,6,7,12,9]
print(sorted(mis_numeros,reverse=True))

print(mis_numeros)

#podemos ver la longitud o el tamaño de una lista
print(len(mis_redes))

mi_texto = "Hola que tal estais"
print(len(mi_texto))


#Podemos modificar varios valores de una lista de una sola vez indicando un rango

#mis_numeros[0] = 4
#mis_numeros[1] = 2
#mis_numeros[2] = 5

print(mis_numeros)
mis_numeros[0:2] = [4,4,5]
print(mis_numeros)

#Podemos acceder a los elementos de una lista por el final con los índices negativos
print(mis_numeros[-1])

#Podemos invertir el orden de la lista
mis_numeros.reverse()
print(mis_numeros)


#Obtener el índice de la prima vez que aparece un valor
indice = mis_numeros.index(4)
print(indice)

