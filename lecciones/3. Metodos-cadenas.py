mi_texto = "hOlA quE Tal EstAis?"

mi_texto_capitalizado = mi_texto.capitalize()
print(mi_texto_capitalizado)

mi_texto_minus = mi_texto.lower()
print(mi_texto_minus)

mi_texto_mayus = mi_texto.upper()
print(mi_texto_mayus)

mi_texto_i = mi_texto.replace('A', 'i')
print(mi_texto_i)

print(mi_texto.find('quE'))

mi_lista = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto']
mi_lista_en_str = ', '.join(mi_lista)
print(mi_lista_en_str)

long = len(mi_texto)
print(long)