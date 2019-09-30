#7.6.1

tupla1 = (4,7,2,9,11,13,20)
tupla2 = (2,3,4,5,6,7,8,9)
marca1 = False


#Uso de for en Python: (ver info en libro o internet)
#no va?
"""for i in Range(0, tupla1.__sizeof__(), 1):
    if tupla1[i] < tupla1[i+1]:
        marca1 = True"""





#usando otro tipo de for y funciones:
def comprobarOrden(tupla):
    marca2 = True
    anterior = tupla2[0]
    for elemento in tupla2:
        if elemento < anterior:
            print("no ordenado")
            marca2 = False

            break

        anterior = elemento;
        if marca2:
            print("ordenada de menor a mayor")



comprobarOrden(tupla2)

#7.6.2.1

#duplas del domino:

def domino(ficha1,ficha2):
    encajan = False
    if ficha1[0] == ficha2[0]:
        encajan=True
    elif ficha1[1] == ficha2[0]:
        encajan = True
    elif ficha1[0] == ficha2[1]:
        encajan = True
    elif ficha1[1] == ficha2[1]:
        encajan = True

    if encajan:
        print("Las fichas("+str(ficha1[0]) + "," + str(ficha1[1]) + ") ("+ str(ficha2[0]) + " , "+ str(ficha2[1]) + ") encajan")

    else:
        print("no encajan")



domino((1,2),(4,3))


#7.6.7

listaTuplas = [("Vaqueiro","Luis","A"),("Fernandez","Maria","J"),("Vazquez","Pepe","X")]

listaCadenas = []
#también vale listaCadenas = list()

def nombresOrdenados(lista):

    for tupla in lista:

        cadena = tupla[1] + " " + tupla[2] + ". " + tupla[0]

        listaCadenas.append(cadena)

    return listaCadenas


print(nombresOrdenados(listaTuplas))


#7.6.3.1

def campanhaElectoral (nombres):
    for nombre in nombres:
        print("Estimado" + nombre)

campanhaElectoral(("Juan", "Pepe", "Pedro"))

#7.6.3.2

def campanhaElectoral (nombres, origen, num):
    for nombre in nombres[origen:num+1]:
        print("Estimado" + nombre)

campanhaElectoral(("Juan", "Pepe", "Pedro"),0,1)


#7.6.3.3 ACABAR

def campanhaElectoral (nombres, origen, num):
    for elemento in nombres[origen:num+1]:
        print("Estimado" + elemento[0])

campanhaElectoral(("Juan", "Pepe", "Pedro"),0,1)

