#Crea una funcion que devuelva numeros aleatorios que se vayan insertando en una lista
import random
import time
def tiempo(numele):
    lista=[]
    j=0
    inicio=time.time()
    for i in range(numele):
        j=random.randint(0,10)
        lista.append(j)
        time.sleep(0.5)
    time.time()
    return lista
#inicio del programa 
bandera=True 
while bandera==True:
    try:
        numele=int(input("Cuantos elementos quieres introducir"))
        print(tiempo(numele))
        bandera=False
    except:
        print("un numero bobolon")   


