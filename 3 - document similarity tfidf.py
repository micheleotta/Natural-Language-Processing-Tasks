# -*- coding: utf-8 -*-

from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

corpus = ["O rato roeu a roupa do rei de Roma.",
          "Nenhum rato rói a roupa do rei de Roma sem punição.",
          "A rota de fuga do rato foi rápida."]

# standardize
corpus = [d.lower() for d in corpus]
print(corpus)

# compute TF-IDF
vectorizer = TfidfVectorizer(token_pattern=r'(?u)\b\w+\b') # considers words with 1 or more letters
response = vectorizer.fit_transform(corpus)
words = vectorizer.get_feature_names_out()
df_tfidf = pd.DataFrame(response.toarray(), columns=words)

print(df_tfidf)