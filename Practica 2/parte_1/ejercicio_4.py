

evaluar = """ título: Experiences in Developing a Distributed Agent-based Modeling Toolkit
with Python
resumen: Distributed agent-based modeling (ABM) on high-performance computing resources
provides the promise of capturing unprecedented details of large-scale complex systems.
However, the specialized knowledge required for developing such ABMs creates barriers to
wider adoption and utilization. Here we present our experiences in developing an initial
implementation of Repast4Py, a Python-based distributed ABM toolkit. We build on our
experiences in developing ABM toolkits, including Repast for High Performance Computing
(Repast HPC), to identify the key elements of a useful distributed ABM toolkit. We leverage
the Numba, NumPy, and PyTorch packages and the Python C-API to create a scalable modeling
system that can exploit the largest HPC resources and emerging computing architectures.
"""
titulo, resumen = evaluar.split("resumen: ")[0], evaluar.split("resumen: ")[1]


titulo = len(titulo.split(" ")) - 1
print(f"Cantidad palabras título: {titulo}")

resumen = resumen.split(".")

facil = 0
aceptable = 0
dificil = 0
muy_dificil = 0

for frase in resumen:
    palabras = frase.split(" ")

    if len(palabras) <= 12:
        facil+=1
    elif ((len(palabras) >= 13) and (len(palabras) <= 17)):
        aceptable+=1
    elif ((len(palabras) >= 18) and (len(palabras) <= 25)):
        dificil+=1
    else:
        muy_dificil+=1


print(f"facil: {facil}")
print(f"aceptable: {aceptable}")
print(f"dificil: {dificil}")
print(f"muy dificil: {muy_dificil}")

