#Función normal
def increment(x):
    return x + 1

#Función lambda
increment_v2 = lambda x : x +1

resultado = increment(10)
print(11)

resultado = increment_v2(20)
print(resultado)

#Lambda de varios argumentos
full_name = lambda name, last_name : f'Full name is {name.title()} {last_name.title()}'

text = full_name('nicolas', 'PEREZ')
print(text)
    