#Pide una cadena y un carácter por teclado (valida que sea un carácter) y muestra cuantas veces aparece el carácter en la cadena.
cadena= input("Dime una cadena")
caracter= input("Dime un caracter").upper()
contador=0

caracter=ord(caracter)
if (caracter>=65 and caracter<=90):
    print("El caracter es valido")
    for aux in cadena:
        if (ord(aux.upper())==caracter):
            contador=contador+1
            

print("El caracter aparece " , contador, " veces")