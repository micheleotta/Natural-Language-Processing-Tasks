# -*- coding: utf-8 -*-

def dice_coefficient(a, b):
  a = set(a)
  b = set(b)
  c = list(a & b)
  return 2 * len(c) / (len(a) + len(b))

lexicon = ["abacate", "abacaxi", "abobora", "abobrinha", "ananás", "maça", "mamão", "manga", "melancia", "melão", "mexerica", "morango"]
word = input("Type a word: ")

for N in range(2, 5):
  print("\n\n=========================================")
  print(f"N = {N}")

  results = {}

  # N-gram similarity
  word_grams = []
  for i in range(len(word) - (N - 1)):
      word_grams.append(word[i:i+N])

  for p in lexicon:
    grams = []
    for i in range(len(p) - (N - 1)):
      grams.append(p[i:i+N])
    result = dice_coefficient(word_grams, grams)
    results[p] = result

  sorted_results = dict(sorted(results.items(), key=lambda item: item[1], reverse = True))

  threshold = 0.7

  print(f"Closest word to {word}: {next(iter(sorted_results.items()))}")

  print(f"\nSimilar words to {word}:")
  for key, result in sorted_results.items():
    if result >= threshold:
      print(f"{key}: {result}")


  print("\nRESULTS")
  for key, result in sorted_results.items():
    print(f"{key}: {result}")