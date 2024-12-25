import random

dict = {}
for i in range(1,5):
    dict[i] = i * 2

print(dict)

#Comprehensión de diccionario
dict_v2 = {i: i * 2 for i in range(1, 5)}
print(dict_v2)

countries = ['col', 'mex', 'bol']
population = {}
for country in countries:
    population[country] = random.randint(1,100)

print(population)

#Comprehensión de diccionario
population_v2 = {country: random.randint(1,100) for country in countries}
print(population_v2)

names = ['Nico', 'Zule', 'Santi']
ages = [15, 23, 17]
#Juntar ambas listas
print(list(zip(names, ages)))

new_dict = {name: age for (name, age) in zip(names, ages)}
print(new_dict)