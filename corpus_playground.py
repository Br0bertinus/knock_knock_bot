import nltk
from nltk.corpus import gutenberg, brown

nltk.download('brown')

words = [word for word in brown.words()]

print(words)

