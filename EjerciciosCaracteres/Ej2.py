#Realizar un programa que comprueba si una cadena leída por teclado comienza por una subcadena introducida por teclado.
cadena= input("Dime una cadena ")
subcadena= input("Dime una subcadena ")
if (subcadena==cadena[0:len(subcadena)]):
    print("SI comienza por la subcadena introducida por teclado")
else:
    print("NO comienza por la subcadena introducida por teclado")