numbers = []
for element in range(1, 11):
    numbers.append(element * 2)

print(numbers)

#Comprehensión de lista
numbers_v2 = [element * 2 for element in range(1,11)]
print(numbers_v2)

numeros = []
for i in range(1, 11):
    if i % 2 == 0:
        numeros.append(i * 2)

print(numeros)

#Comprehensión de lista con condicional
numeros_v2 = [i * 2 for i in range(1,11) if i % 2 ==  0]