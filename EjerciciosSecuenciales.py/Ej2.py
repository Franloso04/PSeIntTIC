print("Indica la medida de los lados del triangulo")
lado1 = int(input("Lado 1: "))
lado2 = int(input("Lado 2: "))
lado3 = int(input("Lado 3: "))

base = int(input("¿Cuanto vale la base?: "))
altura = int(input("¿Cuánto vale la altura?: "))

perimetro = lado1 + lado2 + lado3
area = (base * altura) / 2

print("El perimetro del triangulo es", perimetro, "y el area es", area)