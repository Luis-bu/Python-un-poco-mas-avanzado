#División entre cero
#print(0 / 0)
#Variable no declarada
#print(result)
#Finalización del flujo del programa
print('Hola')

#Asser nos ayuda a validar métodos
suma = lambda x,y: x + y
assert suma(2,2) == 4

print("Hola 2")

#Excepción de forma manual
age = 10
if age < 18:
    raise Exception('No se permiten menores de edad')

