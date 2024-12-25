#módulo estándar que proporciona acceso a variables y funciones del intérprete, así como interacción con el entorno en el que se está ejecutando el programa.
import sys
print(sys.path)

# módulo estándar para trabajar con expresiones regulares, lo que permite buscar, emparejar, dividir o manipular texto de una manera muy eficiente y flexible.
import re
text = 'Mi numero de telefono es 310 132 324, el codigo del pais es 57, mi numero de la suerte es 3'
resultado = re.findall('[0-9]+', text)
print(resultado)

#módulo estándar que proporciona funciones para trabajar con el tiempo, como obtener la hora actual, pausar la ejecución de un programa y medir la duración de operaciones
import time
timestamp = time.time()
local = time.localtime()
result = time.asctime(local)
print(timestamp)
print(result)

#módulo estándar que proporciona clases de contenedores adicionales y especializadas. Estas estructuras de datos extienden las capacidades de los contenedores nativos como listas, diccionarios y tuplas, haciéndolas más eficientes o adaptables a casos específicos.
import collections
numbers = [1,1,2,1,2,2,2,2,1,1,2,1,2,3,3,2,1,2,3]
counter = collections.Counter(numbers)
print(counter)
