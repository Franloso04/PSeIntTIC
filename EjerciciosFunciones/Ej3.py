def tempMedia(dias):
    tempMax = 0
    tempMin = 0
    suma = 0
    media = 0

    for i in range(0, dias):
        tempMax = int(input("Introduce la temperatura máxima del día: "))
        tempMin = int(input("Introduce la temperatura mínima del día: "))
        suma = tempMax + tempMin
        media = (int)(suma / 2)
        print("La temperatura media ha sido de: ", media, "\n")

dias = int(input("¿De cuántos días vas a introducir los valores?: "))
tempMedia(dias)