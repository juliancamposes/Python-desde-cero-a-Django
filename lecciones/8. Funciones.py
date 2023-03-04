#Funciones nos van a servir para poder reutilizar código sin tener que volver a escribirlo

# Elementos de una función: 
# def: palabra reservada para declarar una función
# nombre de la funcion
# (): van a servir para pasar parámetros o valores a la función que luego se utilizarán dentro de ello
# return: sirve para devolver un valor cuando la función se ejecute


#Funcion para imprimir la serie de Fibonacci hasta n
def fib(n):
    a, b = 0, 1
    while b < n:
        print(b)
        a = b
        b = a+b
        
fib(20000)
fib(1000)

#Función con return
def suma(a,b):
    return a + b
    
suma_dos_numeros = suma(4, 3)
print(suma_dos_numeros)

print('-- Argumentos variables en formato tupla')

def suma_x_numeros(*args):
    result = 0
    for x in args:
        result += x
    print(result)
    
suma_x_numeros(1,2,6534,213,671235)

print('-- Argumentos variables en formato diccionario')

def suma_diccionario(**kargs):
    result  = 0
    for clave,valor in kargs.items():
        print(clave + ' = ' +str(valor))
        result += valor
    print(result)

suma_diccionario(x=3,y=4)

print('-- Argumentos con valores predeterminados')

def perro(a = 'Txaku'):
    print('Mi perro se llama ' + a)
    
perro(a = 'Perrito')

def loro(tension, estado='muerto', accion='explotar', tipo='Azul Nordico'):
    print('-------')
    print('Este loro no va a ' + accion)
    print('si le aplicas ' + str(tension) +' voltios')
    print('Gran plumaje tiene el ' + tipo)
    print('Esta ' + estado + '!')
    
loro(10)
loro(10, estado='vivo')
loro(10, accion='volar')
loro(10, estado = 'vivo', accion='volar')