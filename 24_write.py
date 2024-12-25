with open('./text.txt', 'r+') as file:
    for line in file:
        print(line)
    file.write('\nNuevas cosas en este archivo\n')
    file.write('Nueva linea 2\n')
    file.write('Nueva linea 3\n')
    file.write('Nueva linea 4\n')
    
#Con 'w+' Se reescribe el archivo 