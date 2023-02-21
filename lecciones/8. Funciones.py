#Funciones nos van a servir para poder reutilizar código sin tener que volver a escribirlo

#Elementos de una función: 
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


#Funciones con un numero de argumentos variables
def suma_de_x_numeros(*args):
    suma = 0
    for x in args:
        suma += x
    print(suma)
    
suma_de_x_numeros(1,2,3,4,5,6,7,8,9,10,11,12)

def lista_viewers(*args):
    for x in args:
        print(x)


lista_viewers('snow','gold','julian','elon')

#Argumentos variables pero con formato diccionario
def suma_diccionario(**kargs):
    i = 0
    for clave, valor in kargs.items():
        print(clave + " = " + str(valor))
        i += valor
    print(i)
    
suma_diccionario(x=3,y=2)

#
def perro(a):
    print("Mi perro se llama " + a)
    
perro(a = "Txaku")

def loro(tension, estado='muerto', accion='explotar', tipo='Azul Nordico'):
    print('----------')
    print("Este loro no va a " + accion)
    print("si le aplicas " + str(tension) + " voltios")
    print("Gran plumaje tiene el " + tipo)
    print("Esta " + estado +"!")

loro(3000)
loro(1000, estado='vivo')
loro(1000, accion ="volar")