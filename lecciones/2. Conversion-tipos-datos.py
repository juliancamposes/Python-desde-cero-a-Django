#En Python podemos convertir un tipo de dato en otro siempre y cuando sean compatibles
#Podremos pasar de int a float y viceversa, convertir una cadena de texto "2" a un int.. pero no una cadena "Julian" a Int
#Tendremos que usar un poco la lógica

#Aquí las posibles conversiones en Python

#Conversión de Int a Float
mi_numero = 3
mi_numero_float = float(mi_numero)
print(mi_numero_float)

#Conversión de Float a Int
mi_float = 2.88 #es tipo float
mi_float_int = int(mi_float)
print(mi_float_int)

#Conversión de Int a String
mi_numero_str = str(mi_numero)
print(mi_numero_str)
print("Mi numero es " + mi_numero_str)

#Conversión de String a Int
mi_str_para_int = "2"
print(int(mi_str_para_int))

#Conversión de Boolean a String
mi_boolean = True
mi_boolean_str = str(mi_boolean)
print(mi_boolean_str)

#Conversión de String a Boolean
mi_str = "True"
mi_str_boolean = bool(mi_str)
print(mi_boolean_str)

#Conversión de String a Tupla y Lista
mi_str_tuple = tuple(mi_str)
print(mi_str_tuple)
mi_str_set = set(mi_str)
print(mi_str_set)

#Conversión de tupla a lista
mi_tuple_list = set(mi_str_tuple)
print(mi_tuple_list)

#Conversión de lista a tupla
mi_list_tuple = tuple(mi_tuple_list)
print(mi_list_tuple)

