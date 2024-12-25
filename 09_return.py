def find_vol(length = 1, width = 1, depth = 1):
    return length * width * depth, width, 'hola'

resultado, width, texto = find_vol(width=5, depth=28)

print(resultado)
print(width)
print(texto)