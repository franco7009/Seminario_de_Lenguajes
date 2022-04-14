estructura = [
'-*-*-',
'--*--',
'----*',
'*----',
]

matriz = []
for fila in range(len(estructura)):
    for celda in range(len(estructura[fila])):
        #print(estructura[fila][celda])
        nueva_fila = []
        if (estructura[fila][celda]) == '-':
            print(estructura[fila][celda])
            nueva_fila.append(0)

        #else:
        #    nueva_fila.append('*')
        #    if (celda<len(estructura[fila])):
        #        nueva_fila[celda-1]+=1
        #    if (celda>0):
        #        nueva_fila[celda+1]+=1
    matriz.append(nueva_fila)



