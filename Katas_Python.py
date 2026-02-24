# %%
#1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados.
cadena_texto = 'Bienvenidos'
for indice, caracter in enumerate(cadena_texto):
    print(f'Índice: {indice}, caracter: {caracter}')

# %%
#2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()
numeros = [1,2,3,4,5,6]
print(numeros)
resultado_map_lambda = list(map(lambda x: x*2, numeros))
print(f'La nueva lista con el doble de cada valor es:{resultado_map_lambda}')

# %%
#3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.
def match_palabras(x,y):
    palabras_generales = []
    palabra_objetivo = ['mente']
    return list(map(lambda x: palabras_generales.intersection(palabra_objetivo), palabras_generales))

palabras_generales = ['Estoy', 'completamente', 'inmerso', 'en', 'el', 'universo', 'Python', 'recientemente']
palabra_objetivo = ['mente']

resultado = match_palabras(palabras_generales, palabra_objetivo)
print(resultado)

# %%
#4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()
def diferencia_listas (lista1, lista2):
    return list(map(lambda x, y: x - y, lista1, lista2))

lista1 = [15, 20, 25, 30]
lista2 = [5, 3, 2, 1]

resultado = diferencia_listas(lista1, lista2)
print (resultado)

# %%
#5. Ecribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver una tupla que contenga la media y el estado.
def evaluar_examen (lista_notas, nota_aprobado=5):
    media = sum(lista_notas) / len(lista_notas)
    if media >= nota_aprobado:
        estado = "aprobado"
    else:
        estado = "suspenso"
    return (media, estado)

lista_notas = [4, 7, 5, 9, 8]

resultado = evaluar_examen(lista_notas)
print(f'El resultado del examen es: {resultado}')

# %%
#6. Escribe una función que calcule el factorial de un número de manera recursiva.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

factorial (4)

# %%
#7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()
def tupla_a_string(mi_tupla):
    return list(map(lambda t: str(t), mi_tupla))

datos = [10, 15, 20, 25]
resultado = tupla_a_string(datos)
print(resultado)


# %%
#8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje indicando si la división fue exitosa o no.
def division_usuario (numerador, denominador):
    try:
        cociente = numerador / denominador
    except ZeroDivisionError:
        return 'No se puede dividir por cero', None
    else: 
        return 'División exitosa', cociente

try: 
    numerador = float(input(f'Ingrese un número positivo: '))
    denominador = float(input(f'Ingrese otro número positivo: '))
except:
    print('Error: Debes ingresar valores numéricos')
else:
    estado, resultado = division_usuario(numerador, denominador)
    print(estado)
    if resultado is not None:
        print(f'Resultado: {resultado}')

# %%
#9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"].Usa la función filter()
def filtrar_animales (lista_animales):
    prohibidos = {'Mapache', 'Tigre', 'Serpiente Pitón', 'Cocodrilo', 'Oso', 'mapache', 'tigre', 'serpiente pitón', 'cocodrilo', 'oso'}
    return list(filter(lambda animal: animal not in prohibidos, lista_animales))

animales = {'Perro', 'gato', 'Serpiente Pitón', 'leopardo', 'tigre', 'Oso', 'mapache', 'Caballo', 'Cocodrilo'}
resultado = filtrar_animales(animales)

print(f'Las mascotas permitidas en España son: {resultado}')

# %%
#10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente.
class ListaVaciaError(Exception):
    pass

def promedio_numeros (lista_numeros):
    if not lista_numeros:
        raise ListaVaciaError('La lista está vacía, no se puede hacer promedio')
    
    return sum(lista_numeros) / len(lista_numeros)

try: 
    numeros = [6, 9, 12, 15, 24]
    resultado = promedio_numeros(numeros)
except ListaVaciaError as error:
    print(f'Error: {error}')
else:
    print(f'El promedio de la lista es: {resultado}')
print('Para este ejercicio me apoyé en ChatGPT sobre el manejo de errores')


# %%
#11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente.
def edad_usuario():
    try:
        edad = int(input('Ingrese su edad: '))
        if edad < 0 or edad > 120:
            raise ValueError('La edad debe estar entre 0 y 120 años')
    except ValueError as e:
        print(f'Error: {e}')
    else:
        print('La edad del usuario es:', edad)


# %%
edad_usuario()

# %%
#12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()
def longitud_palabras(frase):
    palabras = frase.split()
    return list(map(len, palabras))

resultado = longitud_palabras('Hola esto es Python')
print(resultado)


# %%
#12. Alternativa:
def longitud_palabras(frase):
    palabras = frase.split()
    return list(map(lambda palabra: len(palabra), palabras))

