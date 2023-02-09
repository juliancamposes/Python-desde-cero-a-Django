usuarios = 40

#Vamos a usar diferentes comparadores para ver si algo se cumple o no
# == para ver si un valor es igual a algo (valor == 100)
# < para ver si un valor es menor a algo (valor < 100)
# > para ver si un valor es mayor a algo (valor > 100)
# <= para ver si un valor es menor o igual a algo (valor <= 100)
# >= para ver si un valor es mayor o igual a algo (valor >= 100)

if usuarios < 50:
    print("Cocacola gratis")
elif usuarios < 100:
    print("Dejar pasar usuarios")
else:
    print("No se que hacer")
    

mesNacimiento = "Septiembre"
numero = 0
if mesNacimiento == "Enero":
    numero = 1
elif mesNacimiento == "Febrero":
    numero = 2
    
#Switch, en Python se llama Match
match mesNacimiento:
    case "Enero":
        numero = 1
    case "Febrero":
        numero = 2
    case "Marzo":
        numero = 3
    case "Abril":
        numero = 4
    case "Mayo":
        numero = 5
    case "Junio":
        numero = 6
    case "Julio":
        numero = 7
    case "Agosto":
        numero = 8
    case "Septiembre":
        numero = 9
    case "Octubre":
        numero = 10
    case "Noviembre":
        numero = 11
    case "Diciembre":
        numero = 12
    case _:
        numero = 0

print(numero)