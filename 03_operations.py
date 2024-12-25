set_a = {'col', 'mex', 'bol'}
set_b = {'pe', 'bol'}

#Nos permite hacer la unión entre los 2 conjuntos
set_c = set_a.union(set_b)
print(set_c)
#Otra forma de unirlos
print(set_a | set_b)

#Nos permite hacer la intesección entre los 2 conjuntos
set_c = set_a.intersection(set_b)
print(set_c)
#Otra forma de intesectarlos
print(set_a & set_b)

#Nos permite obtener los elementos que tiene solamente el primer conjunto respecto al otro
set_c = set_a.difference(set_b)
print(set_c)
#Otra forma de hacerlo
print(set_a - set_b)

#Nos permite obtener los elementos de ambos conjuntos, pero excluyendo los que están en ambos conjuntos
set_c = set_a.symmetric_difference(set_b)
print(set_c)
#Otra forma de hacerlo
print(set_a ^ set_b)