print("Introduce los datos del primer punto ")
x1 = int(input("x: "))
x2 = int(input("y: "))

print("Introduce los datos del segundo punto ")
y1 = int(input("x: "))
y2 = int(input("y: "))

distancia = (((abs(x1 - x2)) ** 2) + ((abs(y1 - y2)) ** 2)) ** 0.5

print("La distancia entre dos puntos es", distancia)