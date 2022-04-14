clave = input('Ingresa la clave (debe tener menos de 10 caracteres y no contener los símbolos:@ y !):')

if(len(clave) > 10):
    print('Ingresate mas de 10 caracteres')

if ('@' in clave or '!' in clave):
    print('Ingresaste alguno de estos símbolos: @ o !"')
else:
    print('Clave válida')