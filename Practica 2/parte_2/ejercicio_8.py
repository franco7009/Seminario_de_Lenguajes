valores = {'AEIOULNRST': 1, 'DG': 2, 'BCMP': 3, 'FHVWY': 4, 'K': 5, 'JX':8, 'QZ': 10}

palabra = input('Ingresar palabra: ').upper()

contador = 0

for letra in palabra:
    for valor in valores:
        if (letra in valor):
            contador = contador + valores[valor]

print(f'Puntaje obtenido: {contador}')