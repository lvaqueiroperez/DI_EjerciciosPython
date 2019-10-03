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
#(podemos hacerlo de la manera fácil, donde no se repiten claves)
#LISTA de tuplas a Diccionario
#Las tuplas de la lista solo podrán tener 2 elementos, lo que será la clave y el valor de cada elemento del diccionario

#Para poner varios valores en una misma clave, creamos una lista la lista como Valor
tuplasAlmacen = [("1","Clavo"),("2","Tuerca"),("1","Tornillo"),("3","Tenazas")]

def tuplasADiccionario(listaT):

        diccionario = dict()

        for tupla in listaT:
            if tupla[0] in diccionario:
                #Si el valor existe en el diccionario, haremos una lista y utilizaremos "append" para añadirle un elemento
                #Aquí tenemos que ASUMIR que esa lista ya existe
                diccionario[tupla[0]].append(tupla[1])
            else:
                #Todos los valores serán una lista, que creamos aquí
                lista2 = list()
                lista2.append(tupla[1])
                diccionario[tupla[0]] = lista2

        return diccionario

print(tuplasADiccionario(tuplasAlmacen))


#9.5.2 !!!
#Podemos pasar un String a Mayus o Minus con "upper" y "lower" para evitar diferenciación de mayus y minus
cad = "Qué lindo día que hace hoy"

def contarPalabras(cadena):

    diccionario2 = dict()
    listaPalabras = cadena.split(" ")

    for palabra in listaPalabras:

        if palabra in diccionario2:

            diccionario2[palabra] = diccionario2[palabra] + 1

        else:

            diccionario2[palabra] = 1

    return diccionario2

print(contarPalabras(cad))

#9.5.2.2
"""Escribir una función que cuente la cantidad de apariciones de cada carácter en una
cadena de texto, y los devuelva en un diccionario"""

cad2 = "Esto es una cadena de texto"

#EN PYTHON, LOS STRING CUENTAN COMO COLECCIÓN, SE PUEDEN RECORRER COMO SI FUERAN UNA ESPECIE DE "LISTA DE CARACTERES"
#Entonces, cogiendo el ejercicio anterior, solo borrando el "listaPalabras = cadena.split(" ")" ya iría

def contarCaracteres(cadena):

    diccionario2 = dict()
    listaPalabras = cadena

    for palabra in listaPalabras:

        if palabra in diccionario2:

            diccionario2[palabra] = diccionario2[palabra] + 1

        else:

            diccionario2[palabra] = 1

    return diccionario2

print(contarCaracteres(cad2))












