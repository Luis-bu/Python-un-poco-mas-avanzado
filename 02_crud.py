set_countries = {'col', 'mex', 'bol'}

#Contar la cantidad de elementos en un conjunto
size = len(set_countries)
print(size)

#Verificar elementos en un conjunto
print('col' in set_countries)
print("arg" in set_countries)

#Add ---> Añadir elemento al conjunto
set_countries.add('pe')
print(set_countries)
set_countries.add('pe')
print(set_countries)

#Update ---> Puedes añadir más elementos, puedes enviarle un subconjunto (puede ser arrays, tuplas o otros conjuntos)
set_countries.update({'uru', 'ecu', 'pe'})
print(set_countries)

#Remove ---> Eliminar elemento del conjunto, si no se encuentra, tira error.
set_countries.remove('uru')
print(set_countries)

#discard ---> Eliminar un elemento del conjunto, si no lo encuentra, no pasa nada.
set_countries.discard('arg')
print(set_countries)

#clear ---> Vaciar el conjunto
set_countries.clear()
print(set_countries)
print(len(set_countries))