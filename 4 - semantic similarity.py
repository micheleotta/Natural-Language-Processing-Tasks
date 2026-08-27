# -*- coding: utf-8 -*-

import nltk
from nltk.corpus import wordnet as wn
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('wordnet')
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')

def words_similarity(p1, p2):
  synsets1 = wn.synsets(p1)
  synsets2 = wn.synsets(p2)
  if not synsets1 or not synsets2:
    return 0
  return synsets1[0].wup_similarity(synsets2[0]) or 0

sentence1 = input("Type first sentence: ")
sentence2 = input("Type second sentence: ")
# examples
# sentence1 = "The dog is chasing the cat in the garden."
# sentence2 = "A dog runs after a cat in the yard."

# standardize
sentence1 = sentence1.lower()
sentence2 = sentence2.lower()

# split words -> tokenization
sentence1 = word_tokenize(sentence1)
sentence2 = word_tokenize(sentence2)
print("Tokenization")
print(sentence1)
print(sentence2)

# remove punctuation
sentence1 = [word for word in sentence1 if word.isalnum()]
sentence2 = [word for word in sentence2 if word.isalnum()]

# extract key words, remove stopwords
stop_words = set(stopwords.words('english'))
sentence1 = [w for w in sentence1 if w.lower() not in stop_words]
sentence2 = [w for w in sentence2 if w.lower() not in stop_words]
print("\nKey words")
print(sentence1)
print(sentence2)

similarities = [
    {"word1": p1, "word2": p2, "similarity": words_similarity(p1, p2)}
    for p1, p2 in zip(sentence1, sentence2)
]
# compute average similarity
values = [item['similarity'] for item in similarities]
average = sum(values) / len(values)
print(f"\nFinal semantic similarity: {average:.2f}")

# most similar words' pairs
similarities.sort(key=lambda x: x['similarity'], reverse=True)
top10 = similarities[:10]
print("\nMost similar pairs:")
for item in top10:
    print(f"{item['similarity']:.2f} -> {item['word1']} + {item['word2']}")