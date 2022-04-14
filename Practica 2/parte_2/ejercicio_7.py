from collections import Counter

c = Counter(input('Frase o palabra: ').lower()).most_common()

#if (Counter(input('Frase o palabra: ').lower()).most_common()[0][1] > 1):
if (c[0][1] > 1):
    print('No es un heterograma')
else:
    print('Es un heterograma')


