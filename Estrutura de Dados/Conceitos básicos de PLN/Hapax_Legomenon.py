import re

with open("texto.txt", 'r') as arquivo:
    texto = arquivo.read()

texto = texto.lower()
freq = dict()
palavras = re.split(r'[., ?, ! , " ", ;, \", ..., :, @, #, +, -, *, / , -, \, , \[, \], \{, \}, \(, \)]', texto)
for i in palavras:
    if(i != '' and i != '-'):
        if(i in freq):
            freq[i]+=1
        else:
            freq[i] = 1

lista = []

for chave,valor in freq.items():
    if valor == 1:
        a = tuple([chave, valor])
        lista.append(a)

n = len(lista)
c = 1
for i in range(n):
    for j in range(n-c):
        if lista[j] > lista[j+1]:
            a = lista[j]
            lista[j] = lista[j+1]
            lista[j+1] = a
    c+=1

for i in lista:
    print(i[0])