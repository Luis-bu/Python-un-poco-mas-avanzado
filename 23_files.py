#Archivos en Python

file = open('./text.txt')
#Leer todo el archivo
#print(file.read())

#Leer linea por linea
print(file.readline())
print(file.readline())
print(file.readline())


for line in file:
    print(line)

file.close()

#Instrucción para el cierre aútomatico de un archivo
with open('./text.txt') as file:
    for line in file:
        print(line)