nums = (int)(input("¿Cuantos numeros vas a introducir? "))
vNum = []
num0 = 0
num1 = 0
num2 = 0
num = 0

for i in range(0,nums):

    num = int(input("Introduce un numero "))
    vNum.append(num)

    if num > 0:
        num1 = num1 + 1
    elif num < 0:
        num2 = num2 + 1
    else:
        num0 = num0 + 1
print("Hay", num1, "mayores de 0,", num2, "menores de 0 y", num0, "iguales a 0")