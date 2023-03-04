try:
    edad = input("Inserte su edad: ")
    print('Hola')
    print(2022 - edad)
except ValueError:
    print('Oops un error de ValueError ha ocurrido')
except TypeError:
    print('Oops un error TypeError ha ocurrido')
except RuntimeError:
    print('Oops un error RuntimeError ha ocurrido')
except:
    print('Ooops un error desconocido ha ocurrido')
finally:
    print('Esto se va a ejecutar siempre')