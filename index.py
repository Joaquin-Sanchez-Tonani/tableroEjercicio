a = "O"
b = "H"
linea = 0
contador = 0
tamano = int(input("De manera vertical: ¿Cuál es la cantidad de casillas que queres en tu tablaro?"))

def tablero(casillas):
    global linea, contador
    for i in range(tamano):
        if linea % 2 == 0:
            for i in range(tamano):
                if i % 2 == 0:
                    print(a, end=" ")
                else: 
                    print(b, end=" ")
        else: 
            for i in range(tamano):
                if i % 2 == 0:
                    print(b, end=" ")
                else: 
                    print(a, end=" ")
        print()
        linea += 1
tablero(tamano)