#Realizar un programa que dada una cadena de caracteres por caracteres, genere otra cadena resultado de invertir la primera.
cadena=input("Introduce una cadena ")
long=len(cadena)-1

while long>=0:
    print(cadena[long])
    long=long-1