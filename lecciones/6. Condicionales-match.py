mes = "Febrer"
numero = 0

#Match nos evita usar muchos if-elif anidados

if mes == "Enero":
    numero = 1
elif mes == "Febrero":
    numero = 2
elif mes == "Marzo":
    numero = 3
elif mes == "Abril":
    numero = 4
elif mes == "Mayo":
    numero = 5
elif mes == "Junio":
    numero = 6
    
#Match equivale a Switch() en otros lenguajes de programacion
#Está disponible a partir de Python 3.09
#Si funcionamiento es analizar un valor y ejecutar, según coincide con los case
#Un código u otro

match mes: 
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
    case _: #Default
        numero = 13

print(numero)
        
    