# import nltk
# from nltk.tokenize import word_tokenize

# text = "Hello, I'm Eringz. Let's work together!"
# tokens = word_tokenize(text)
# print(tokens)

import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize

text = 'I am ron.'
tokens = word_tokenize(text)
print(tokens)