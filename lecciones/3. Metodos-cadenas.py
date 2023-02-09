miTexto = "hOla, que tAl estAis ?"
miTextoCapitalizado = miTexto.capitalize()
print(miTextoCapitalizado)

miTextoEnMinus = miTexto.lower()
print(miTextoEnMinus)
miTextoEnMayus = miTexto.upper()
print(miTextoEnMayus)

miTextoCambiado = miTextoEnMinus.replace('a','i')
print(miTextoCambiado)

print(miTextoEnMinus.find('hola'))
print(miTexto[0])


miLista = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto']
miCadena = ', '.join(miLista)
miSegundaCadena = '-'.join(miLista)
print(miCadena)
print(miSegundaCadena)

help(str)
