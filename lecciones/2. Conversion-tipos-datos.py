##Tipos de conversión (casteo) de datos. Es decir, cómo convertir un dato de un tipo a otro

numero = 3
numeroEnString = str(numero)
numeroEnFloat = float(numero)

numeroEnInt = int(numeroEnFloat)

cadenaTexto = "true"
cadenaEnBoolean = bool(cadenaTexto)

cadenaEnTupla = tuple(cadenaTexto) ## -> ("true")
cadenaEnLista = list(cadenaTexto) ## -> ["true"]
cadenaEnConjunto = set(cadenaTexto) ## -> {"true"}