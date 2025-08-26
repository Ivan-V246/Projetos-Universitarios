import re
import nltk

nltk.download('stopwords')
stopwords = nltk.corpus.stopwords.words('portuguese')

with open("texto.txt", 'r') as arquivo:
    texto = arquivo.read()

texto = texto.lower()
palavras = re.split(r'[., ?, ! , " ", ;, \", ..., :, @, #, +, -, *, / , -, \, , \[, \], \{, \}, \(, \)]', texto)
for i in palavras:
    if i != '' and i != '-' and not i in stopwords:
            print(i, end = " ")
