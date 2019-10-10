#Ejercicios del fichero de moodle "Exercicios de Python"
#7.6.1
print("7.6.1")
tupla1 = (4,5,6,3,11,13,20)
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

comprobarOrden(tupla1)




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
print("7.6.3.1")
def campanhaElectoral (nombres):
    for nombre in nombres:
        print("Estimado" + nombre)

campanhaElectoral(("Juan", "Pepe", "Pedro"))

#7.6.3.2
print("7.6.3.2")

def campanhaElectoral (nombres, origen, num):
    #debemos utilizar el "slicing"
    for nombre in nombres[origen:num+1]:
        print("Estimado" + nombre)

campanhaElectoral(("Juan", "Pepe", "Pedro"),0,1)


#7.6.3.3
print("7.6.3.3")
def campanhaElectoral (nombres):
    for elemento in nombres:
        if elemento[1] == 'M':
            print("Estimado " + elemento[0])
        elif elemento[1] == 'F':
            print("Estimada " + elemento[0])


campanhaElectoral((("Juan",'M'), ("Pepe","M"), ("Maria","F")))


#7.6.5.1
print("7.6.5.1")

listaNum = [1,44,6,2,8,11, 13, 7, 23]

def listaPrimos(lista):

    cont = 1;
    primos = list();
    contNum = 0

    for elemento in lista:
        while cont < 10:
            if elemento % cont == 0:

                cont = cont +1
                contNum = contNum + 1
            else:
                cont = cont + 1


        if contNum <= 2 and elemento != 2:
            primos.append(elemento)
            cont = 1
            contNum = 0

        else:
            cont = 1
            contNum = 0

    print(primos)

listaPrimos(listaNum)




#9.5.1
#(podemos hacerlo de la manera fácil, donde no se repiten claves)
#LISTA de tuplas a Diccionario
#Las tuplas de la lista solo podrán tener 2 elementos, lo que será la clave y el valor de cada elemento del diccionario

#Para poner varios valores en una misma clave, creamos una lista la lista como Valor
print("9.5.1")
tuplasAlmacen = [("1","Clavo"),("2","Tuerca"),("1","Tornillo"),("3","Tenazas")]

def tuplasADiccionario(listaT):

        diccionario = dict()

        for tupla in listaT:
            if tupla[0] in diccionario:
                #Si el valor existe en el diccionario, haremos una lista y utilizaremos "append" para AÑADIRLE un elemento
                #Aquí tenemos que ASUMIR que esa lista ya existe
                #AGREGAR VALORES A UNA CLAVE EN UN DICCIONARIO:
                diccionario[tupla[0]].append(tupla[1])
            else:
                #Todos los valores serán una lista, que creamos aquí
                #Creamos la lista cada vez que se inicia el bucle para limpiarla de los valores anteriores !!!
                lista2 = list()
                lista2.append(tupla[1])
                diccionario[tupla[0]] = lista2

        return diccionario

print(tuplasADiccionario(tuplasAlmacen))


#9.5.2.1 !!!
#Podemos pasar un String a Mayus o Minus con "upper" y "lower" para evitar diferenciación de mayus y minus
print("9.5.2.1")
#CÓMO QUITAR TILDES DE UNA STRING??
cad = "Que lindo dia que hace hoy"

def contarPalabras(cadena):



    diccionario2 = dict()
    listaPalabras = cadena.split(" ")

    for palabra in listaPalabras:

        if palabra in diccionario2:

            diccionario2[palabra] = diccionario2[palabra] + 1

        else:

            diccionario2[palabra] = 1

    return diccionario2

#En la llamada a la función podemos hacer que la string sea toda en mayus o en minus para más precisión
print(contarPalabras(cad.upper()))


#9.5.2.2
"""Escribir una función que cuente la cantidad de apariciones de cada carácter en una
cadena de texto, y los devuelva en un diccionario"""

cad2 = "Esto es una cadena de texto"

#EN PYTHON, LOS STRING CUENTAN COMO COLECCIÓN, SE PUEDEN RECORRER COMO SI FUERAN UNA ESPECIE DE "LISTA DE CARACTERES"
#Entonces, cogiendo el ejercicio anterior, solo borrando el "listaPalabras = cadena.split(" ")" ya iría
#SI METEMOS UNA CADENA EN UNA LISTA, CADA ELEMENTO DE LA LISTA SERÁ UN CARACTER DE LA CADENA, INCLUYENDO LOS ESPACIOS
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



"""Función que pase lista de temperaturas en Farenhait a Celsius,devolviendo otra lista"""
"""tiene que usar map con lambdas"""
"""y otra versión con solamente los corchetes []"""

listaFaren = [13,40,60,75]

print("forma 1")
listaCels = map(lambda temp : (temp -32)/1.8 ,listaFaren)
for elemento in listaCels:
    print(elemento)
#Para que aparezca como lista: ?
#podemos hacerlo con append

print("forma2")
listaCels2 = [(temp -32)/1.8 for temp in listaFaren]
print(listaCels2)








