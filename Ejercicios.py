#Ejercicios del fichero de moodle "Exercicios de Python"
#7.6.1

tupla1 = (4,7,2,9,11,13,20)
tupla2 = (2,3,4,5,6,7,8,9)


#Uso de for en Python: (ver info en libro o internet)
#no va el Range???
"""for i in Range(0, tupla1.__sizeof__(), 1):
    if tupla1[i] < tupla1[i+1]:
        marca1 = True"""

#Usando otro tipo de for y funciones:
def comprobarOrden(tupla):
    marca2 = True
    anterior = tupla[0]
    for elemento in tupla:
        if elemento < anterior:

             marca2 = False

             break

        anterior = elemento;
    if marca2 == True:
         print("ordenada de menor a mayor")
    else:
         print("no ordenado")

comprobarOrden(tupla2)




#7.6.2.1

#duplas del domino:
#si, por ejemplo, las duplas tuvieran más valores, podríamos hacer un for "a lo java" para que recorriese to' automáticamente
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
        print("Las fichas("+str(ficha1[0]) + "," + str(ficha1[1]) + ") ("+ str(ficha2[0]) + ","+ str(ficha2[1]) + ") encajan")

    else:
        print("no encajan")


#Obviamente la función puede recibir duplas directamente o variables de duplas
domino((1,2),(4,2))


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

def campanhaElectoral (nombres):
    for elemento in nombres:
        if elemento[1] == 'M':
            print("Estimado" + elemento[0])


#campanhaElectoral(("Juan",'M'), ("Pepe","M"), ("Maria","F"))



#7.6.5 ACABAR



#9.5.1
#LISTA de tuplas a Diccionario
#Las tuplas de la lista solo podrán tener 2 elementos, lo que será la clave y el valor de cada elemento del diccionario

#Para poner varios valores en una misma clave, creamos una lista la lista como Valor
tuplasAlmacen = [("1","Clavo"),("2","Tuerca"),("1","Tornillo"),("3","Tenazas")]

def tuplasADiccionario(lista):

        diccionario = dict()
        listaValoresTemporal = list()
        listaValores2 = list()

        for tupla in lista:

            for tupla2 in lista:

                if tupla[0] == tupla2[0]:
                    #siempre almacena el primer valor independientemente de que se repita o no
                    listaValoresTemporal.extend(tupla2[0])

            listaValores2.extend(listaValoresTemporal)
            listaValoresTemporal.clear()
            diccionario[tupla] = listaValores2

        return diccionario

print(tuplasADiccionario(tuplasAlmacen))











