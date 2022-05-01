import nltk
from sklearn.cluster import KMeans
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA

import requests
from bs4 import BeautifulSoup

import seaborn as sns
sns.set(style="white", color_codes=True)
import warnings
warnings.filterwarnings("ignore")

page_url = 'https://en.wikipedia.org/wiki/Natural_language_processing'
html = requests.get(page_url)
page = BeautifulSoup(html.content, "html.parser")

# For Bonus Points
with open('input.txt', 'w', encoding='utf-8') as file:
    file.write(page.get_text())

# Reduce amount of text we are processing
working_text = page.get_text()[2000:6000]

import nltk
nltk.download('punkt')
nltk.download('universal_tagset')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('maxent_ne_chunker')
nltk.download('words')

# Tokenizing each word
w_tokens = nltk.word_tokenize(working_text)
print(w_tokens)

# Tagging each word
tagged = nltk.pos_tag(w_tokens)
print(tagged)

# Stemming each word
stemmer = nltk.stem.LancasterStemmer()
stemmed = [stemmer.stem(token) for token in w_tokens]
print(stemmed)

# Lemmatizing each word
lemmatizer = nltk.stem.WordNetLemmatizer()
lemmatized = [lemmatizer.lemmatize(token) for token in w_tokens]
print(lemmatized)

# Using Named Entity Recognition on each word
named_entity_recognition = nltk.ne_chunk(nltk.pos_tag(nltk.wordpunct_tokenize(working_text)))
print(named_entity_recognition)

# Trigramming the word_list
trigrammed = nltk.trigrams(w_tokens)
print(*trigrammed)

# Finding word counts
word_counts = [w_tokens.count(word) for word in w_tokens]
words_and_counts = set(zip(w_tokens, word_counts))
print(words_and_counts)

# Plotting the count of each word (first 20)
import matplotlib.pyplot as plt
plt.bar(w_tokens[:20], word_counts[:20])
plt.title('Word vs Count')
plt.xlabel('Word')
plt.ylabel('Count')
plt.show()

# Plotting the frequency of each word (first 20)
word_freq = [count / len(w_tokens) for count in word_counts]
plt.bar(w_tokens[:20], word_freq[:20])
plt.title('Word vs Frequency')
plt.xlabel('Word')
plt.ylabel('Frequency')
plt.show()