resultado = longitud_palabras('Esto utiliza lambda')
print(resultado)


# %%
#13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas. Las letras no pueden estar repetidas .Usa la función map()
def conjunto_caracteres(caracteres):
    caracteres_unicos = set(caracteres)
    return list(map(lambda c: (c.upper(), c.lower()), caracteres_unicos))

caracteres = 'Me encanta Python'
resultado = conjunto_caracteres(caracteres)
print(f'Las letras de mi conjunto de caracteres son: {resultado}')
print('Aquí el argumento de lambda genera la iteración en mínusculas y mayusculas')

# %%
#14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la función filter()
def palabras_con_letra(lista_palabras, letra):
    return list(filter(lambda palabra: palabra.startswith(letra), lista_palabras)) 

lista_palabras = ['Bienvenidos', 'a', 'mis', 'katas', 'de', 'Python']
resultado = palabras_con_letra(lista_palabras, 'P')
print(f'Las palabras que comienzan con la letra P son: {resultado}')
print('Para este ejercicio consulté a ChatGPT sobre como obtener un elemento por su inicial, comprendiendo así el fundamento .startswith()')

# %%
#15. Crea una función lambda que sume 3 a cada número de una lista dada.
def suma_tres(lista_numeros):
    return list(map(lambda numero: numero+3, lista_numeros))

lista_numeros = [4, 6, 9, 12, 17]
resultado = suma_tres(lista_numeros)
print(f'El resultado de sumar 3 a cada número de la lista es: {resultado}')

# %%
#16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de todas las palabras que sean más largas que n. Usa la función filter()
def filtrar_texto(cadena_texto, numero):
    palabras = cadena_texto.split()
    return list(filter(lambda palabra: len(palabra) > numero, palabras))

cadena_texto = 'Esto es una cadena de texto para mi función filtrar texto'
resultado = filtrar_texto(cadena_texto, 4)
print(f'Las palabras de mi cadena_texto con más de 4 caracteres son: {resultado}')


# %%
#17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2] corresponde al número quinientos setenta y dos (572). Usa la función reduce()
from functools import reduce

def lista_a_numero(lista_digitos):
    return reduce(lambda acumulador, digito: acumulador * 10 + digito, lista_digitos)

lista_digitos = [5, 7, 2]
resultado = lista_a_numero(lista_digitos)
print(f'El número resultante es: {resultado}')
print('Para usar la función "reduce" hay que instalarla previamente, y para obtener el número en conjunto multipliqué por 10')

# %%
#18. Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes (nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a 90. Usa la función filter()
estudiantes = [
    {'nombre': 'Laura', 'edad': 23, 'calificacion': 78},
    {'nombre': 'Juan', 'edad': 21, 'calificacion': 90},
    {'nombre': 'Mateo', 'edad': 25, 'calificacion': 93},
    {'nombre': 'Laia', 'edad': 22, 'calificacion': 91},
    {'nombre': 'Jordi', 'edad': 24, 'calificacion': 89}
]

def calificacion_aceptable(estudiante):
    return estudiante['calificacion'] >= 90

estudiantes_filtrados = list(filter(calificacion_aceptable, estudiantes))

print('Estudiantes con califiación >= 90:')
for estudiante in estudiantes_filtrados:
    print(estudiante['nombre'])
print('Aquí entendí sobre la estructura de los diccionarios, y que podemos utilizar diccionarios con varios pares key-value')

# %%
#19. Crea una función lambda que filtre los números impares de una lista dada.
def filtrar_numeros(lista_numeros):
    return list(filter(lambda n: n % 2 != 0, lista_numeros))

lista_numeros = [4, 7, 11, 16, 19, 23, 28]
resultado = filtrar_numeros(lista_numeros)
print(f'Los impares de la lista de números son: {resultado}')

# %%
#20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función filter()
def filtrar_enteros(lista_inicial):
    return list(filter(lambda i: isinstance(i, int), lista_inicial))

lista_inicial = ('Esta', 'lista', 'contiene', 13, 'elementos', 3.0, 'de', 'ellos', 'son', 'números', 'y', 10, 'palabras')
resultado = filtrar_enteros(lista_inicial)
print(f'Los elementos enteros de la lista inicial son: {resultado}')

# %%
#21. Crea una función que calcule el cubo de un número dado mediante una función lambda
def numero_cubo(numeros):
    return list(map(lambda n: n**3, numeros))

numeros = [2, 3, 5, 6]
resultado = numero_cubo(numeros)
print(f'El resultado de los números al cubo es: {resultado}')

