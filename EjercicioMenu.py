def mostrarmenu():
    seleccion=0
    while(seleccion<1 or seleccion>6):
        print("1-Ejercicio 1")
        print("2-Ejercicio 2")
        print("3-Salir")
      
        try:
            seleccion =int( input("Selecciona una opcion:"))
        except:
            seleccion=0
            print("Ten cuidado con lo que tecleas")
        if(seleccion<1 or seleccion>3):
            print("las opciones son hasta 3")
    return seleccion
mostrarmenu()