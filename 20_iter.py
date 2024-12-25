#Bucle convencional
for i in range(1, 10):
    print(i)

#Iterar de forma manual  
my_iter = iter(range(1, 4))
print(my_iter)
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
#Excepción por no poder hacer más iteraciones
print(next(my_iter))


