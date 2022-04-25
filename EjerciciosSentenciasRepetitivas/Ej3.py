num = 1 


while num != 0: 
    num = int(input("Introduce una serie de números y los sumare, introduce 0 para salir: "))
    total = num + total
    contador = contador + 1


print("La suma es:", total)

media = total / contador 
print("La media es:", media)