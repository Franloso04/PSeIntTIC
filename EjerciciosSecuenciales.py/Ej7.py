minutos = int(input("Indica la cantidad de minutos empleados: "))

hora = minutos / 60
horas = "{:.0f}".format(hora)

print("Has dedicado", horas, "horas")