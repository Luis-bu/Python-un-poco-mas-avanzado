#No admite elementos duplicados
set_countries = {'col', 'mex', 'bol'}
print(set_countries)
print(type(set_countries))

#Admite también valores númericos
set_numbers = {1, 2, 2, 443, 23}
print(set_numbers)

#Puede tener múltiples tipos de datos en un solo conjunto
set_types = {1, 'hola', False, 12.12}
print(set_types)

#Forma manual de declararlo y divide el string en elementos del
set_from_string = set('hola')
print(set_from_string)

set_from_tupla = set(('abc', 'cbv', 'as', 'abc'))
print(set_from_tupla)

#forma sencilla de eliminar elemntos duplicados de un array
numbers = [1,2,3,1,2,3,4]
set_numbers = set(numbers)
print(set_numbers)
unique_numbers = list(set_numbers)
unique_numbers = list(set_numbers)
print(unique_numbers)
print(len(set_countries))