# %%
#22. Dada una lista numérica, obtén el producto total de los valores de dicha lista. Usa la función reduce().
from functools import reduce

def producto_total(i, n):
    return i*n

lista_numeros = [2, 4, 3, 5, 6]
resultado = reduce(producto_total, lista_numeros)
print(f'El producto total de los números de la lista es: {resultado}')
print('Como mencioné anteriormente para usar la función "reduce" siempre debe importarse previamente desde functools')


# %%
#23. Concatena una lista de palabras. Usa la función reduce().
from functools import reduce

def concatenar_elementos(s,n):
    return s + n

lista_elementos = ['Bienvenidos ', 'a ', 'mi ', 'lista ', 'de ', 'prueba.']
resultado = reduce(concatenar_elementos, lista_elementos)
print(f'La lista concatenada es: {resultado}')
print('Siempre que usemos reduce, al estar en notebooks independientes de Jupyter, importamos desde functools')


# %%
#24. Calcula la diferencia total en los valores de una lista. Usa la función reduce().
from functools import reduce

def diferencia_total(a,b):
    return a - b

lista_valores = [24, 5, 3, 6, 2]
resultado = reduce(diferencia_total, lista_valores)
print(f'La diferencia de todos los valores de la lista es: {resultado}')
print('Importo la función reduce previamente desde functools')

# %%
#25. Crea una función que cuente el número de caracteres en una cadena de texto dada.

def contabilizar_caracteres(cadena_texto):
    return len(cadena_texto)

cadena_texto = 'Estoy aprendiendo a programar en Python'
resultado = contabilizar_caracteres(cadena_texto)
print(f'El total de caracteres de mi cadena_texto es: {resultado}')

# %%
#26. Crea una función lambda que calcule el resto de la división entre dos números dados.
def resto_cociente(x,y):
    calcular_resto = lambda a, b: a % b
    return calcular_resto(x,y)

resultado = resto_cociente(25, 3)
print(f'El resto de la división de los valores x,y es: {resultado}')

# %%
#27. Crea una función que calcule el promedio de una lista de números.
def calculo_promedio(lista_numeros):
    return sum(lista_numeros) / len(lista_numeros)

lista_numeros = [3, 5, 8, 12, 19]
resultado = calculo_promedio(lista_numeros)
print(f'El promedio de mi lista_numeros es: {resultado}')


# %%
#28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.
def elemento_duplicado(mi_lista):
    vistos = set()
    for elemento in mi_lista:
        if elemento in vistos:
            return elemento
        vistos.add(elemento)
    return None

mi_lista = [3, 5, 6, 9, 6, 11, 5, 14]
resultado = elemento_duplicado(mi_lista)
print(f'El primer duplicado de mi_lista es: {resultado}')
print('Aquí mediante consulta en ChatGPT logré crear un set que llamé "vistos" para aplicar la comparación de elementos entre dos listas')

# %%
#29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el carácter '#', excepto los últimos cuatro.
def conversion_texto(variable):
    texto = str(variable)
    return '#' * (len(texto) - 4) + texto[-4:]

variable = 19922026
resultado = conversion_texto(variable)
print(f'El resultado de mi variable enmascarada es: {resultado}')
print('Me apoyé en ChatGPT sobre como obtener la forma de enmascarar determinados caracteres, lo cual me suguirió: "#" * (len(texto) - "X" caracteres)')

# %%
#30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden.
def detecto_anagrama(palabra1, palabra2):
    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()
    return sorted(palabra1) == sorted(palabra2)

palabra1 = 'Roma'
palabra2 = 'Amor'
resultado = detecto_anagrama(palabra1, palabra2)
print(f'¿Son las palabras un anagrama?: {resultado}')
print('Aquí mediante "sorted()" podemos ordenar cualquier string alfabeticamente para luego compararlos')

# %%
#31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se lanza una excepción.
def ingresar_nombres():
    lista_nombres = input('Ingrese una lista de nombres separados por coma: ')
    
    lista_nombres = lista_nombres.split(',')
    lista_nombres = [nombre.strip() for nombre in lista_nombres]

    buscar_nombre = input('Ingrese el nombre que desea buscar: ')
    if buscar_nombre in lista_nombres:
        print(f'El nombre se ha encontrado con éxito.')
    else:
        raise ValueError(f'El nombre no se encuentra en la lista')
    
print('Con "split" separo las palabras, y luego "strip" descarta los espacios antes o después del nombre')

# %%
ingresar_nombres()

