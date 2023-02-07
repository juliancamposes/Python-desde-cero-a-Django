#Tipos de datos en Python
##Datos inmutables: no se pueden modificar una vez en la memoria
miInt = 2 #Datos numéricos enteros positivos
miString = 'Esto es una cadena de texto' #Cadenas de texto
miTupla = (1,2,3,'Toulouse') #Conjunto de valores dentro de una misma variable, identificados por un índice y no modificable

##Datos mutables
miBoolean = True #Indica que es verdadero
miBoolean = False #Indica que es falso
miFloat = 9.3 #Datos numéricos decimales y negativos, modificables en la memoria
miFloat = -3 
miListas = [1,2,3,4] #Conjunto de datos dentro de una misma variable, indetificados por un índice pero sí son modificables
miListas[0] = 2

diccionario = {
    "primerValor" : 3,
    "segundoValor" : 'Julian',
    "tercerValor" : True,
    "cuartoValor" : (1,2,3)
} #conjuntos de datos dentro de una mismas variables, modificable e indentificados por un valor escrito, semejantes a los JSON

miConjunto = {1,2,3,4,1,2,3,4} #conjuntos de datos dentro de una misma variables, pero sin valores repetidos
