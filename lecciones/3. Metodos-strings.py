## Vamos a estudiar los métodos existentes para trabajar y manipular Strings

# String con el que vamos a trabajar
mi_texto = "hOla quE tAl estais?"

#Capitalizar el texto
mi_texto_capitalizado = mi_texto.capitalize()
print(mi_texto_capitalizado)

#Poner todas las letras de un texto en minúsculas
print(mi_texto.lower())

#Poner todas las letras de un texto en mayúsculas
print(mi_texto.upper())

#Reemplazar una letra por otra
mi_nuevo_texto = mi_texto.replace('A','i')
print(mi_nuevo_texto)

#Encontrar la posición de  un elemento dentro de una cadena, si no se encuentra la posición será -1
print(mi_texto.find('quE'))

#Convertir lista en string
mi_lista = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto']
mi_lista_en_str = '-'.join(mi_lista)
print(mi_lista_en_str)

#convertir string en listas
mi_nueva_lista = mi_lista_en_str.split('-')
print(mi_nueva_lista)
mi_nuevo_string = "Hola que tal estas muy bien gracias"
print(mi_nuevo_string.split(' '))

#averiguar el tamaño de un string
print(len(mi_nuevo_string))