# %%
#32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.
def buscar_empleado(nombre_completo, lista_empleados):
    if nombre_completo in lista_empleados:
        return lista_empleados.index(nombre_completo)
    else:
        return 'Esta persona no trabaja aquí.'
    
lista_empleados = ['Yoko Ono', 'Robert Plant', 'Freddy Mercury', 'John Lennon']
nombre_completo = 'John Lennon'

resultado = buscar_empleado(nombre_completo, lista_empleados)
print(f'El empleado se encuentra en la posición Nro {resultado} de la plantilla de empleados')
print('Aquí "index" devuelve la posición del nombre en la lista')   

# %%
#33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.
def suma_elementos(lista1, lista2):
    return list(map(lambda x, y: x + y, lista1, lista2))

lista1 = [12, 4, 7, 'Roma', 3]
lista2 = [6, 2, 5, 'Italia', 4]

resultado = suma_elementos(lista1, lista2)
print(f'La suma de los elementos es: {resultado}')


# %%
#34.Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son: crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e info_arbol . El objetivo es implementar estos métodos para manipular la estructura del árbol.
    #1. Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
class Arbol:
    def __init__(self):
        self.tronco = 1
        self.ramas = []

#2. Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad.
    def crecer_tronco(self):
        self.tronco += 1
        print(f'El tronco ha crecido en 1 unidad')

#3. Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
    def nueva_rama(self):
        self.ramas.append(1)
        print(f'El árbol tiene una nueva rama')

#4. Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
    def crecer_ramas(self):
        self.ramas += 1
        print(f'Han crecido las ramas de todo el árbol en 1 unidad')

#5. Implementar el método quitar_rama para eliminar una rama en una posición específica.
    def quitar_rama(self, posicion):
        if 0 <= posicion <= len(self.ramas):
            self.ramas.pop(posicion)
        else:
            print('No hay ramas que quitar en esa posición')

#6. Implementar el método info_arbol para devolver información sobre la longitud del tronco, el número de ramas y las longitudes de las mismas.
    def info_arbol(self):
        return {
                'Longitud del tronco': self.tronco,
                'Número de ramas': self.ramas,
                'Longitud de las ramas': len(self.ramas)
                }

# %%
#35. Caso de uso:
#1. Crear un árbol.
mi_arbol = Arbol()

#2. Hacer crecer el tronco del árbol una unidad.
mi_arbol.crecer_tronco()

#3. Añadir una nueva rama al árbol.
mi_arbol.nueva_rama()

#4. Hacer crecer todas las ramas del árbol una unidad.
mi_arbol.crecer_ramas()

#5. Añadir dos nuevas ramas al árbol.
mi_arbol.nueva_rama()

#6. Retirar la rama situada en la posición 2.
mi_arbol.quitar_rama(2)

#7. Obtener información sobre el árbol.
print(mi_arbol.info_arbol())

# %%
#36. Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente. Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y agregar dinero al saldo.
    #1. Inicializar un usuario con su nombre, saldo y si tiene o no cuenta corriente mediante True y False.
class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta = cuenta

#2. Implementar el método retirar_dinero para retirar dinero del saldo del usuario. Lanzará un error en caso de no poder hacerse.
    def retirar_dinero(self, retiro):
        if not self.cuenta:
            raise ValueError('No tiene cuenta bancaria')
        if retiro > self.saldo:
            raise ValueError('No tiene saldo suficiente')
        self.saldo -= retiro

#3. Implementar el método transferir_dinero para realizar una transferencia desde otro usuario al usuario actual. Lanzará un error en caso de no poder hacerse.
    def transferir_dinero(self, otro_usuario, monto):
        if not self.cuenta or not otro_usuario.cuenta:
            raise ValueError('Alguno de los usuarios no tiene cuenta')
        if otro_usuario.saldo < monto:
            raise ValueError('El usuario remitente no tiene saldo suficiente')
        otro_usuario.saldo -= monto
        self.saldo += monto
        
#4. Implementar el método agregar_dinero para agregar dinero al saldo del usuario.
    def agregar_dinero(self, deposito):
        if not self.cuenta:
            raise ValueError('No tiene cuenta bancaria')
        self.saldo += deposito

print('En este ejercicio me ayudé de ChatGPT para el #3 en el manejo de errores, el cual inicialmente pasaba por alto y no contemplaba toda la casuística')

# %%
#Caso de Uso:
#1. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
cuenta_alicia = UsuarioBanco('Alicia', 100, True)
cuenta_bob = UsuarioBanco('Bob', 50, True)

#2. Agregar 20 unidades de saldo de "Bob"
cuenta_bob.agregar_dinero(20)

