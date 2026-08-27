# -*- coding: utf-8 -*-

from collections import Counter
import matplotlib.pyplot as plt

n_docs = 0

with open("files/2000_texts.txt", "r", encoding="utf-8") as file:
  counter = Counter()
  for linha in file:
    words = linha.replace('\n',' ').replace('\t','').replace(',', ' ').replace(';', ' ').replace('.', ' ').split(' ')
    counter.update(words)
    n_docs += 1

del counter['']

print(f"Total frequency = {sum(counter.values())}")
print(f"Three most common = {counter.most_common(3)}")

sorted_data = counter.most_common()
keys = [item[0] for item in sorted_data]
values = [item[1] for item in sorted_data]

plt.bar(keys, values)

plt.xticks([])
plt.yticks([])

plt.yscale('log')

plt.savefig('files/2000_texts_frequency.png')
plt.show()