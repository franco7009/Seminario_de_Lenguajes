def crearEstructura():
    with open(r"nombres_1.txt", encoding="UTF-8") as nombres:
        nombres = nombres.read()
    with open(r"eval1.txt") as eval1:
        eval1 = eval1.read()
    with open(r"eval2.txt") as eval2:
        eval2 = eval2.read()

    nombres = nombres.replace(",", "").replace("'", "").lower().split()
    eval1 = eval1.replace(",","").split()
    eval2 = eval2.replace(",","").split()
    notas = {}
    for alumno in range(len(nombres)):
        nota = (int(eval1[alumno]) + int(eval2[alumno]))
        notas[nombres[alumno]] = nota
    return notas

def calcularPromedio(notas):
    promedio = 0
    for alumno in notas:
        promedio+= notas[alumno]
    return int(promedio / len(notas))


def promediosBajos(notas, promedio):
    bajos = {}
    for alumno in notas:
        if(notas[alumno] < promedio):
            bajos[alumno] = notas[alumno]
    return bajos



notas = crearEstructura()
promedio = calcularPromedio(notas)
prom_bajos = promediosBajos(notas, promedio)


print(f'Alumnos con promedio menor a {promedio}')

for alumno in prom_bajos:
    print(f'{alumno}\t{prom_bajos[alumno]}'.capitalize())