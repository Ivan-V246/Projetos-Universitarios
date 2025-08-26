import re

with open("texto.txt", 'r') as arquivo:
    texto = arquivo.read()

texto = texto.lower()
freq = dict()
palavras = zre.split(r'[., ?, ! , " ", ;, \", ..., :, @, #, +, -, *, / , -, \, , \[, \], \{, \}, \(, \)]', texto)
for i in palavras:
    if(i != '' and i != '-'):
        if(i in freq):
            freq[i]+=1
        else:
            freq[i] = 1

pares = []

for chave,valor in freq.items():
    a = tuple([chave, valor])
    pares.append(a)

n = len(pares)
c = 1
for i in range(n):
    for j in range(n-c):
        if(pares[j][1] < pares[j+1][1]):
            a = pares[j]
            pares[j] = pares[j+1]
            pares[j+1] = a
        elif (pares[j][1] == pares[j+1][1] and pares[j][0] > pares[j+1][0]):
            a = pares[j]
            pares[j] = pares[j+1]
            pares[j+1] = a
    c+=1

n = int(input("Qual o top x de termos que você gostaria de ver?\n"))

if len(pares) < n:
    n = len(pares)

for i in range(n):
    print(f"Top {i+1}: \"{pares[i][0]}\" que se repetiu {pares[i][1]} vezes.")