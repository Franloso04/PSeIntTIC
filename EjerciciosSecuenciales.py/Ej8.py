base = int(input("Indica tu salario base: "))
ventas = int(input("Indica el número de ventas realizadas este mes: "))

comision = base * 0.1

total = base + (comision * ventas)

print("Has obtenido ", total, "euros este mes")