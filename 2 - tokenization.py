# -*- coding: utf-8 -*-

from collections import Counter
import nltk
nltk.download('punkt_tab')
from nltk import tokenize

texts = ["São Paulo, SP, S.P., S. Paulo", "nome@pucpr.br", "CPF: 001.002.003-04"]

print("\nWithout tokenization: ")
for text in texts:
  words = text.replace('\n',' ').replace('\t','').replace(',', ' ').replace('.', ' ').split(' ')
  counter = Counter(words)
  for cont in counter.items():
    print(cont)

print("\nWith tokenization: ")
for text in texts:
  tokenize_words = tokenize.word_tokenize(text)
  print(tokenize_words)
  counter = Counter(tokenize_words)
  for cont in counter.items():
    print(cont)