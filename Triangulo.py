n=int(input("Dime el primer lado del triangulo"))
m=int(input("Dime el segundo lado del triangulo"))
x=int(input("Dime el tercer lado del triangulo"))
if ((n==m) and (m==x)):
    input("El triangulo es equilatero")
if ((n!=m) or (m!=x) or (n!=x)):
    input("El triangulo es escaleno")
else:
        input("El triangulo es isosceles")

