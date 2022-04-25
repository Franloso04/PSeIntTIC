
examen1 = float(input("1º Examen: "))
examen2 = float(input("2º Examen: "))
examen3 = float(input("3º Examen: "))

examenfinal = float(input("Examen final: "))
trabajo = float(input("Trabajo final: "))

parciales = ((examen1 + examen2 + examen3) / 3) * 0.55
examenf = examenfinal * 0.30
trabajof = trabajo * 0.15

nota = parciales + examenf + trabajof

print("Tu nota final será", nota)