#3. Hacer una transferencia de 80 unidades desde "Bob" a "Alicia".
cuenta_alicia.transferir_dinero(cuenta_bob, 80)

#4. Retirar 50 unidades de saldo a "Alicia".
cuenta_alicia.retirar_dinero(50)

print('Con los datos del ejericio Bob se queda sin saldo. Para una transferencia exitosa se debe realizar por 60 euros o menos')


# %%
#37. Crea una función llamada procesar_texto que procesa un texto según la opción especificada: contar_palabras, reemplazar_palabras, eliminar_palabra. Estas opciones son otras funciones que tenemos que definir primero y llamar dentro de la función procesar texto.
def contar_palabras(texto):
    palabras = texto.split()
    return len(palabras)

def reemplazar_palabras(texto, palabra_vieja, palabra_nueva):
    return texto.replace(palabra_vieja, palabra_nueva)

def eliminar_palabra(texto, palabra):
    palabras = texto.split()
    return texto.remove(palabra)

def procesar_texto(texto, opcion, palabra_vieja = None, palabra_nueva = None):
    if opcion == 'contar':
        return contar_palabras(texto)
    elif opcion == 'reemplazar':
        return reemplazar_palabras(texto, palabra_vieja, palabra_nueva)
    elif opcion == 'eliminar':
        return eliminar_palabra(texto, palabra_vieja)
    else:
        return 'Opción invalida'
    

# %%
#Caso de Uso: Comprueba el funcionamiento completo de la función procesar_texto:

texto = 'Esta frase es para testear mis funciones de Python'

print(procesar_texto(texto, 'contar'))

print(procesar_texto(texto, 'reemplazar', 'Python', 'Python en mi version 3.14.2'))

print(procesar_texto(texto, 'eliminar', 'Python'))


# %%
#38. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.
hora = int(input('Introduce la hora sin los minutos (en formato numérico 0-24): '))

if 7 <= hora <= 12:
    print('Es de mañana')
elif 12 <= hora <= 19:
    print('Es de tarde')
elif 0 <= hora <= 7 or 19 <= hora <= 24:
    print('Es de noche')
else:
    print('Hora inválida')

# %%
#39. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica. Las reglas de calificación son: 0 - 69 insuficiente, 70 - 79 bien, 80 - 89 muy bien, 90 - 100 excelente.
calificacion = int(input('Ingrese su calificación (de 0 a 100): '))

if 0 <= calificacion <= 69:
    print('Calificación: Insuficiente')
elif 70 <= calificacion <= 79:
    print('Calificacion: Bien')
elif 80 <= calificacion <= 89:
    print('Calificación: Muy Bien')
elif 90 <= calificacion <= 100:
    print('Calificación: Excelente')
else:
    print('Revise su calificación, debe estar entre 0 y 100')

print('Ingreso una calificación de 91 como ejemplo')


# %%
#40. Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo", "triangulo") y datos (una tupla con los datos necesarios para calcular el área de la figura).
def calcular_area(figura, datos):
    x, y = datos
    if figura == 'rectangulo':
        return x * y
    elif figura == 'triangulo':
        return (x * y) / 2
    else:
        return 'Figura incompatible'

# %%
#Utilizo ejemplos con varias figuras para verificar todas las opciones de la función:
print(calcular_area('rectangulo', (5,4)))

print(calcular_area('triangulo', (6,3)))

print(calcular_area('trapecio', (5,4)))

# %%
#41. En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe hacer lo siguiente:
    #1. Solicita al usuario que ingrese el precio original de un artículo.
precio_original = float(input('Ingrese el precio del producto seleccionado: '))

    #2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no).
cupon = input('¿Tienes un cupón de descuento? (si/no): ')
cupon = cupon.lower()
    
    #3. Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento.
if cupon == 'si':
    descuento = float(input('Ingrese el valor del cupón: '))
    
    #4. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido (es decir, mayor a cero). Por ejemplo, descuento de 15€.
    if descuento > 0 and descuento <= precio_original:
        precio_final = precio_original - descuento
    else:
        print('Cupón no válido')
        precio_final = precio_original

elif cupon == 'no':
    precio_final = precio_original
else:
    print('Valor inválido. No es posible aplicar descuento')

    #5. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él.
print(f'El precio final es: {precio_final} €')

    #6. Recuerda utilizar estructuras de control de flujo como if, elif y else para llevar a cabo estas acciones en tu programa de Python.
print('Para ejecutar el código utilizo como precio_original = 199.90 y un cupón de 15 euros como suguiere la consigna')


